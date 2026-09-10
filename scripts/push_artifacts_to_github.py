#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Publie les artefacts du challenge vers votre dépôt GitHub (méthode 2 : token).

Le token est fourni par saisie **masquée** (recommandé), par variable
d'environnement, ou par le secret Colab ``GITHUB_TOKEN``. Il n'est **jamais**
affiché, jamais écrit sur disque, jamais commité : toutes les sorties passent par
``redact()``.

Ce qui est publié (par défaut) :
    models/**      tokenizer(s) entraîné(s)
    reports/**     rapports JSON / Markdown
    submissions/** (avec --include-submissions) dossier de soumission

Exemples
--------
Colab — recommandé (dans une cellule Python, champ masqué actif) :
    import sys, runpy
    sys.argv = ["push_artifacts_to_github.py", "--source", "/content", "--include-submissions"]
    try:
        runpy.run_path("/content/push_artifacts_to_github.py", run_name="__main__")
    except SystemExit as exc:
        print("code de sortie :", exc.code)

Colab — avec !python : un sous-processus n'a ni champ masqué ni Secrets, il faut
fournir le token autrement (secret exporté dans l'environnement, ou --token-file) :
    !python scripts/push_artifacts_to_github.py --source /content

Colab, en incluant le dossier de soumission :
    !python scripts/push_artifacts_to_github.py --source /content --include-submissions

Local :
    python scripts/push_artifacts_to_github.py --repo . --source .

Vérifier sans rien publier :
    python scripts/push_artifacts_to_github.py --source . --no-push

Créer explicitement une branche inexistante :
    python scripts/push_artifacts_to_github.py --source . --branch nouvelle-branche --create-branch

Publier sur une autre branche / un autre dépôt :
    python scripts/push_artifacts_to_github.py --source . --branch main \
        --repo-url https://github.com/<user>/<repo>.git
"""

from __future__ import annotations

import argparse
import getpass
import os
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

DEFAULT_REPO_URL = "https://github.com/maick-code/tokenizer.git"
DEFAULT_BRANCH = "arena/01a0889d-tokenizer"   # branche de travail (main reste intacte)
DEFAULT_MESSAGE = "Artifacts: tokenizer.json + reports (run Colab)"
ARTIFACT_DIRS = ("models", "reports")
EXCLUDE_DIR_NAMES = {"__pycache__", ".ipynb_checkpoints", ".git"}
EXCLUDE_SUFFIXES = (".pyc", ".pyo", ".zip", ".tmp", ".log")

EXIT_OK, EXIT_ERROR, EXIT_MISSING, EXIT_UNSAFE = 0, 1, 2, 3


# --------------------------------------------------------------------------- #
# Utilitaires
# --------------------------------------------------------------------------- #
def log(message: str = "") -> None:
    print(message, flush=True)


def die(message: str, code: int) -> "NoReturn":  # noqa: F821
    log(f"\nERREUR : {message}")
    raise SystemExit(code)


def redact(text: str, token: str | None) -> str:
    """Supprime toute trace du token d'une sortie."""
    if not text:
        return ""
    if token:
        text = text.replace(token, "***")
    return text


def clone_dir_default() -> Path:
    if os.path.isdir("/content"):          # Google Colab
        return Path("/content/tokenizer")
    return Path.cwd() / ".push_clone"


# --------------------------------------------------------------------------- #
# Token
# --------------------------------------------------------------------------- #
def token_from_colab_secret() -> str | None:
    try:
        from google.colab import userdata  # type: ignore

        value = userdata.get("GITHUB_TOKEN")
        return value.strip() if value else None
    except Exception:
        return None


_COLAB_MASKED_FIELD_JS = r"""
new Promise((resolve) => {
  const box = document.createElement('div');
  box.style.cssText = 'font-family:monospace;padding:10px;margin-top:6px;'
                    + 'border:1px solid #c8c8c8;border-radius:6px;display:inline-block';
  const label = document.createElement('span');
  label.textContent = 'Colle ton token GitHub puis valide : ';
  const input = document.createElement('input');
  input.type = 'password';
  input.style.cssText = 'font-size:14px;padding:3px 5px;width:330px';
  const button = document.createElement('button');
  button.textContent = 'Enregistrer';
  button.style.cssText = 'margin-left:8px;padding:3px 12px';
  const done = () => {
    input.disabled = true; button.disabled = true;
    const value = input.value; box.remove(); resolve(value);
  };
  button.addEventListener('click', done);
  input.addEventListener('keydown', (event) => { if (event.key === 'Enter') done(); });
  box.appendChild(label); box.appendChild(input); box.appendChild(button);
  document.body.appendChild(box);
  input.focus();
})
"""


def token_from_colab_masked_field() -> str | None:
    """Champ de saisie masqué natif Colab (nécessite d'exécuter le script EN PROCESSUS).

    Fonctionne quand le script est lancé dans une cellule Python (``runpy``), pas
    avec ``!python`` : un sous-processus n'a pas accès à l'interface du notebook.
    """
    try:
        from google.colab import output  # type: ignore
    except Exception:
        return None
    try:
        value = output.eval_js(_COLAB_MASKED_FIELD_JS)
    except Exception as exc:
        log(f"Champ masqué Colab indisponible ({type(exc).__name__}) : repli sur la saisie classique.")
        return None
    if isinstance(value, str) and value.strip():
        log("Token saisi dans le champ masqué Colab (non affiché).")
        return value.strip().strip('"').strip("'")
    return None


def read_token(args: argparse.Namespace) -> str | None:
    """Token par ordre de priorité : --token-file, env, secret Colab, champ masqué Colab, saisie."""
    if args.token_file:
        path = Path(args.token_file)
        if not path.is_file():
            die(f"fichier de token introuvable : {path}", EXIT_ERROR)
        token = path.read_text(encoding="utf-8").strip()
        if token:
            log("Token lu depuis le fichier indiqué (--token-file).")
            return token

    for var in ("GITHUB_TOKEN", "GH_TOKEN"):
        token = os.environ.get(var)
        if token:
            log(f"Token récupéré depuis la variable d'environnement {var}.")
            return token.strip()

    token = token_from_colab_secret()
    if token:
        log("Token récupéré depuis le secret Colab 'GITHUB_TOKEN'.")
        return token

    if args.no_input:
        return None

    token = token_from_colab_masked_field()
    if token:
        return token

    prompt = "Colle ton token GitHub puis Entrée : "
    try:
        token = getpass.getpass(prompt)          # saisie masquée
    except Exception:
        try:
            token = input(prompt)                # repli si getpass indisponible
        except Exception:
            return None
    token = (token or "").strip().strip('"').strip("'")
    if token:
        log(f"Token saisi ({len(token)} caractères, non affiché).")
    return token or None


def authed_url(url: str, token: str | None) -> str:
    """URL https porteuse du token, uniquement pour github.com."""
    if token and url.startswith("https://github.com/"):
        return url.replace("https://", f"https://x-access-token:{token}@")
    return url


# --------------------------------------------------------------------------- #
# Git
# --------------------------------------------------------------------------- #
def git(repo: Path | str | None, *args: str) -> subprocess.CompletedProcess:
    command = ["git"]
    if repo is not None:
        command += ["-C", str(repo)]
    return subprocess.run(command + list(args), capture_output=True, text=True)


def git_or_die(repo: Path | str | None, token: str | None, *args: str,
               what: str = "commande git") -> subprocess.CompletedProcess:
    result = git(repo, *args)
    if result.returncode != 0:
        die(f"{what} a échoué :\n{redact(result.stderr or result.stdout, token).strip()}",
            EXIT_ERROR)
    return result


# --------------------------------------------------------------------------- #
# Artefacts
# --------------------------------------------------------------------------- #
def collect_artifacts(source: Path, include_submissions: bool) -> list[str]:
    """Chemins relatifs (posix) des fichiers à publier, triés."""
    roots = list(ARTIFACT_DIRS) + (["submissions"] if include_submissions else [])
    files: list[str] = []
    for root in roots:
        base = source / root
        if not base.is_dir():
            continue
        for path in sorted(base.rglob("*")):
            if not path.is_file():
                continue
            parts = set(path.relative_to(source).parts)
            if parts & EXCLUDE_DIR_NAMES or path.name.startswith("."):
                continue
            if path.suffix.lower() in EXCLUDE_SUFFIXES:
                continue
            files.append(path.relative_to(source).as_posix())
    return files


def safety_checks(source: Path, files: list[str], force: bool) -> list[str]:
    """Contrôles avant publication. Retourne la liste des avertissements bloquants."""
    import json

    problems: list[str] = []

    baseline = source / "reports" / "baseline_bpe_10k.json"
    if baseline.is_file():
        try:
            status = json.loads(baseline.read_text(encoding="utf-8")).get("status")
            if status != "computed_on_official_dataset":
                problems.append(
                    f"reports/baseline_bpe_10k.json : status = {status!r} "
                    "(run non conforme au dataset officiel)")
        except Exception as exc:
            problems.append(f"reports/baseline_bpe_10k.json illisible : {exc}")

    sweep = source / "reports" / "optimization_sweep.json"
    if sweep.is_file():
        try:
            payload = json.loads(sweep.read_text(encoding="utf-8"))
            rows = (payload.get("dataset") or {}).get("validation_rows")
            if rows != 24_000:
                problems.append(
                    f"reports/optimization_sweep.json : validation_rows = {rows} "
                    "(attendu 24 000 : le balayage n'a pas tourné sur le vrai dataset)")
        except Exception as exc:
            problems.append(f"reports/optimization_sweep.json illisible : {exc}")

    if not any(f.startswith("models/") and f.endswith("tokenizer.json") for f in files):
        problems.append("aucun models/**/tokenizer.json trouvé dans les artefacts")

    # Une soumission = UN dossier. Un dossier obsolète laissé par une exécution antérieure
    # (ancien slug, par exemple après avoir renommé SLUG) rendrait la PR invalide : le
    # checker officiel exige exactement un répertoire `submissions/<slug>/`.
    subs = source / "submissions"
    if subs.is_dir():
        slugs = sorted(p.name for p in subs.iterdir()
                       if p.is_dir() and (p / "tokenizer.json").is_file())
        if len(slugs) > 1:
            problems.append(
                f"plusieurs dossiers de soumission dans submissions/ : {', '.join(slugs)} "
                "(un seul slug est autorisé par PR ; supprimez les dossiers obsolètes)")

    if problems and not force:
        log("\n" + "!" * 74)
        log("PUBLICATION REFUSÉE — les artefacts semblent ne pas venir d'un run réel :")
        for problem in problems:
            log(f"  - {problem}")
        log("Corrigez le run, ou relancez avec --force pour publier quand même.")
        log("!" * 74)
        raise SystemExit(EXIT_UNSAFE)

    if problems:
        log("\nAVERTISSEMENT (--force) :")
        for problem in problems:
            log(f"  - {problem}")
    return problems


# --------------------------------------------------------------------------- #
# Programme principal
# --------------------------------------------------------------------------- #
def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Publie models/ et reports/ vers votre dépôt GitHub (méthode token).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--source", default="/content" if os.path.isdir("/content") else ".",
                        help="répertoire contenant models/ et reports/ (défaut : /content ou .)")
    parser.add_argument("--repo", default=None,
                        help="clone git existant du dépôt (sinon clonage automatique)")
    parser.add_argument("--repo-url", default=DEFAULT_REPO_URL, help="URL https du dépôt")
    parser.add_argument("--branch", default=DEFAULT_BRANCH, help="branche cible")
    parser.add_argument("--message", default=DEFAULT_MESSAGE, help="message de commit")
    parser.add_argument("--token-file", default=None,
                        help="lire le token depuis un fichier (évite la saisie)")
    parser.add_argument("--no-input", action="store_true",
                        help="ne jamais demander le token de façon interactive")
    parser.add_argument("--no-push", action="store_true",
                        help="copier et commiter sans pousser")
    parser.add_argument("--include-submissions", action="store_true",
                        help="publier aussi submissions/**")
    parser.add_argument("--zip", action="store_true",
                        help="créer en plus une archive de secours dans --source")
    parser.add_argument("--force", action="store_true",
                        help="publier malgré les avertissements de conformité")
    parser.add_argument("--create-branch", action="store_true",
                        help="autoriser la création de la branche si elle n'existe pas")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    source = Path(args.source).resolve()
    branch = args.branch
    repo_url = args.repo_url

    log("=" * 74)
    log("Publication des artefacts vers GitHub")
    log("=" * 74)
    log(f"Source      : {source}")
    log(f"Dépôt       : {repo_url}")
    log(f"Branche     : {branch}")
    log(f"Artefacts   : {', '.join(ARTIFACT_DIRS + (('submissions',) if args.include_submissions else ()))}")
    log()

    files = collect_artifacts(source, args.include_submissions)
    if not files:
        die(f"aucun artefact trouvé dans {source} (attendu : models/, reports/)", EXIT_MISSING)

    log(f"{len(files)} fichier(s) à publier :")
    total = 0
    for rel in files:
        size = (source / rel).stat().st_size
        total += size
        log(f"  {size:>12,} o  {rel}")
    log(f"  {'-' * 12}")
    log(f"  {total:>12,} o  total")

    safety_checks(source, files, args.force)

    if args.zip:
        archive = source / "artifacts_backup.zip"
        with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as handle:
            for rel in files:
                handle.write(source / rel, rel)
        log(f"\nArchive de secours : {archive} ({archive.stat().st_size:,} o)")

    token = read_token(args)

    repo = Path(args.repo).resolve() if args.repo else clone_dir_default()

    if not (repo / ".git").exists():
        if not token:
            die("aucun token fourni et pas de clone local : impossible de cloner.", EXIT_ERROR)
        log(f"\nClone de {repo_url} (branche {branch}) dans {repo} ...")
        clone = subprocess.run(
            ["git", "clone", "--branch", branch, authed_url(repo_url, token), str(repo)],
            capture_output=True, text=True)
        if clone.returncode != 0:
            die("clonage impossible (token invalide, branche inexistante ou réseau) :\n"
                f"{redact(clone.stderr or clone.stdout, token).strip()}", EXIT_ERROR)
        log("clone : OK")
    else:
        log(f"\nClone existant réutilisé : {repo}")

    if token:
        check = git(repo, "ls-remote", "--heads", authed_url(repo_url, token), branch)
        if check.returncode != 0:
            die("authentification refusée : vérifiez la portée `repo` du token,"
                " sa date d'expiration et le nom de la branche.", EXIT_ERROR)
        log("authentification : OK")

    # La branche cible doit exister : sans ce contrôle, une faute de frappe
    # créerait silencieusement une nouvelle branche distante.
    exists = git(None, "ls-remote", "--heads",
                 authed_url(repo_url, token) if token else repo_url, branch)
    if exists.returncode == 0 and not exists.stdout.strip():
        if args.create_branch:
            log(f"branche '{branch}' absente du dépôt : elle sera créée (--create-branch).")
        else:
            die(f"la branche '{branch}' n'existe pas sur {repo_url}.\n"
                "Vérifiez le nom (--branch), ou utilisez --create-branch pour la créer.",
                EXIT_ERROR)
    elif exists.returncode != 0 and not token:
        log("(impossible de vérifier la branche sans token : le push tranchera.)")

    # --- resynchronisation ---------------------------------------------------
    # Un clone Colab réutilisé (ou un clone créé dans une session précédente) peut être
    # en retard sur la branche distante : le commit local ne serait alors pas un
    # fast-forward et le push serait refusé. On se replace d'abord sur la tête distante ;
    # les artefacts étant recopiés juste après, rien n'est perdu.
    fetch = git(repo, "fetch", authed_url(repo_url, token) if token else repo_url, branch)
    if fetch.returncode == 0:
        ancestor = git(repo, "merge-base", "--is-ancestor", "FETCH_HEAD", "HEAD")
        if ancestor.returncode == 0:
            log("clone à jour avec la branche distante.")
        else:
            local = git(repo, "rev-parse", "--short", "HEAD").stdout.strip()
            remote = git(repo, "rev-parse", "--short", "FETCH_HEAD").stdout.strip()
            log(f"clone en retard ({local}) sur la branche distante ({remote}) : "
                "resynchronisation sur la tête distante (les artefacts sont recopiés ensuite).")
            git_or_die(repo, token, "checkout", "-B", branch, "FETCH_HEAD",
                       what=f"git checkout -B {branch} {remote}")
    else:
        log("fetch impossible (réseau ?) : on tente le push tel quel.")

    for rel in files:
        destination = repo / rel
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source / rel, destination)
    log(f"{len(files)} fichier(s) copié(s) dans le clone.")

    git(repo, "config", "user.name", "Artifact Publisher")
    git(repo, "config", "user.email", "publisher@users.noreply.github.com")
    for root in {Path(rel).parts[0] for rel in files}:
        git_or_die(repo, token, "add", root, what=f"git add {root}")

    commit = git(repo, "commit", "-m", args.message)
    if commit.returncode == 0:
        log("commit : OK")
    elif "nothing to commit" in (commit.stdout + commit.stderr):
        log("commit : rien de nouveau (artefacts identiques)")
    else:
        die(f"commit impossible :\n{redact(commit.stderr or commit.stdout, token).strip()}",
            EXIT_ERROR)

    if args.no_push:
        log("\n--no-push : publication non effectuée. Commande manuelle :")
        log(f"  git -C {repo} push {repo_url} HEAD:{branch}")
        return EXIT_OK

    if not token:
        log("\nAucun token : publication non effectuée. Commande manuelle :")
        log(f"  git -C {repo} push {repo_url} HEAD:{branch}")
        return EXIT_OK

    push = git(repo, "push", authed_url(repo_url, token), f"HEAD:{branch}")
    if push.returncode != 0:
        die(f"push refusé :\n{redact(push.stderr or push.stdout, token).strip()}", EXIT_ERROR)

    log("push : OK")
    log()
    log(f"Publié sur {repo_url} (branche {branch}).")
    if "github.com" in repo_url:
        slug = repo_url.rstrip("/").removesuffix(".git")
        log(f"Vérifiez : {slug}/tree/{branch}")
    return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main())
