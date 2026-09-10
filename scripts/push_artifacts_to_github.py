#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pousse les artefacts de la baseline BPE 10K vers GitHub.

Utilisable depuis Google Colab (après avoir exécuté le notebook) OU en local.

Le token GitHub n'est JAMAIS écrit dans le dépôt : il est lu depuis
- le secret Colab ``GITHUB_TOKEN`` (Colab ▸ icône clé 🔑 ▸ Notebook access), ou
- la variable d'environnement ``GITHUB_TOKEN``.

Exemples
--------
Colab (après le run du notebook) :
    !python push_artifacts_to_github.py --source /content

Local (artefacts déjà présents dans le dépôt) :
    GITHUB_TOKEN=xxx python push_artifacts_to_github.py --repo . --source .

Sans token (n'effectue que copie + commit, et affiche la commande de push) :
    python push_artifacts_to_github.py --repo /chemin/vers/tokenizer
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

DEFAULT_REPO_URL = "https://github.com/maick-code/tokenizer.git"
DEFAULT_BRANCH = "arena/01a0889d-tokenizer"  # branche de travail (main reste intacte)
CLONE_DIR = Path("/content/tokenizer")

# Chemins relatifs à la racine des artefacts (source), identiques dans le dépôt.
ARTIFACTS = [
    "models/baseline_bpe_10k/tokenizer.json",
    "reports/baseline_bpe_10k.json",
    "reports/baseline_bpe_10k.md",
]
COMMIT_MESSAGE = "Baseline BPE 10K: tokenizer.json + reports (Colab run)"


def get_token() -> str | None:
    """Token depuis Colab Secrets ou l'environnement. Jamais journalisé."""
    try:  # environnements Colab
        from google.colab import userdata  # type: ignore

        token = userdata.get("GITHUB_TOKEN")
        if token:
            return token
    except Exception:
        pass
    return os.environ.get("GITHUB_TOKEN")


def authed_url(url: str, token: str | None) -> str:
    if token and url.startswith("https://github.com/"):
        return url.replace("https://", f"https://x-access-token:{token}@")
    return url


def git(repo: Path | str, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True)


def redact(text: str, token: str | None) -> str:
    return text.replace(token, "***") if token else text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--source", default="/content", help="répertoire contenant models/ et reports/ (défaut : /content)")
    parser.add_argument("--repo", default=None, help="clone existant du dépôt ; sinon il est cloné dans /content/tokenizer")
    parser.add_argument("--repo-url", default=DEFAULT_REPO_URL)
    parser.add_argument("--branch", default=DEFAULT_BRANCH)
    parser.add_argument("--zip", action="store_true", help="créer aussi baseline_bpe_10k_artifacts.zip dans --source")
    parser.add_argument("--no-push", action="store_true", help="copier et commiter sans pousser")
    args = parser.parse_args()

    source = Path(args.source).resolve()
    missing = [rel for rel in ARTIFACTS if not (source / rel).exists()]
    for rel in ARTIFACTS:
        state = "OK    " if (source / rel).exists() else "ABSENT"
        print(f"{state} {source / rel}")
    if missing:
        print("\nArtefacts manquants : lancez d'abord le notebook (`Runtime ▸ Run all`).", file=sys.stderr)
        return 2

    if args.zip:
        archive = source / "baseline_bpe_10k_artifacts.zip"
        with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as zf:
            for rel in ARTIFACTS:
                zf.write(source / rel, rel)
        print(f"\nArchive : {archive} ({archive.stat().st_size:,} octets)")

    token = get_token()
    print(f"\nToken GitHub : {'détecté' if token else 'absent (copie + commit seulement)'}")

    repo = Path(args.repo).resolve() if args.repo else None
    if repo is None:
        repo = CLONE_DIR if CLONE_DIR.exists() else Path.cwd() / "tokenizer"

    if not (repo / ".git").exists():
        print(f"Clone de {args.repo_url} (branche {args.branch}) dans {repo} ...")
        clone = subprocess.run(
            ["git", "clone", "--branch", args.branch, authed_url(args.repo_url, token), str(repo)],
            capture_output=True, text=True,
        )
        print("clone :", "OK" if clone.returncode == 0 else "ECHEC")
        if clone.returncode != 0:
            print(redact(clone.stderr or clone.stdout, token)[-800:])
            return 1

    for rel in ARTIFACTS:
        dest = repo / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source / rel, dest)
        print(f"copié -> {dest}")

    git(repo, "config", "user.name", "Colab Runner")
    git(repo, "config", "user.email", "colab@users.noreply.github.com")
    git(repo, "add", *["models", "reports"])
    commit = git(repo, "commit", "-m", COMMIT_MESSAGE)
    nothing = "nothing to commit" in (commit.stdout + commit.stderr)
    print("commit :", "OK" if commit.returncode == 0 else ("rien à commiter" if nothing else "ECHEC"))
    if commit.returncode != 0 and not nothing:
        print(redact(commit.stderr or commit.stdout, token)[-800:])

    if args.no_push or not token:
        print("\nPush non effectué. Commande manuelle :")
        print(f"  git -C {repo} push {args.repo_url} HEAD:{args.branch}")
        return 0

    push = subprocess.run(
        ["git", "-C", str(repo), "push", authed_url(args.repo_url, token), f"HEAD:{args.branch}"],
        capture_output=True, text=True,
    )
    print("push   :", "OK" if push.returncode == 0 else "ECHEC")
    if push.returncode != 0:
        print(redact(push.stderr or push.stdout, token)[-800:])
        return 1
    print(f"Poussé vers {args.repo_url} (branche {args.branch})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
