# tokenizer — AIMS Africa Multilingual Tokenizer Challenge

[Challenge officiel](https://airf.aims.ac.za/community/africa-multilingual-tokenizer-challenge/) ·
[dépôt d'évaluation officiel](https://github.com/aims-ai-research-foundations/airf-multilingual-tokenizer-challenge) ·
[dataset](https://huggingface.co/datasets/Similoluwa/african-multilingual-tokenizer-challenge)

## Statut actuel

| Élément | Valeur |
|---|---|
| Étape 1 | **Baseline `BPE 10K`** → score officiel **2.059977** (guardrails EN/FR **PASS**) |
| Étape 2 | **`02_optimization_sweep.ipynb`** — balayage de configurations avec la métrique officielle (à exécuter dans Colab) |
| Dataset | `Similoluwa/african-multilingual-tokenizer-challenge` — révision `v1.0.0` |
| Splits | `train` 240 000 (40 000/langue) · `validation` 24 000 (4 000/langue) |
| Métrique | `score = fertility + 100 × unk_rate`, moyenne sur `ha`, `sw`, `yo`, `am` |
| Version imposée | **`tokenizers==0.22.1`** (le checker officiel vérifie l'égalité exacte) |
| Vocabulaire max | 10 000 (`get_vocab_size(with_added_tokens=True)`) |
| Taille max `tokenizer.json` | 20 MiB |

> ✅ **Vérifié avec le code officiel du challenge** (celui de l'évaluateur) : le tokenizer de la
> baseline **passe** le checker officiel (`valid=True`, vocab 10 000, 503,8 KiB) et le **guardrail
> EN/FR est PASS**. Voir « Résultats de la baseline » plus bas.
>
> ⚠️ L'environnement de développement (Arena) n'a **pas** accès réseau à Hugging Face : les
> entraînements tournent dans **Google Colab**, les scores réels sont calculés là-bas.

## Règles officielles (extraites du code du challenge, pas supposées)

Fichiers de référence : `competition/constants.py`, `competition/metrics.py`,
`competition/validation.py`, `competition/submissions.py`, `starter/utils.py`.

```python
SCORED_LANGUAGES = ("ha", "sw", "yo", "am")     # seules langues notées
CONTEXT_LANGUAGES = ("en", "fr")                # guardrail
CONTEXT_FERTILITY_RATIO = 1.15
UNKNOWN_PENALTY = 100.0
MAX_VOCAB_SIZE = 10_000
MAX_TOKENIZER_BYTES = 20 * 1024 * 1024
SUPPORTED_TOKENIZERS_VERSION = "0.22.1"
```

- **Mot** = `len(text.split())` · **fertility** = `tokens / words` · **score** = `fertility + 100 × unk_rate`.
- **Score final** = moyenne des scores de `ha`, `sw`, `yo`, `am` (plus bas = meilleur).
- **Guardrail EN/FR** :
  ```python
  budget = 1.15 × moyenne(fertility BRUTE de ha, sw, yo, am)
  # échec si fertility["en"] > budget OU fertility["fr"] > budget  -> soumission invalide
  ```
  ⚠️ Le budget est **relatif à votre propre tokenizer** : améliorer beaucoup les langues notées
  **abaisse** le budget et peut casser le guardrail. `02_optimization_sweep.ipynb` vérifie donc le
  guardrail pour **chaque** configuration.
- **Contraintes** : un seul tokenizer pour 6 langues ; entraînement **uniquement** sur le `train`
  fourni (aucun corpus externe, aucun tokenizer pré-entraîné) ; le tokenizer doit fonctionner
  **sans code du participant** ; temps d'évaluation ≤ 5× celui de la baseline.

### Soumission (workflow officiel)

1. *Fork* de `aims-ai-research-foundations/airf-multilingual-tokenizer-challenge`.
2. Branche nommée **exactement `submission`**.
3. Un dossier `submissions/<slug>/` (slug en minuscules kebab-case) contenant :
   `tokenizer.json` (obligatoire), `metadata.yml` (obligatoire), `notebook.ipynb` (avant la date
   limite), `README.md` (optionnel). **Rien d'autre** — pas de symlink, `metadata.yml` ≤ 16 KiB.
4. *Pull Request* vers le dépôt officiel (la PR ne doit toucher **que** `submissions/<slug>/`).

## Résultats de la baseline (valeurs réelles, split `validation`)

| Language | Words | Tokens | Fertility | UNK | UNK Rate | Score |
|---|---:|---:|---:|---:|---:|---:|
| English | 88 469 | 167 141 | 1.8893 | 5 | 0.000057 | 1.8949 |
| French | 90 652 | 180 295 | 1.9889 | 63 | 0.000695 | 2.0584 |
| Hausa* | 89 819 | 154 957 | **1.7252** | 43 | 0.000479 | **1.7731** |
| Swahili* | 69 832 | 133 438 | 1.9108 | 2 | 0.000029 | **1.9137** |
| Yoruba* | 85 758 | 161 700 | 1.8855 | 12 | 0.000140 | **1.8995** |
| Amharic* | 79 413 | 197 729 | **2.4899** | 130 | 0.001637 | **2.6536** |
| | | | | | **Target average** | **2.059977** |

`*` = langues notées. Vocabulaire réel : **10 000 / 10 000**. Guardrail officiel :
`budget = 1.15 × 2.002869 = 2.303300` → English 1.8893 **PASS** (marge +0.4140),
French 1.9889 **PASS** (marge +0.3144).

Diagnostic : l'**amharique** domine le score (2,4899 = 1,32× l'anglais, 130 `[UNK]`) ; le
**hausa** est le plus efficace (0,91× l'anglais). Les 255 `[UNK]` proviennent de **résidus
multilingues de Wikipédia** (CJK, kana, hangul, formes de présentation arabes, cyrillique,
hébreu, syriaque, emoji), **jamais** des diacritiques yoruba/hausa ni du guèze.

> ℹ️ Le fichier `reports/baseline_bpe_10k.json` a été produit **avant** la lecture des règles
> officielles : son champ `12_guardrails` indique `N/A`. Le verdict vérifié avec le code officiel
> du challenge (**PASS / PASS**, budget 2.303300) est consigné dans
> `reports/official_check_baseline.json`, avec le test d'équivalence de la métrique.

## Structure du projet

```text
tokenizer/
├── README.md
├── .gitignore
├── notebooks/
│   ├── 01_baseline_bpe_10k.ipynb      # Étape 1 : baseline BPE 10K (scores de référence)
│   └── 02_optimization_sweep.ipynb    # Étape 2 : balayage d'optimisation (métrique officielle)
├── scripts/
│   └── push_artifacts_to_github.py    # pousse models/ + reports/ vers GitHub
├── models/
│   └── baseline_bpe_10k/tokenizer.json
└── reports/
    ├── baseline_bpe_10k.json
    └── baseline_bpe_10k.md
```

## Exécution dans Google Colab (instructions exactes)

1. Ouvrir <https://colab.research.google.com>.
2. `File` → `Open notebook` → onglet **GitHub** → `maick-code/tokenizer` →
   sélectionner `notebooks/01_baseline_bpe_10k.ipynb`  
   (ou `File` → `Upload notebook` puis déposer le fichier).
3. Menu `Runtime` → `Run all` (exécution de haut en bas, aucune intervention requise).
4. Le notebook installe lui-même les dépendances :
   `!pip install -q datasets tokenizers pandas numpy`
5. Le dataset officiel est chargé automatiquement depuis Hugging Face :
   ```python
   dataset = load_dataset(
       "Similoluwa/african-multilingual-tokenizer-challenge",
       revision="v1.0.0",
   )
   ```

**Artefacts produits** (dans le répertoire courant de Colab, `/content`) :

```text
/content/models/baseline_bpe_10k/tokenizer.json
/content/reports/baseline_bpe_10k.json
/content/reports/baseline_bpe_10k.md
```

### ⚠️ Pourquoi les rapports n'apparaissent pas sur GitHub ?

Parce que **Colab ne pousse jamais rien sur GitHub tout seul**. Colab exécute le code sur une
machine temporaire ; quand on ouvre un notebook depuis GitHub, le dépôt n'est **pas** cloné
(seul le notebook est copié en mémoire). Les fichiers générés existent donc uniquement dans la
VM Colab : `/content/models/...` et `/content/reports/...`, jusqu'à l'extinction de la VM.

La section **18** du notebook publie tout automatiquement (méthode 2 : avec token GitHub) :

1. **Créer le token** (une seule fois) : GitHub → *Settings* → *Developer settings* →
   *Personal access tokens* → *Tokens (classic)* → **Generate new token (classic)** →
   cocher la portée **`repo`** → générer et copier le token (`ghp_...`).
2. **Exécuter le notebook** (`Runtime ▸ Run all`), puis la cellule **18.1** : un champ de saisie
   masqué s'affiche → **coller le token** → Entrée.
3. Exécuter la cellule **18.2** : elle vérifie le token, clone le dépôt, copie
   `models/` + `reports/`, commite et **pousse**.
   La branche cible se règle en haut de la cellule — par défaut
   `BRANCH = "arena/01a0889d-tokenizer"` : **`main` n'est pas touchée**.
4. Vérifier :
   <https://github.com/maick-code/tokenizer/tree/arena/01a0889d-tokenizer/reports>.

> **Branche cible** (ligne `BRANCH` dans la cellule 18.2) :
> - `BRANCH = "arena/01a0889d-tokenizer"` *(valeur par défaut)* → tout va sur la branche de
>   travail, `main` reste totalement intacte ;
> - `BRANCH = "main"` → à n'utiliser que si l'on veut publier directement sur la branche par
>   défaut du dépôt.

> Alternative sans champ de saisie : si un secret Colab nommé `GITHUB_TOKEN` existe
> (icône 🔑 → *Add new secret* → *Notebook access*), la cellule 18.1 le détecte et l'utilise
> directement.

Le token n'est **jamais** écrit dans le dépôt, jamais affiché (les sorties sont masquées via `***`)
et ne doit **jamais** être partagé dans un chat. S'il fuit : le révoquer immédiatement
(*Settings → Developer settings → Tokens → Delete*).

> Le `.gitignore` n'exclut volontairement **pas** `models/` et `reports/` : ils doivent pouvoir
> être commités. Seuls les caches (`.cache/huggingface/`, `__pycache__/`, etc.) sont ignorés.

## Script de publication (méthode token)

`scripts/push_artifacts_to_github.py` publie `models/**` + `reports/**` (et `submissions/**`
avec `--include-submissions`) vers votre dépôt, en **une seule commande**, avec le token demandé
par **saisie masquée**.

### 1. Créer le token

GitHub → *Settings* → *Developer settings* → *Personal access tokens* → *Tokens (classic)* →
**Generate new token (classic)** → portée **`repo`** → copier le token (`ghp_...`).

### 2. Utilisation dans Google Colab (recommandé)

⚠️ Dans Colab, `!python script.py` lance un **sous-processus** : il n'a ni accès aux Secrets
Colab, ni à l'interface du notebook (donc **pas de champ masqué**). Pour avoir la saisie masquée,
exécuter le script **dans une cellule Python** :

```python
# cellule 1 — récupérer le script
!wget -q https://raw.githubusercontent.com/maick-code/tokenizer/arena/01a0889d-tokenizer/scripts/push_artifacts_to_github.py

# cellule 2 — publier (un champ masqué « Colle ton token GitHub puis valide » apparaît)
import sys, runpy
sys.argv = ["push_artifacts_to_github.py", "--source", "/content"]
try:
    runpy.run_path("/content/push_artifacts_to_github.py", run_name="__main__")
except SystemExit as exc:
    print("code de sortie :", exc.code)
```

Pour inclure le dossier de soumission :

```python
sys.argv = ["push_artifacts_to_github.py", "--source", "/content", "--include-submissions"]
```

**Variante sans rien taper** (le token est lu dans un secret Colab) :

1. Colab → icône **clé 🔑** → *Add new secret* → *Name* : `GITHUB_TOKEN` → *Value* : votre token
   → activer **Notebook access**.
2. Le script le détecte automatiquement (priorité sur le champ masqué), en cellule Python **ou**
   avec `!python` :

```python
from google.colab import userdata
import os
os.environ["GITHUB_TOKEN"] = userdata.get("GITHUB_TOKEN")   # mémoire seulement
!python push_artifacts_to_github.py --source /content
```

### 2bis. Utilisation en local

```bash
python scripts/push_artifacts_to_github.py --source .
```

Sans saisie (token dans l'environnement) :

```bash
GITHUB_TOKEN=ghp_xxx python scripts/push_artifacts_to_github.py --source .
```

### 3. Options principales

| Option | Effet |
|---|---|
| `--source DIR` | répertoire contenant `models/` et `reports/` (défaut `/content` en Colab, sinon `.`) |
| `--branch NAME` | branche cible (défaut `arena/01a0889d-tokenizer`) |
| `--repo-url URL` | autre dépôt |
| `--include-submissions` | publier aussi `submissions/**` |
| `--message TXT` | message de commit |
| `--no-push` | copier + commiter sans pousser |
| `--zip` | créer en plus `artifacts_backup.zip` |
| `--create-branch` | autoriser la création d'une branche inexistante |
| `--force` | publier malgré un avertissement de conformité |
| `--no-input` | ne jamais demander le token (mode automatisé) |

### 4. Garde-fous

- **Refuse de publier des artefacts non conformes** (ex. run sur données synthétiques) :
  contrôle de `reports/baseline_bpe_10k.json` (`status`) et de
  `reports/optimization_sweep.json` (`validation_rows == 24 000`) → `--force` pour passer outre.
- **Refuse une branche inexistante** (une faute de frappe ne crée plus de branche silencieusement)
  → `--create-branch` pour la créer volontairement.
- Le **token n'est jamais affiché, écrit sur disque ni commité** (sorties filtrées par `***`).
- Codes de sortie : `0` succès · `1` erreur · `2` artefacts manquants · `3` publication refusée.

## Configuration de la baseline (figée — ne pas modifier pour cette expérience)

```python
from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.normalizers import NFC
from tokenizers.pre_tokenizers import Whitespace
from tokenizers.trainers import BpeTrainer

tokenizer = Tokenizer(BPE(unk_token="[UNK]"))
tokenizer.normalizer = NFC()
tokenizer.pre_tokenizer = Whitespace()

trainer = BpeTrainer(
    vocab_size=10_000,
    min_frequency=2,
    special_tokens=["[UNK]"],
)
```

Contraintes respectées :

- Entraînement **uniquement** sur `dataset["train"]`, évaluation **uniquement** sur
  `dataset["validation"]`.
- Dataset déjà NFC : **aucune** conversion ASCII, **aucun** `StripAccents`,
  **aucun** NFD/NFKD + suppression d'accents, **aucun** `lowercase`.
- Pas d'optimisation pour cette baseline (pas de ByteLevel, UnicodeScripts,
  ParityBpeTrainer, WordPiece, Unigram, autre `vocab_size` ou autre `min_frequency`).

## Étape 2 — optimisation (`notebooks/02_optimization_sweep.ipynb`)

Balayage de configurations **avec la métrique officielle**, exécutable dans Colab après avoir
remplacé le dataset réel (le notebook charge le dataset officiel lui-même) :

1. `b1-baseline` — référence (doit redonner ≈ 2.0600).
2. `c2-wssplit-mf2` — pré-tokeniseur `WhitespaceSplit` (la ponctuation reste collée au mot :
   le baseline dépensait ~43 000 tokens sur la validation pour `,` et `.` isolés).
3. `c3-wssplit-mf5` — + `min_frequency=5`.
4. `c4-wssplit-mf10-alpha` — + `min_frequency=10` + alphabet initial complet (supprime les `[UNK]`).
5. `c5-bytelevel` — `ByteLevel(use_regex=True)` : round-trip sans perte, zéro `[UNK]`
   (mais coûteux en octets pour l'éthiopien : à mesurer).
6. `c6-unigram-alpha` — modèle **Unigram** + alphabet complet.
7. `c7-…-amboost` — sur-échantillonnage de l'amharique (×2).
8. `c8-scoredboost` — sur-échantillonnage des 4 langues notées (teste la limite du guardrail).

Le notebook : entraîne, évalue (score + guardrail **par configuration**), classe, sauvegarde le
meilleur (`models/optimized_<config>/tokenizer.json`), écrit `reports/optimization_sweep.{json,md}`,
génère `submissions/<slug>/` et exécute le **checker officiel** (`starter/utils.py`).

> ⚙️ `MAX_TRAIN_DOCS = 60_000` dans la cellule 2 permet un pré-balayage rapide avant de relancer
> les 2–3 meilleures configurations sur les 240 000 textes.

## Guardrails English / French — règle officielle

Le guardrail est **relatif** (voir « Règles officielles ») :
`budget = 1.15 × moyenne(fertility brute de ha, sw, yo, am)` ; échec si `fertility(en)` ou
`fertility(fr)` dépasse ce budget. Les deux notebooks l'implémentent et affichent un verdict
`PASS`/`FAIL` explicite (plus aucun seuil supposé).
