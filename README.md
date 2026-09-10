# tokenizer — AIMS Africa Multilingual Tokenizer Challenge

Baselines et expériences de tokenizer pour le **AIMS Africa Multilingual Tokenizer Challenge**.

## Statut actuel

| Élément | Valeur |
|---|---|
| Expérience | **Baseline `BPE 10K`** (aucune optimisation) |
| Dataset | `Similoluwa/african-multilingual-tokenizer-challenge` |
| Révision | `v1.0.0` |
| Pipeline | Dataset officiel → NFC → Whitespace → BPE → 10 000 tokens max → Évaluation |
| Split d'entraînement | `train` (240 000 exemples, 40 000/langue) |
| Split d'évaluation | `validation` (24 000 exemples, 4 000/langue) |
| Métrique | `score = fertility + 100 * unk_rate`, `fertility = tokens / words` |
| Score cible | Moyenne sur `ha`, `sw`, `yo`, `am` |

> ⚠️ **Aucun score n'est fabriqué.** L'environnement de développement (Arena) n'a pas
> accès réseau à Hugging Face : le notebook n'a donc **pas** pu être exécuté sur le
> dataset réel ici. Il est conçu pour être exécuté de haut en bas dans **Google Colab**
> et calcule alors tous les scores réels (vocabulaire, fertility, UNK rate, score,
> rapports). Les artefacts `models/…` et `reports/…` produits par Colab peuvent ensuite
> être commités dans ce dépôt.

## Structure du projet

```text
tokenizer/
├── README.md
├── .gitignore
├── notebooks/
│   └── 01_baseline_bpe_10k.ipynb   # Baseline BPE 10K (Colab-ready, auto-suffisant)
├── models/                          # créé par le notebook en Colab
│   └── baseline_bpe_10k/
│       └── tokenizer.json
└── reports/                         # créé par le notebook en Colab
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

## Guardrails English / French

La documentation publique du challenge accessible (fiche Hugging Face du dataset à la
révision `v1.0.0`, vérifiée le 10/09/2026) **ne définit pas de seuil numérique officiel**
pour les guardrails English/French. Le notebook affiche donc les scores English/French
réels mais **n'affirme pas** de verdict `PASS`/`FAIL` tant qu'aucun seuil officiel n'est
fourni. Dès que les règles officielles sont disponibles, renseigner dans le notebook :

```python
EN_GUARDRAIL_MAX_SCORE = None   # ex. valeur limite officielle
FR_GUARDRAIL_MAX_SCORE = None
```

Le verdict `PASS`/`FAIL` est alors calculé (jamais supposé).
