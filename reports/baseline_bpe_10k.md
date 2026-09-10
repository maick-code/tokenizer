# Baseline BPE 10K — AIMS Africa Multilingual Tokenizer Challenge

*Généré le 2026-09-10 00:31 UTC par `notebooks/01_baseline_bpe_10k.ipynb`.*

## 1. Dataset utilisé

- Nom : `Similoluwa/african-multilingual-tokenizer-challenge`
- URL : https://huggingface.co/datasets/Similoluwa/african-multilingual-tokenizer-challenge
- Révision : `v1.0.0`
- Colonnes : ['language', 'text', 'source_id', 'source_url', 'source_config', 'source_revision', 'segment_index', 'content_sha256']
- Train : 240,000 exemples — Validation : 24,000 exemples

### Nombre d'exemples par langue

| Langue | Code | Train | Validation |
|---|---|---:|---:|
| English | en | 40,000 | 4,000 |
| French | fr | 40,000 | 4,000 |
| Hausa | ha | 40,000 | 4,000 |
| Swahili | sw | 40,000 | 4,000 |
| Yoruba | yo | 40,000 | 4,000 |
| Amharic | am | 40,000 | 4,000 |

## 2. Statistiques du dataset

| language | split | examples | words | characters | avg_words | avg_chars | distinct_unicode_chars |
|---|---|---:|---:|---:|---:|---:|---:|
| English | train | 40,000 | 872,502 | 5,429,908 | 21.81 | 135.75 | 608 |
| French | train | 40,000 | 906,116 | 5,686,404 | 22.65 | 142.16 | 954 |
| Hausa | train | 40,000 | 906,481 | 5,251,977 | 22.66 | 131.30 | 738 |
| Swahili | train | 40,000 | 694,439 | 4,376,925 | 17.36 | 109.42 | 901 |
| Yoruba | train | 40,000 | 840,923 | 4,629,899 | 21.02 | 115.75 | 1,473 |
| Amharic | train | 40,000 | 801,033 | 4,079,673 | 20.03 | 101.99 | 1,585 |
| English | validation | 4,000 | 88,469 | 545,187 | 22.12 | 136.30 | 217 |
| French | validation | 4,000 | 90,652 | 567,579 | 22.66 | 141.89 | 320 |
| Hausa | validation | 4,000 | 89,819 | 519,630 | 22.45 | 129.91 | 366 |
| Swahili | validation | 4,000 | 69,832 | 444,263 | 17.46 | 111.07 | 247 |
| Yoruba | validation | 4,000 | 85,758 | 469,153 | 21.44 | 117.29 | 365 |
| Amharic | validation | 4,000 | 79,413 | 404,303 | 19.85 | 101.08 | 735 |

## 3. Configuration du tokenizer

```python
from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.normalizers import NFC
from tokenizers.pre_tokenizers import Whitespace
from tokenizers.trainers import BpeTrainer

tokenizer = Tokenizer(BPE(unk_token="[UNK]"))
tokenizer.normalizer = NFC()
tokenizer.pre_tokenizer = Whitespace()

trainer = BpeTrainer(vocab_size=10_000, min_frequency=2, special_tokens=['[UNK]'])
```

- Entraînement : split `train` uniquement (multilingue).
- Évaluation : split `validation` uniquement.
- Définition du mot : suite maximale de caractères non-espaces (`text.split()`), identique pour les 6 langues.
- Aucune conversion ASCII / suppression d'accents / lowercase.

## 4. Vocabulaire

- Vocabulaire demandé : 10000
- Vocabulaire réel : 10000 (<= 10 000, OK)
- Tokens spéciaux : ['[UNK]']
- Tokens longueur 1 / 2 / 3 : 3,044 / 1,564 / 1,852
- Longueur moyenne / maximale : 2.9957 / 13

## 5. Résultats par langue (validation)

| Language | Words | Tokens | Fertility | UNK | UNK Rate | Score |
|---|---:|---:|---:|---:|---:|---:|
| English | 88,469 | 167,141 | 1.8893 | 5 | 0.000057 | 1.8949 |
| French | 90,652 | 180,295 | 1.9889 | 63 | 0.000695 | 2.0584 |
| Hausa | 89,819 | 154,957 | 1.7252 | 43 | 0.000479 | 1.7731 |
| Swahili | 69,832 | 133,438 | 1.9108 | 2 | 0.000029 | 1.9137 |
| Yoruba | 85,758 | 161,700 | 1.8855 | 12 | 0.000140 | 1.8995 |
| Amharic | 79,413 | 197,729 | 2.4899 | 130 | 0.001637 | 2.6536 |

## 6. Target average (ha, sw, yo, am)

| Langue | Score |
|---|---:|
| Hausa | 1.7731 |
| Swahili | 1.9137 |
| Yoruba | 1.8995 |
| Amharic | 2.6536 |
| **Target average** | **2.0600** |

## 7. English / French et guardrails

- English : score = 1.8949 (fertility = 1.8893, unk_rate = 0.000057, unk = 5)
- French : score = 2.0584 (fertility = 1.9889, unk_rate = 0.000695, unk = 63)

- English guardrail : N/A (aucun seuil officiel trouvé — non affirmé)
- French guardrail : N/A (aucun seuil officiel trouvé — non affirmé)

**Note guardrails :** aucun seuil numérique officiel English/French n'a été trouvé dans la documentation publique du challenge (fiche HF du dataset à la révision `v1.0.0` et pages web publiques, vérifié le 10/09/2026). Aucune formule de garde-fou n'est supposée : renseigner `EN_GUARDRAIL_MAX_SCORE` / `FR_GUARDRAIL_MAX_SCORE` dans le notebook pour activer le verdict PASS/FAIL.

## 8. Exemples de tokenisation (10 par langue)

### English

Original : An Oligocene (34 – 23 Mya) pollen is known for Asteraceae and Goodeniaceae, and seeds from Oligocene and Miocene (23 – 5.3 Mya) are known for Menyanthaceae and Campanulaceae respectively.

Tokens : `['An', 'Oli', 'go', 'c', 'ene', '(', '34', '–', '23', 'M', 'ya', ')', 'pol', 'len', 'is', 'known', 'for', 'As', 'ter', 'ace', 'ae', 'and', 'Good', 'eni', 'ace', 'ae', ',', 'and', 'se', 'eds', 'from', 'Oli', 'go', 'c', 'ene', 'and', 'Mi', 'oc', 'ene', '(', '23', '–', '5', '.', '3', 'M', 'ya', ')', 'are', 'known', 'for', 'Men', 'yan', 'th', 'ace', 'ae', 'and', 'C', 'amp', 'anu', 'la', 'ce', 'ae', 'respe', 'cti', 'vely', '.']`

Token IDs : `[3236, 9595, 3194, 67, 3465, 8, 5930, 1623, 4179, 45, 3057, 9, 4348, 5134, 3055, 4608, 3160, 3817, 3134, 7166, 7845, 3089, 9421, 3850, 7166, 7845, 12, 3089, 3117, 8851, 3390, 9595, 3194, 67, 3465, 3089, 3558, 3845, 3465, 8, 4179, 1623, 21, 14, 19, 45, 3057, 9, 3165, 4608, 3160, 9409, 3195, 3056, 7166, 7845, 3089, 35, 4809, 4017, 3066, 3088, 7845, 7683, 4469, 6692, 14]`

### English

Original : When the price of Angola's principal crops—coffee and sisal—jumped after the war, the Portuguese government began to reinvest some profits inside the country, initiating a series of projects to develop infrastructure.

Tokens : `['When', 'the', 'pri', 'ce', 'of', 'Angola', "'", 's', 'princip', 'al', 'cro', 'ps', '—', 'c', 'of', 'fe', 'e', 'and', 'sis', 'al', '—', 'jum', 'ped', 'after', 'the', 'war', ',', 'the', 'Portu', 'gu', 'ese', 'government', 'began', 'to', 're', 'inv', 'est', 'some', 'prof', 'its', 'insi', 'de', 'the', 'country', ',', 'initi', 'ating', 'a', 'series', 'of', 'pro', 'je', 'cts', 'to', 'de', 'velop', 'inf', 'r', 'ast', 'ru', 'cture', '.']`

Token IDs : `[8560, 3072, 3569, 3088, 3079, 9395, 7, 83, 5040, 3054, 4235, 4340, 1624, 67, 3079, 3279, 69, 3089, 4908, 3054, 1624, 6950, 5534, 4523, 3072, 3255, 12, 3072, 6869, 3163, 3687, 7197, 7382, 3071, 3067, 9390, 3149, 4349, 4896, 3618, 4449, 3065, 3072, 7944, 12, 7162, 6668, 65, 6968, 3079, 3206, 3192, 4701, 3071, 3065, 4240, 4562, 82, 3812, 3243, 4838, 14]`

### English

Original : After Gide fled with Marc to London, his wife Madeleine burned all his correspondence in retaliation– "the best part of myself," Gide later commented.

Tokens : `['After', 'Gi', 'de', 'f', 'led', 'with', 'Mar', 'c', 'to', 'London', ',', 'his', 'wi', 'fe', 'Ma', 'de', 'le', 'ine', 'bur', 'ned', 'all', 'his', 'correspond', 'ence', 'in', 're', 't', 'ali', 'ation', '–', '"', 'the', 'b', 'est', 'part', 'of', 'm', 'ys', 'elf', ',', '"', 'Gi', 'de', 'later', 'commen', 'ted', '.']`

Token IDs : `[6848, 5265, 3065, 70, 3764, 3324, 3459, 67, 3071, 5398, 12, 3308, 3203, 3279, 3169, 3065, 3064, 3196, 4703, 5724, 3479, 3308, 9839, 3421, 3046, 3067, 84, 3108, 3416, 1623, 2, 3072, 66, 3149, 4158, 3079, 77, 3490, 6191, 12, 2, 5265, 3065, 5169, 9373, 3224, 14]`

### English

Original : Excluding the Philippines, abacá was first cultivated on a large scale in Sumatra in 1925 under the Dutch, who had observed its cultivation in the Philippines for cordage since the nineteenth century, followed up by plantings in Central America in 1929 sponsored by the U.S.

Tokens : `['Ex', 'c', 'lu', 'ding', 'the', 'Philip', 'pin', 'es', ',', 'a', 'bac', 'á', 'was', 'first', 'cul', 'ti', 'va', 'ted', 'on', 'a', 'large', 'sc', 'ale', 'in', 'Su', 'ma', 'tra', 'in', '1925', 'under', 'the', 'Dut', 'ch', ',', 'who', 'had', 'obser', 'ved', 'its', 'cul', 'ti', 'vation', 'in', 'the', 'Philip', 'pin', 'es', 'for', 'cor', 'da', 'ge', 'since', 'the', 'n', 'ine', 'te', 'en', 'th', 'century', ',', 'follow', 'ed', 'up', 'by', 'pl', 'ant', 'ings', 'in', 'Central', 'America', 'in', '1929', 'sp', 'ons', 'or', 'ed', 'by', 'the', 'U', '.', 'S', '.']`

Token IDs : `[4897, 67, 3205, 3712, 3072, 7521, 3854, 3049, 12, 65, 8335, 152, 3209, 3936, 3729, 3053, 3505, 3224, 3048, 65, 5770, 6749, 3253, 3046, 3905, 3060, 3383, 3046, 9010, 4657, 3072, 8512, 3075, 12, 4106, 3836, 7972, 3920, 3618, 3729, 3053, 6802, 3046, 3072, 7521, 3854, 3049, 3160, 3419, 3059, 3146, 7225, 3072, 78, 3196, 3073, 3050, 3056, 4584, 12, 5473, 3162, 3406, 3284, 3314, 3156, 6177, 3046, 8858, 7598, 3046, 8643, 5568, 3581, 3061, 3162, 3284, 3072, 53, 14, 51, 14]`

### English

Original : Therefore, equivalently to the preceding definition, the set A contains almost all graphs if the probability that a coin-flip–generated graph with n vertices is in A tends to 1 as n tends to infinity.

Tokens : `['There', 'fore', ',', 'e', 'qui', 'val', 'ent', 'ly', 'to', 'the', 'pre', 'ce', 'ding', 'de', 'fini', 'tion', ',', 'the', 'set', 'A', 'con', 'tains', 'al', 'most', 'all', 'gra', 'ph', 's', 'if', 'the', 'pro', 'ba', 'bility', 'that', 'a', 'co', 'in', '-', 'f', 'li', 'p', '–', 'gen', 'era', 'ted', 'gra', 'ph', 'with', 'n', 'ver', 'ti', 'ces', 'is', 'in', 'A', 'ten', 'ds', 'to', '1', 'as', 'n', 'ten', 'ds', 'to', 'in', 'fin', 'ity', '.']`

Token IDs : `[7299, 4997, 12, 69, 3297, 3894, 3083, 3189, 3071, 3072, 3486, 3088, 3712, 3065, 5220, 3093, 12, 3072, 4923, 33, 3143, 5456, 3054, 4351, 3479, 3488, 3333, 83, 5633, 3072, 3206, 3077, 6487, 3365, 65, 3202, 3046, 13, 70, 3069, 80, 1623, 3539, 4098, 3224, 3488, 3333, 3324, 78, 3174, 3053, 3265, 3055, 3046, 33, 3341, 3460, 3071, 17, 3070, 78, 3341, 3460, 3071, 3046, 3326, 3823, 14]`

### English

Original : Apple was founded as Apple Computer Company on April 1, 1976, by Steve Wozniak, Steve Jobs and Ronald Wayne to develop and sell Wozniak's Apple I personal computer.

Tokens : `['Apple', 'was', 'founded', 'as', 'Apple', 'Com', 'pu', 'ter', 'Com', 'pan', 'y', 'on', 'April', '1', ',', '1976', ',', 'by', 'Ste', 've', 'Wo', 'z', 'ni', 'ak', ',', 'Ste', 've', 'J', 'ob', 's', 'and', 'R', 'on', 'ald', 'Wa', 'y', 'ne', 'to', 'de', 'velop', 'and', 's', 'ell', 'Wo', 'z', 'ni', 'ak', "'", 's', 'Apple', 'I', 'person', 'al', 'computer', '.']`

Token IDs : `[6881, 3209, 9945, 3070, 6881, 3768, 3273, 3134, 3768, 4092, 89, 3048, 6505, 17, 12, 6179, 12, 3284, 5524, 3142, 7571, 90, 3090, 4079, 12, 5524, 3142, 42, 3300, 83, 3089, 50, 3048, 7785, 3331, 89, 3113, 3071, 3065, 4240, 3089, 83, 3864, 7571, 90, 3090, 4079, 7, 83, 6881, 41, 4609, 3054, 8419, 14]`

### English

Original : An assembler program creates object code by translating combinations of mnemonics and syntax for operations and addressing modes into their numerical equivalents.

Tokens : `['An', 'as', 'semb', 'ler', 'program', 'cre', 'ates', 'ob', 'ject', 'code', 'by', 'trans', 'la', 'ting', 'com', 'bina', 'tions', 'of', 'm', 'ne', 'moni', 'cs', 'and', 'syn', 'ta', 'x', 'for', 'opera', 'tions', 'and', 'ad', 'd', 'ress', 'ing', 'mo', 'des', 'into', 'their', 'num', 'eri', 'cal', 'e', 'qui', 'val', 'ents', '.']`

Token IDs : `[3236, 3070, 4637, 4859, 6107, 4035, 7852, 3300, 6093, 7264, 3284, 4252, 3066, 4019, 3175, 7633, 3298, 3079, 77, 3113, 6651, 4264, 3089, 6625, 3058, 88, 3160, 9006, 3298, 3089, 3222, 68, 4430, 3101, 3154, 3139, 4502, 4160, 6766, 3158, 3355, 69, 3297, 3894, 4945, 14]`

### English

Original : still alive. The first novel-length alternate history in English would seem to be Castello Holford's Aristopia (1895).

Tokens : `['still', 'ali', 've', '.', 'The', 'first', 'novel', '-', 'len', 'g', 'th', 'alter', 'na', 'te', 'history', 'in', 'English', 'would', 'see', 'm', 'to', 'be', 'Cas', 'tel', 'lo', 'Hol', 'ford', "'", 's', 'Aristo', 'pia', '(', '189', '5', ').']`

Token IDs : `[8204, 3108, 3142, 14, 3198, 3936, 9832, 13, 5134, 71, 3056, 7171, 3074, 3073, 7100, 3046, 4993, 5212, 6066, 77, 3071, 3173, 6675, 4300, 3138, 6392, 6008, 7, 83, 9700, 3694, 8, 4039, 21, 3227]`

### English

Original : administration for not having consulted Russia prior to announcing its endeavours to deploy a new missile defence system in Central Europe.

Tokens : `['administ', 'ration', 'for', 'not', 'having', 'con', 'sul', 'ted', 'Russi', 'a', 'pri', 'or', 'to', 'an', 'noun', 'cing', 'its', 'ende', 'a', 'vo', 'urs', 'to', 'de', 'plo', 'y', 'a', 'new', 'mis', 'sile', 'de', 'f', 'ence', 'system', 'in', 'Central', 'Europe', '.']`

Token IDs : `[6952, 4867, 3160, 3867, 9707, 3143, 5889, 3224, 6684, 65, 3569, 3061, 3071, 3045, 9482, 7546, 3618, 4710, 65, 3431, 3354, 3071, 3065, 8166, 89, 65, 4679, 3910, 8016, 3065, 70, 3421, 6323, 3046, 8858, 4605, 14]`

### English

Original : Molder Statue Park in downtown is dedicated to the many molders who dealt with molten iron.

Tokens : `['M', 'ol', 'der', 'Sta', 'tu', 'e', 'Par', 'k', 'in', 'down', 'town', 'is', 'de', 'di', 'cated', 'to', 'the', 'many', 'm', 'old', 'ers', 'who', 'de', 'al', 't', 'with', 'mol', 'ten', 'ir', 'on', '.']`

Token IDs : `[45, 3104, 3335, 3990, 3130, 69, 3614, 75, 3046, 9005, 6959, 3055, 3065, 3084, 6412, 3071, 3072, 4790, 77, 4771, 3302, 4106, 3065, 3054, 84, 3324, 9645, 3341, 3153, 3048, 14]`

### French

Original : Elles sont contiguës avec les langues ougriennes trans-ouraliennes et les langues permiennes cis-ouraliennes, mais sont séparées des langues fenniques par les Russes, à l'ouest, et du youkaguire par le peuple turc des Yakoutes, à l'est.

Tokens : `['El', 'les', 'sont', 'con', 'ti', 'gu', 'ë', 's', 'avec', 'les', 'langues', 'ou', 'gri', 'ennes', 'trans', '-', 'our', 'ali', 'ennes', 'et', 'les', 'langues', 'per', 'mi', 'ennes', 'cis', '-', 'our', 'ali', 'ennes', ',', 'mais', 'sont', 'sé', 'par', 'ées', 'des', 'langues', 'fen', 'ni', 'ques', 'par', 'les', 'R', 'us', 'ses', ',', 'à', 'l', "'", 'ouest', ',', 'et', 'du', 'you', 'ka', 'gu', 'ire', 'par', 'le', 'peup', 'le', 'tur', 'c', 'des', 'Ya', 'k', 'ou', 'tes', ',', 'à', 'l', "'", 'est', '.']`

Token IDs : `[5312, 3132, 3598, 3143, 3053, 3163, 162, 83, 3578, 3132, 6087, 3126, 9702, 5933, 4252, 13, 7602, 3108, 5933, 3098, 3132, 6087, 3327, 3121, 5933, 5541, 13, 7602, 3108, 5933, 12, 4006, 3598, 4222, 3147, 3788, 3139, 6087, 5861, 3090, 3403, 3147, 3132, 50, 3076, 3632, 12, 151, 76, 7, 6293, 12, 3098, 3115, 9187, 3062, 3163, 3328, 3147, 3064, 7353, 3064, 3667, 67, 3139, 3839, 75, 3126, 3380, 12, 151, 76, 7, 3149, 14]`

### French

Original : Distinction entre l'empereur et le roi La taille du territoire gouverné et la diversité religieuse et ethnique des peuples gouvernés peuvent être pris en considération.

Tokens : `['D', 'ist', 'in', 'ction', 'entre', 'l', "'", 'emp', 'ere', 'ur', 'et', 'le', 'roi', 'La', 'ta', 'ille', 'du', 'territoire', 'gouver', 'né', 'et', 'la', 'di', 'versité', 'reli', 'gie', 'use', 'et', 'eth', 'ni', 'que', 'des', 'peup', 'les', 'gouver', 'né', 's', 'peuvent', 'être', 'pris', 'en', 'considé', 'ration', '.']`

Token IDs : `[36, 3237, 3046, 3398, 3984, 76, 7, 3970, 3231, 3068, 3098, 3064, 7704, 3320, 3058, 3597, 3115, 7570, 7069, 3504, 3098, 3066, 3084, 8342, 4651, 5688, 3519, 3098, 7818, 3090, 3155, 3139, 7353, 3132, 7069, 3504, 83, 8161, 4499, 4961, 3050, 6769, 4867, 14]`

### French

Original : Issu des frustrations engendrées par ce nouveau modèle de société, le fascisme rejette les droits de l'homme, le communisme, l'anarchisme, les libertés individuelles et le libéralisme politique.

Tokens : `['Is', 'su', 'des', 'f', 'rus', 'tra', 'tions', 'en', 'gen', 'd', 'ré', 'es', 'par', 'ce', 'nouveau', 'modè', 'le', 'de', 'société', ',', 'le', 'f', 'as', 'cis', 'me', 're', 'j', 'ette', 'les', 'dro', 'its', 'de', 'l', "'", 'homme', ',', 'le', 'commun', 'isme', ',', 'l', "'", 'an', 'arch', 'isme', ',', 'les', 'liber', 'tés', 'individu', 'elles', 'et', 'le', 'li', 'bé', 'r', 'alis', 'me', 'politique', '.']`

Token IDs : `[3903, 3128, 3139, 70, 5936, 3383, 3298, 3050, 3539, 68, 3161, 3049, 3147, 3088, 7855, 9372, 3064, 3065, 7325, 12, 3064, 70, 3070, 5541, 3119, 3067, 74, 4796, 3132, 4439, 3618, 3065, 76, 7, 8598, 12, 3064, 4870, 6346, 12, 76, 7, 3045, 5272, 6346, 12, 3132, 9990, 4875, 8221, 4797, 3098, 3064, 3069, 5248, 82, 3627, 3119, 6557, 14]`

### French

Original : Cette recommandation se heurte au véto de la France dominée alors par une majorité conservatrice qui pense maintenir ainsi le statut du français comme première langue diplomatique.

Tokens : `['Cette', 're', 'com', 'man', 'da', 'tion', 'se', 'he', 'ur', 'te', 'au', 'vé', 'to', 'de', 'la', 'France', 'domin', 'ée', 'alors', 'par', 'une', 'major', 'ité', 'conser', 'v', 'atri', 'ce', 'qui', 'pen', 'se', 'main', 'ten', 'ir', 'ainsi', 'le', 'sta', 'tut', 'du', 'français', 'comme', 'première', 'langue', 'di', 'plo', 'ma', 'tique', '.']`

Token IDs : `[5991, 3067, 3175, 3217, 3059, 3093, 3117, 3097, 3068, 3073, 3125, 5147, 3071, 3065, 3066, 4422, 5304, 3343, 5029, 3147, 3228, 6121, 4046, 8104, 86, 6598, 3088, 3297, 3508, 3117, 4107, 3341, 3153, 4934, 3064, 3603, 7140, 3115, 5102, 3834, 5612, 5643, 3084, 8166, 3060, 3620, 14]`

### French

Original : L'astronomie est la science de l'observation des astres, cherchant à expliquer leur origine, leur évolution, ainsi que leurs propriétés physiques et chimiques.

Tokens : `['L', "'", 'astron', 'omi', 'e', 'est', 'la', 'science', 'de', 'l', "'", 'obser', 'vation', 'des', 'ast', 'res', ',', 'cher', 'ch', 'ant', 'à', 'exp', 'li', 'quer', 'leur', 'origine', ',', 'leur', 'é', 'volution', ',', 'ainsi', 'que', 'leurs', 'propri', 'été', 's', 'physi', 'ques', 'et', 'chi', 'mi', 'ques', '.']`

Token IDs : `[44, 7, 7460, 3926, 69, 3149, 3066, 7186, 3065, 76, 7, 7972, 6802, 3139, 3812, 3186, 12, 4778, 3075, 3156, 151, 4895, 3069, 7716, 4575, 6935, 12, 4575, 160, 5739, 12, 4934, 3155, 5951, 9756, 3895, 83, 5777, 3403, 3098, 3274, 3121, 3403, 14]`

### French

Original : Thalbitzer a rapproché les Inuit et leur nom des Aïnous, une ethnie du Japon et de la Russie, et de leur nom sur le radical innu, d'autant que les mythes fondateurs des deux communautés sont très semblables.

Tokens : `['Th', 'al', 'bit', 'zer', 'a', 'rap', 'pro', 'ché', 'les', 'In', 'u', 'it', 'et', 'leur', 'nom', 'des', 'A', 'ï', 'no', 'us', ',', 'une', 'eth', 'nie', 'du', 'Japon', 'et', 'de', 'la', 'Russi', 'e', ',', 'et', 'de', 'leur', 'nom', 'sur', 'le', 'radi', 'cal', 'in', 'nu', ',', 'd', "'", 'au', 'tant', 'que', 'les', 'my', 'thes', 'fonda', 'teurs', 'des', 'deux', 'commun', 'au', 'tés', 'sont', 'très', 'semb', 'la', 'bles', '.']`

Token IDs : `[3943, 3054, 6803, 5154, 65, 5641, 3206, 7218, 3132, 3216, 85, 3114, 3098, 4575, 3533, 3139, 33, 166, 3230, 3076, 12, 3228, 7818, 7595, 3115, 7072, 3098, 3065, 3066, 6684, 69, 12, 3098, 3065, 4575, 3533, 3352, 3064, 7000, 3355, 3046, 3622, 12, 68, 7, 3125, 3759, 3155, 3132, 3954, 8771, 8475, 4493, 3139, 4128, 4870, 3125, 4875, 3598, 5310, 4637, 3066, 5525, 14]`

### French

Original : Ils permettent de transcrire la langue japonaise sans ambigüité, au contraire des kanjis.

Tokens : `['Ils', 'permet', 'tent', 'de', 'trans', 'cri', 're', 'la', 'langue', 'japona', 'ise', 'sans', 'ambi', 'g', 'ü', 'ité', ',', 'au', 'contra', 'ire', 'des', 'kan', 'j', 'is', '.']`

Token IDs : `[9525, 5291, 5976, 3065, 4252, 3568, 3067, 3066, 5643, 7270, 3521, 5479, 7329, 71, 179, 4046, 12, 3125, 7057, 3328, 3139, 3180, 74, 3055, 14]`

### French

Original : Afin d’en savoir plus sur l’accident de Rita, elles se rendent au restaurant où une serveuse du nom de Diane prend leur commande ; cela déclenche chez Rita le souvenir du nom de « Diane Selwyn ».

Tokens : `['A', 'fin', 'd', '’', 'en', 'sa', 'voir', 'plus', 'sur', 'l', '’', 'ac', 'cident', 'de', 'R', 'ita', ',', 'elles', 'se', 'ren', 'dent', 'au', 'res', 'taur', 'ant', 'où', 'une', 'ser', 've', 'use', 'du', 'nom', 'de', 'Di', 'ane', 'prend', 'leur', 'com', 'mande', ';', 'ce', 'la', 'déc', 'len', 'che', 'chez', 'R', 'ita', 'le', 'sou', 'ven', 'ir', 'du', 'nom', 'de', '«', 'Di', 'ane', 'Sel', 'w', 'yn', '».']`

Token IDs : `[33, 3326, 68, 1627, 3050, 3100, 4614, 3496, 3352, 76, 1627, 3293, 6960, 3065, 50, 3534, 12, 4797, 3117, 3364, 4090, 3125, 3186, 8989, 3156, 5034, 3228, 3489, 3142, 3519, 3115, 3533, 3065, 3807, 4126, 8934, 4575, 3175, 9087, 27, 3088, 3066, 8218, 5134, 3382, 9229, 50, 3534, 3064, 3899, 3525, 3153, 3115, 3533, 3065, 103, 3807, 4126, 7488, 87, 6914, 5491]`

### French

Original : De plus, son côté enfantin et charmeur, volontiers railleur, doublé d'un caractère torturé et mystérieux, en a fait un personnage populaire incarnant la figure du gentleman cambrioleur de la Belle Époque.

Tokens : `['De', 'plus', ',', 'son', 'cô', 'té', 'enf', 'ant', 'in', 'et', 'char', 'me', 'ur', ',', 'vol', 'on', 'ti', 'ers', 'ra', 'ille', 'ur', ',', 'dou', 'b', 'lé', 'd', "'", 'un', 'caract', 'ère', 'tor', 'tur', 'é', 'et', 'my', 'st', 'éri', 'eux', ',', 'en', 'a', 'fait', 'un', 'person', 'na', 'ge', 'popu', 'laire', 'in', 'car', 'nant', 'la', 'fi', 'gu', 're', 'du', 'gent', 'le', 'man', 'cam', 'bri', 'o', 'leur', 'de', 'la', 'B', 'elle', 'É', 'po', 'que', '.']`

Token IDs : `[3480, 3496, 12, 3210, 6956, 3232, 9567, 3156, 3046, 3098, 5176, 3119, 3068, 12, 4602, 3048, 3053, 3302, 3092, 3597, 3068, 12, 5315, 66, 3281, 68, 7, 3063, 9452, 3441, 5743, 3667, 160, 3098, 3954, 3151, 3866, 6852, 12, 3050, 65, 4478, 3063, 4609, 3074, 3146, 4700, 5956, 3046, 3705, 9281, 3066, 3110, 3163, 3067, 3115, 5690, 3064, 3217, 6793, 4591, 79, 4575, 3065, 3066, 34, 3471, 130, 3122, 3155, 14]`

### French

Original : Divers classements placent Amsterdam parmi les métropoles mondiales offrant le meilleur confort de vie, le magazine américain Forbes la positionnant à la première place en 2016 pour les jeunes adultes ; elle également désignée en 2016 comme capitale européenne de l'innovation.

Tokens : `['Di', 'vers', 'clas', 'se', 'ments', 'pla', 'cent', 'Am', 's', 'ter', 'dam', 'par', 'mi', 'les', 'mé', 'tro', 'pol', 'es', 'mon', 'di', 'ales', 'off', 'rant', 'le', 'me', 'ille', 'ur', 'con', 'fort', 'de', 'vie', ',', 'le', 'ma', 'gaz', 'ine', 'américain', 'For', 'bes', 'la', 'position', 'nant', 'à', 'la', 'première', 'place', 'en', '2016', 'pour', 'les', 'je', 'un', 'es', 'adu', 'l', 'tes', ';', 'elle', 'également', 'dé', 'sign', 'ée', 'en', '2016', 'comme', 'capitale', 'europé', 'enne', 'de', 'l', "'", 'in', 'no', 'vation', '.']`

Token IDs : `[3807, 3997, 4648, 3117, 3744, 3570, 3514, 3291, 83, 3134, 7480, 3147, 3121, 3132, 3478, 3456, 4348, 3049, 3366, 3084, 4446, 5224, 8801, 3064, 3119, 3597, 3068, 3143, 7399, 3065, 4236, 12, 3064, 3060, 7675, 3196, 9593, 4470, 5109, 3066, 5039, 9281, 151, 3066, 5612, 5247, 3050, 4429, 3370, 3132, 3192, 3063, 3049, 6474, 76, 3380, 27, 3471, 5049, 3187, 5558, 3343, 3050, 4429, 3834, 9640, 6841, 4085, 3065, 76, 7, 3046, 3230, 6802, 14]`

### Hausa

Original : ƙasar Amurka itace ta gabatar da Majalisar Dinkin Duniya, Bankin Duniya, da sauran manyan ƙungiyoyin duniya.Amurka itace kasa mafi ƙarfin tattalin arzikin duniya da siyasa da kuma al'adu.

Tokens : `['ƙasar', 'Amurka', 'itace', 'ta', 'gabatar', 'da', 'Majalisar', 'Din', 'kin', 'Duniya', ',', 'Ban', 'kin', 'Duniya', ',', 'da', 'sauran', 'manyan', 'ƙun', 'gi', 'yoyin', 'duniya', '.', 'Amurka', 'itace', 'kasa', 'mafi', 'ƙar', 'fin', 'tattalin', 'ar', 'zi', 'kin', 'duniya', 'da', 'siyasa', 'da', 'kuma', 'al', "'", 'adu', '.']`

Token IDs : `[3824, 5307, 7739, 3058, 6294, 3059, 6677, 9820, 3152, 5585, 12, 4890, 3152, 5585, 12, 3059, 5548, 5920, 9283, 3137, 4913, 4479, 14, 5307, 7739, 4181, 4902, 4692, 3326, 8148, 3047, 3179, 3152, 4479, 3059, 6148, 3059, 3212, 3054, 7, 6474, 14]`

### Hausa

Original : lang-pt|República da Guiné-Bissau lang-pt|República da Guiné-Bissau [ʁepublikɐ dɐ ɡinɛ bisaw] ), wata ƙasa ne a yammacin Afirka wanda yake rufe kilomita 36,125 (13,948 tare da kimanin mutane 1,815,698 .

Tokens : `['lan', 'g', '-', 'pt', '|', 'Re', 'pú', 'bli', 'ca', 'da', 'Gu', 'in', 'é', '-', 'B', 'is', 'sau', 'lan', 'g', '-', 'pt', '|', 'Re', 'pú', 'bli', 'ca', 'da', 'Gu', 'in', 'é', '-', 'B', 'is', 'sau', '[', 'ʁ', 'e', 'publi', 'k', 'ɐ', 'd', 'ɐ', 'ɡ', 'in', 'ɛ', 'bisa', 'w', ']', '),', 'wata', 'ƙasa', 'ne', 'a', 'yammacin', 'Afirka', 'wanda', 'yake', 'ru', 'fe', 'kilomita', '36', ',', '12', '5', '(', '13', ',', '9', '48', 'tare', 'da', 'kimanin', 'mutane', '1', ',', '8', '15', ',', '6', '98', '.']`

Token IDs : `[3345, 71, 13, 4362, 92, 3509, 8676, 3579, 3188, 3059, 3779, 3046, 160, 13, 34, 3055, 4824, 3345, 71, 13, 4362, 92, 3509, 8676, 3579, 3188, 3059, 3779, 3046, 160, 13, 34, 3055, 4824, 59, 347, 69, 3857, 75, 314, 68, 314, 327, 3046, 324, 7167, 87, 61, 3221, 4389, 5692, 3113, 65, 9450, 4364, 3484, 3720, 3243, 3279, 6650, 5516, 12, 3550, 21, 8, 3593, 12, 25, 6600, 3611, 3059, 8202, 4688, 17, 12, 24, 3422, 12, 22, 7013, 14]`

### Hausa

Original : Filin jirgin saman Félix-Houphouët-Boigny ko Filin jirgin saman Abidjan ko Filin jirgin saman Port-Bouët, shi ne babban filin jirgin sama dake birnin Abidjan, babban birnin ƙasar Côte d'Ivoire.

Tokens : `['Fil', 'in', 'jirgin', 'saman', 'F', 'éli', 'x', '-', 'H', 'ou', 'ph', 'ou', 'ë', 't', '-', 'Bo', 'ign', 'y', 'ko', 'Fil', 'in', 'jirgin', 'saman', 'Abi', 'd', 'jan', 'ko', 'Fil', 'in', 'jirgin', 'saman', 'Port', '-', 'Bou', 'ë', 't', ',', 'shi', 'ne', 'babban', 'filin', 'jirgin', 'sama', 'dake', 'birnin', 'Abi', 'd', 'jan', ',', 'babban', 'birnin', 'ƙasar', 'C', 'ô', 'te', 'd', "'", 'I', 'voire', '.']`

Token IDs : `[5753, 3046, 6425, 9992, 38, 7890, 88, 13, 40, 3126, 3333, 3126, 162, 84, 13, 3755, 4448, 89, 3135, 5753, 3046, 6425, 9992, 7686, 68, 5019, 3135, 5753, 3046, 6425, 9992, 8735, 13, 8635, 162, 84, 12, 3211, 3113, 4509, 9696, 6425, 5228, 4472, 4172, 7686, 68, 5019, 12, 4509, 4172, 3824, 35, 171, 3073, 68, 7, 41, 9007, 14]`

### Hausa

Original : Akwai fiye da 20 kananan jam'iyyun. Guinea-Bissau ne zuwa kashi takwas da yankuna lang|pt|regiões lang|pt|regiões ) da kuma wani kamfanoni masu zaman kansu.

Tokens : `['Akwai', 'fi', 'ye', 'da', '20', 'kan', 'anan', 'jam', "'", 'i', 'y', 'yun', '.', 'Guinea', '-', 'B', 'is', 'sau', 'ne', 'zuwa', 'kashi', 'takwas', 'da', 'yan', 'kuna', 'lan', 'g', '|', 'pt', '|', 're', 'gi', 'õ', 'es', 'lan', 'g', '|', 'pt', '|', 're', 'gi', 'õ', 'es', ')', 'da', 'kuma', 'wani', 'kam', 'fan', 'oni', 'masu', 'zaman', 'kansu', '.']`

Token IDs : `[9474, 3110, 3183, 3059, 3109, 3180, 4195, 5399, 7, 73, 89, 5755, 14, 7841, 13, 34, 3055, 4824, 3113, 3616, 9241, 9682, 3059, 3195, 4677, 3345, 71, 92, 4362, 92, 3067, 3137, 172, 3049, 3345, 71, 92, 4362, 92, 3067, 3137, 172, 3049, 9, 3059, 3212, 3685, 4150, 3602, 3313, 4069, 5921, 9539, 14]`

### Hausa

Original : Akiode ta kasance mamba a ƙungiyar ƙwallon kwando ta mata ta kasa ta Najeriya a wasannin Olympics na lokacin bazara na 2004 da 2006 Commonwealth Games .

Tokens : `['A', 'kio', 'de', 'ta', 'kasance', 'ma', 'mba', 'a', 'ƙungiyar', 'ƙwallon', 'kw', 'ando', 'ta', 'mata', 'ta', 'kasa', 'ta', 'Najeriya', 'a', 'wasannin', 'Olympi', 'cs', 'na', 'lokacin', 'ba', 'zara', 'na', '2004', 'da', '2006', 'Common', 'wealth', 'Gam', 'es', '.']`

Token IDs : `[33, 4021, 3065, 3058, 3868, 3060, 3415, 65, 7910, 4447, 8241, 9286, 3058, 3587, 3058, 4181, 3058, 3466, 65, 9853, 8264, 4264, 3074, 4088, 3077, 9736, 3074, 4836, 3059, 4441, 8909, 9589, 9334, 3049, 14]`

### Hausa

Original : Kashin bayan fadan da ake yawan samu a yankin yana da nasaba da sarauta da mallakar garin Tafawa Balewa.

Tokens : `['K', 'ashin', 'bayan', 'fa', 'dan', 'da', 'ake', 'yawan', 'samu', 'a', 'yankin', 'yana', 'da', 'n', 'asa', 'ba', 'da', 'sara', 'uta', 'da', 'mal', 'la', 'kar', 'garin', 'Ta', 'fa', 'wa', 'B', 'ale', 'wa', '.']`

Token IDs : `[43, 4776, 4044, 3157, 3178, 3059, 4419, 4162, 4561, 65, 4585, 3527, 3059, 78, 3353, 3077, 3059, 7129, 5591, 3059, 3977, 3066, 3177, 4793, 3476, 3157, 3052, 34, 3253, 3052, 14]`

### Hausa

Original : A daya daga cikin sanannun hare-haren sa akwai wanda yayi garkuwa da yanmatan makarantar sakandare sama da 200 a 2014.

Tokens : `['A', 'daya', 'daga', 'cikin', 'san', 'ann', 'un', 'h', 'are', '-', 'har', 'en', 'sa', 'akwai', 'wanda', 'yayi', 'gar', 'kuwa', 'da', 'yan', 'ma', 'tan', 'makarantar', 'sakandare', 'sama', 'da', '200', 'a', '2014', '.']`

Token IDs : `[33, 4462, 3322, 3295, 3267, 3402, 3063, 72, 3165, 13, 3245, 3050, 3100, 6117, 3484, 6259, 3477, 3280, 3059, 3195, 3060, 3208, 5814, 9973, 5228, 3059, 3214, 65, 4408, 14]`

### Hausa

Original : Fiye da kowane, dole ne mu tabbatar kowane memba ya san yadda za a amsa buƙatuwa na tashin hankali a rayuwar Musulmi wanda a halin yanzu yake ma'amala dashi ayanzu da yadda alumma ke martini ga Musulunci.

Tokens : `['Fi', 'ye', 'da', 'kowan', 'e', ',', 'do', 'le', 'ne', 'mu', 'tab', 'batar', 'kowan', 'e', 'memba', 'ya', 'san', 'yadda', 'za', 'a', 'am', 'sa', 'bu', 'ƙ', 'atu', 'wa', 'na', 'ta', 'shin', 'hankali', 'a', 'rayuwar', 'Musul', 'mi', 'wanda', 'a', 'hal', 'in', 'yanzu', 'yake', 'ma', "'", 'am', 'ala', 'da', 'shi', 'a', 'yanzu', 'da', 'yadda', 'al', 'umma', 'ke', 'mar', 't', 'ini', 'ga', 'Musulunci', '.']`

Token IDs : `[4327, 3183, 3059, 9480, 69, 12, 3204, 3064, 3113, 3166, 4733, 9586, 9480, 69, 9604, 3057, 3267, 6051, 3129, 65, 3080, 3100, 3150, 280, 3615, 3052, 3074, 3058, 4911, 8246, 65, 8554, 5780, 3121, 3484, 65, 4157, 3046, 5299, 3720, 3060, 7, 3080, 3278, 3059, 3211, 65, 5299, 3059, 6051, 3054, 7754, 3123, 3270, 84, 3193, 3106, 7334, 14]`

### Hausa

Original : Abubuwan daya kamata a sani game da Isyaku Rabi'u Wadannan su ne abubuwa guda bakwai da da wuya ka samu fahimtarsa: 1.

Tokens : `['Abu', 'bu', 'wan', 'daya', 'kama', 'ta', 'a', 'sani', 'game', 'da', 'Is', 'ya', 'ku', 'Ra', 'bi', "'", 'u', 'Wa', 'dan', 'nan', 'su', 'ne', 'abubu', 'wa', 'guda', 'bakwai', 'da', 'da', 'wu', 'ya', 'ka', 'samu', 'fa', 'him', 'tar', 'sa', ':', '1', '.']`

Token IDs : `[4565, 3150, 3176, 4462, 3537, 3058, 65, 6822, 5173, 3059, 3903, 3057, 3078, 3608, 3105, 7, 85, 3331, 3178, 3482, 3128, 3113, 7769, 3052, 5580, 8120, 3059, 3059, 4356, 3057, 3062, 4561, 3157, 3877, 3396, 3100, 26, 17, 14]`

### Hausa

Original : A cikin shekara ta ( 2012) ta auri Kenny Rodriguez kuma ta ci gaba da jagora a cikin shekara ta (2015) bayan haihuwar ɗanta Matthew.

Tokens : `['A', 'cikin', 'shekara', 'ta', '(', '2012', ')', 'ta', 'a', 'uri', 'Ken', 'ny', 'R', 'od', 'ri', 'gue', 'z', 'kuma', 'ta', 'ci', 'gaba', 'da', 'ja', 'g', 'ora', 'a', 'cikin', 'shekara', 'ta', '(', '2015', ')', 'bayan', 'hai', 'huwar', 'ɗan', 'ta', 'Mat', 'the', 'w', '.']`

Token IDs : `[33, 3295, 3427, 3058, 8, 4522, 9, 3058, 65, 3458, 4844, 4048, 50, 3360, 3081, 4211, 90, 3212, 3058, 3095, 4033, 3059, 3218, 71, 4385, 65, 3295, 3427, 3058, 8, 4335, 9, 4044, 3400, 7288, 4253, 3058, 5704, 3072, 87, 14]`

### Swahili

Original : Karibu yale yote tunayoyajua kuhusu maisha ya Beda yamo katika sura ya mwisho ya Historia Ecclesiastica, aliyoimaliza mwaka 731 hivi, ambapo anadokeza kuwa yuko katika mwaka wa 59 wa maisha yake, hivyo alizaliwa 672–673.

Tokens : `['K', 'ari', 'bu', 'y', 'ale', 'yote', 'tuna', 'yo', 'ya', 'jua', 'kuhusu', 'maisha', 'ya', 'Be', 'da', 'ya', 'mo', 'katika', 'sur', 'a', 'ya', 'mwisho', 'ya', 'Historia', 'E', 'c', 'cles', 'i', 'as', 'ti', 'ca', ',', 'ali', 'yo', 'im', 'ali', 'za', 'mwaka', '7', '31', 'hi', 'vi', ',', 'ambapo', 'ana', 'do', 'ke', 'za', 'kuwa', 'yu', 'ko', 'katika', 'mwaka', 'wa', '59', 'wa', 'maisha', 'yake', ',', 'hivyo', 'ali', 'zaliwa', '67', '2', '–', '67', '3', '.']`

Token IDs : `[43, 3133, 3150, 89, 3253, 6321, 6284, 3213, 3057, 9228, 7261, 8849, 3057, 4111, 3059, 3057, 3154, 3338, 3352, 65, 3057, 8315, 3057, 6067, 37, 67, 7093, 73, 3070, 3053, 3188, 12, 3108, 3213, 3623, 3108, 3129, 3356, 23, 5107, 3087, 3171, 12, 9326, 3124, 3204, 3123, 3129, 3280, 3361, 3135, 3338, 3356, 3052, 9594, 3052, 8849, 3720, 12, 5848, 3108, 3666, 7228, 18, 1623, 7228, 19, 14]`

### Swahili

Original : Akifuata masisitizo ya mababu kama Ambrosi, Augustino na Sirili wa Aleksandria, alifundisha kwamba sakramenti hazimfanyi mtu “awe Mkristo tu, bali Kristo mwenyewe”.

Tokens : `['A', 'ki', 'fuata', 'mas', 'isi', 'ti', 'zo', 'ya', 'ma', 'babu', 'kama', 'Amb', 'ro', 'si', ',', 'Aug', 'us', 'tin', 'o', 'na', 'Si', 'ri', 'li', 'wa', 'Ale', 'ks', 'and', 'ria', ',', 'ali', 'fun', 'dis', 'ha', 'kwamba', 'sa', 'k', 'ram', 'enti', 'ha', 'zi', 'm', 'fan', 'yi', 'mtu', '“', 'a', 'we', 'M', 'kristo', 'tu', ',', 'bali', 'Kristo', 'm', 'wenyewe', '”', '.']`

Token IDs : `[33, 3094, 4921, 3675, 3336, 3053, 3316, 3057, 3060, 8625, 3537, 9641, 3099, 3085, 12, 4756, 3076, 3524, 79, 3074, 3758, 3081, 3069, 3052, 8672, 4293, 3089, 4258, 12, 3108, 3520, 3442, 3096, 5667, 3100, 75, 7887, 3741, 3096, 3179, 77, 3602, 3226, 8095, 1629, 65, 3241, 45, 5231, 3130, 12, 9869, 4292, 77, 7492, 1630, 14]`

### Swahili

Original : Beda maarufu kama Mheshimiwa tangu enzi za uhai wake (Wearmouth-Jarrow, Northumbria, leo nchini Uingereza, 672 au 673 – 25 Mei - Wearmouth-Jarrow, 735) alikuwa mmonaki, padri, mwanateolojia na mwanahistoria nchini Uingereza.

Tokens : `['Be', 'da', 'ma', 'aru', 'fu', 'kama', 'M', 'h', 'eshi', 'mi', 'wa', 'tangu', 'en', 'zi', 'za', 'u', 'hai', 'wake', '(', 'W', 'ear', 'mou', 'th', '-', 'J', 'ar', 'row', ',', 'North', 'u', 'mb', 'ria', ',', 'leo', 'nchini', 'Uingereza', ',', '67', '2', 'au', '67', '3', '–', '25', 'Mei', '-', 'W', 'ear', 'mou', 'th', '-', 'J', 'ar', 'row', ',', '7', '35', ')', 'alikuwa', 'm', 'mon', 'aki', ',', 'pa', 'dri', ',', 'mwana', 'te', 'olojia', 'na', 'mwana', 'historia', 'nchini', 'Uingereza', '.']`

Token IDs : `[4111, 3059, 3060, 7043, 3257, 3537, 45, 72, 4622, 3121, 3052, 5748, 3050, 3179, 3129, 85, 3400, 4387, 8, 55, 4182, 5891, 3056, 13, 42, 3047, 9881, 12, 6094, 85, 3190, 4258, 12, 5508, 4986, 5227, 12, 7228, 18, 3125, 7228, 19, 1623, 4037, 6085, 13, 55, 4182, 5891, 3056, 13, 42, 3047, 9881, 12, 23, 5287, 9, 4097, 77, 3366, 5094, 12, 3145, 6251, 12, 5542, 3073, 7744, 3074, 5542, 6322, 4986, 5227, 14]`

### Swahili

Original : Bahari ya Kaspi (pia: Bahari ya Qazwin; kwa Kiajemi: دريا خزر "darya khazar"; kwa Kirusi: Каспийское море "kaspiiskoye more") ni ziwa kubwa kabisa duniani lenye eneo la km² 371,000 na mjao wa km³ 78,200.

Tokens : `['Bahari', 'ya', 'Kas', 'pi', '(', 'pia', ':', 'Bahari', 'ya', 'Q', 'a', 'z', 'win', ';', 'kwa', 'Ki', 'aje', 'mi', ':', 'د', 'ر', 'ي', 'ا', 'خ', 'ز', 'ر', '"', 'dar', 'ya', 'k', 'ha', 'zar', '"', ';', 'kwa', 'Kir', 'usi', ':', 'К', 'а', 'с', 'п', 'и', 'й', 'с', 'к', 'о', 'е', 'м', 'о', 'р', 'е', '"', 'kas', 'pi', 'is', 'ko', 'ye', 'more', '")', 'ni', 'ziwa', 'kubwa', 'kabisa', 'duniani', 'len', 'ye', 'eneo', 'la', 'km', '²', '37', '1', ',', '000', 'na', 'm', 'ja', 'o', 'wa', 'km', '³', '78', ',', '200', '.']`

Token IDs : `[6671, 3057, 4937, 3201, 8, 3694, 26, 6671, 3057, 49, 65, 90, 5887, 27, 3184, 3311, 8674, 3121, 26, 658, 660, 680, 650, 657, 661, 660, 2, 4115, 3057, 75, 3096, 3604, 2, 27, 3184, 6814, 3418, 26, 495, 516, 533, 531, 524, 525, 533, 526, 530, 521, 528, 530, 532, 521, 2, 4520, 3201, 3055, 3135, 3183, 4497, 6329, 3090, 9067, 3929, 8186, 7088, 5134, 3183, 4131, 3066, 4862, 110, 5517, 17, 12, 3784, 3074, 77, 3218, 79, 3052, 4862, 111, 9921, 12, 3214, 14]`

### Swahili

Original : Kwa ajili ya uimbaji na utunzi wake wa kuliwaza, Remmy anaitwa “Dokta” na ni mtu anayejulikana sana katika sehemu za Sinza ambazo ni jirani na anakoishi yeye na mkewe Mwingereza na watoto wao 5 na kasuku mmoja, nje kidogo ya jiji la Dar es Salaam.

Tokens : `['Kwa', 'ajili', 'ya', 'u', 'i', 'mba', 'ji', 'na', 'ut', 'un', 'zi', 'wake', 'wa', 'ku', 'liwa', 'za', ',', 'Re', 'm', 'my', 'ana', 'itwa', '“', 'D', 'ok', 'ta', '”', 'na', 'ni', 'mtu', 'ana', 'ye', 'julikana', 'sana', 'katika', 'sehemu', 'za', 'Sin', 'za', 'amba', 'zo', 'ni', 'jir', 'ani', 'na', 'ana', 'ko', 'ishi', 'ye', 'ye', 'na', 'm', 'ke', 'we', 'M', 'w', 'ingereza', 'na', 'wato', 'to', 'wao', '5', 'na', 'kasu', 'ku', 'mmoja', ',', 'nje', 'ki', 'dogo', 'ya', 'jiji', 'la', 'Dar', 'es', 'Salaam', '.']`

Token IDs : `[4145, 8478, 3057, 85, 73, 3415, 3136, 3074, 3321, 3063, 3179, 4387, 3052, 3078, 6292, 3129, 12, 3509, 77, 3954, 3124, 5218, 1629, 36, 3813, 3058, 1630, 3074, 3090, 8095, 3124, 3183, 7117, 4658, 3338, 4593, 3129, 6977, 3129, 3649, 3316, 3090, 5267, 3127, 3074, 3124, 3135, 3799, 3183, 3183, 3074, 77, 3123, 3241, 45, 87, 4251, 3074, 5378, 3071, 7715, 21, 3074, 5106, 3078, 9201, 12, 4639, 3094, 4879, 3057, 8087, 3066, 6019, 3049, 9298, 14]`

### Swahili

Original : Alimkuta Papa huko Canossa akapiga magoti mbele ya ngome ya Papa na kuomba msamaha.

Tokens : `['Ali', 'm', 'kuta', 'Papa', 'huko', 'Can', 'os', 'sa', 'aka', 'pi', 'ga', 'ma', 'go', 'ti', 'mbe', 'le', 'ya', 'ng', 'ome', 'ya', 'Papa', 'na', 'ku', 'om', 'ba', 'm', 'sama', 'ha', '.']`

Token IDs : `[3949, 77, 6092, 3983, 6376, 7258, 3379, 3100, 3315, 3201, 3106, 3060, 3194, 3053, 5965, 3064, 3057, 7297, 3656, 3057, 3983, 3074, 3078, 3082, 3077, 77, 5228, 3096, 14]`

### Swahili

Original : ISBN 0-19-501785-4 Roget’s II: The New Thesaurus, (Boston: Houghton Mifflin, 2003 3rd edition) ISBN 0-618-25414-5

Tokens : `['ISBN', '0', '-', '19', '-', '50', '17', '85', '-', '4', 'Ro', 'get', '’', 's', 'II', ':', 'The', 'New', 'Th', 'esa', 'ur', 'us', ',', '(', 'Bo', 'ston', ':', 'H', 'ough', 'ton', 'Mi', 'ff', 'lin', ',', '2003', '3', 'rd', 'e', 'dition', ')', 'ISBN', '0', '-', '6', '18', '-', '25', '4', '14', '-', '5']`

Token IDs : `[6552, 16, 13, 3086, 13, 4325, 3389, 8196, 13, 20, 3555, 9200, 1627, 83, 3515, 26, 3198, 3896, 3943, 5125, 3068, 3076, 12, 8, 3755, 7105, 26, 40, 4857, 3679, 3558, 3463, 3882, 12, 4762, 19, 8965, 69, 4604, 9, 6552, 16, 13, 22, 3191, 13, 4037, 20, 3522, 13, 21]`

### Swahili

Original : Makala hii inahusu mwaka 1860 BK (Baada ya Kristo). Matukio Waliozaliwa

Tokens : `['Makala', 'hii', 'inahusu', 'mwaka', '186', '0', 'BK', '(', 'Baada', 'ya', 'Kristo', ').', 'Matukio', 'Waliozaliwa']`

Token IDs : `[4312, 3912, 4336, 3356, 4728, 16, 4537, 8, 3947, 3057, 4292, 3227, 4146, 3827]`

### Swahili

Original : Alizaliwa katika Mufulira (Zambia). Akamwoa Maureen Mwanawasa katika ndoa yake ya pili akazaa naye watoto 4.

Tokens : `['Ali', 'zaliwa', 'katika', 'Mu', 'fu', 'li', 'ra', '(', 'Zam', 'bia', ').', 'A', 'kam', 'wo', 'a', 'M', 'aure', 'en', 'M', 'wana', 'wasa', 'katika', 'n', 'do', 'a', 'yake', 'ya', 'pili', 'aka', 'za', 'a', 'na', 'ye', 'wato', 'to', '4', '.']`

Token IDs : `[3949, 3666, 3338, 3641, 3257, 3069, 3092, 8, 6333, 4234, 3227, 33, 4150, 3307, 65, 45, 7084, 3050, 45, 3690, 5620, 3338, 78, 3204, 65, 3720, 3057, 7222, 3315, 3129, 65, 3074, 3183, 5378, 3071, 20, 14]`

### Swahili

Original : Alimfuata Papa Benedikto VII akafuatwa na Papa Yohane XV. Tazama pia Orodha ya Mapapa Tanbihi Viungo vya nje

Tokens : `['Alimfuata', 'Papa', 'Bene', 'dik', 'to', 'V', 'II', 'aka', 'fuatwa', 'na', 'Papa', 'Yohane', 'X', 'V', '.', 'Tazama', 'pia', 'Orodha', 'ya', 'Ma', 'papa', 'Tanbihi', 'Viungo', 'vya', 'nje']`

Token IDs : `[9486, 3983, 9386, 9960, 3071, 54, 3515, 3315, 9665, 3074, 3983, 8683, 56, 54, 14, 6303, 3694, 5674, 3057, 3169, 8190, 8054, 5062, 3841, 4639]`

### Yoruba

Original : Ó di gbajú-gbàjà ní ọdún 2015 nígbà tí Olamide pèé lórí Instagram tí ó sì gbà á wọlé sí inú ilé-iṣẹ́ agbórin-jáde rẹ̀ YBNL níbi tí Temmie ti gba ìnagijẹ ''YBNL princess''.

Tokens : `['Ó', 'di', 'gbajú', '-', 'gbà', 'jà', 'ní', 'ọdún', '2015', 'nígbà', 'tí', 'Ola', 'mi', 'de', 'pè', 'é', 'lórí', 'In', 'sta', 'gram', 'tí', 'ó', 'sì', 'gbà', 'á', 'wọ', 'lé', 'sí', 'inú', 'ilé', '-', 'iṣẹ́', 'a', 'gbó', 'rin', '-', 'jáde', 'rẹ̀', 'Y', 'BN', 'L', 'níbi', 'tí', 'Te', 'm', 'mie', 'ti', 'gba', 'ì', 'na', 'gi', 'jẹ', "''", 'Y', 'BN', 'L', 'prin', 'cess', "''", '.']`

Token IDs : `[139, 3084, 6196, 13, 3395, 4450, 3131, 3409, 4335, 4939, 3168, 7897, 3121, 3065, 4400, 160, 4549, 3216, 3603, 4903, 3168, 170, 3462, 3395, 152, 3112, 3281, 3244, 7079, 3778, 13, 3953, 65, 5482, 3276, 13, 5263, 3340, 57, 6233, 44, 5960, 3168, 4529, 77, 6007, 3053, 3344, 163, 3074, 3137, 3876, 6264, 57, 6233, 44, 4302, 4535, 6264, 14]`

### Yoruba

Original : Nígbà tí ó tàtaré bọ́ sí orílẹ̀ èdè Jámánì nílùú Hamburg lẹ́ni ọmọ ọdún méjìdínlógún, ó mú orin gẹ́gẹ́ bí iṣẹ́ ajẹ́ pẹ̀lú ìkẹ́kọ̀ọ́ gboyé nínú ìmọ̀ àṣà àti ìṣe ènìyàn.

Tokens : `['Nígbà', 'tí', 'ó', 'tà', 'tar', 'é', 'bọ́', 'sí', 'orílẹ̀', 'èdè', 'J', 'á', 'má', 'nì', 'ní', 'lù', 'ú', 'Ham', 'burg', 'lẹ́', 'ni', 'ọmọ', 'ọdún', 'méjì', 'dínlógún', ',', 'ó', 'mú', 'orin', 'gẹ́gẹ́', 'bí', 'iṣẹ́', 'a', 'jẹ́', 'pẹ̀lú', 'ì', 'kẹ́kọ̀ọ́', 'gbo', 'yé', 'nínú', 'ìmọ̀', 'àṣà', 'àti', 'ì', 'ṣe', 'ènìyàn', '.']`

Token IDs : `[8759, 3168, 170, 3670, 3396, 160, 7395, 3244, 3809, 3481, 42, 152, 3789, 3738, 3131, 4707, 177, 8006, 6360, 3991, 3090, 3625, 3409, 5906, 8380, 12, 170, 4623, 4176, 4536, 3262, 3953, 65, 3319, 4581, 163, 9131, 3548, 4309, 3633, 5215, 9598, 3330, 163, 3393, 4269, 14]`

### Yoruba

Original : Ionuț Silaghi de Oaș, Poezii oșenești: Poezii, Fotografii, Culegere de folclor din Țara Oașului (Awọn ewi, Fọtoyiya, Akopọ awọ lati Ilu Oaş), Negrești-Oaș, 2017, ISBN 978-973-0-24681-0, Gbigba CD.

Tokens : `['I', 'on', 'u', 'ț', 'Si', 'la', 'g', 'hi', 'de', 'O', 'a', 'ș', ',', 'Po', 'e', 'zi', 'i', 'o', 'ș', 'ene', 'ș', 'ti', ':', 'Po', 'e', 'zi', 'i', ',', 'Fo', 'to', 'gra', 'fi', 'i', ',', 'C', 'ule', 'g', 'ere', 'de', 'fol', 'cl', 'or', 'din', 'Ț', 'ara', 'O', 'a', 'ș', 'u', 'lui', '(', 'Awọn', 'e', 'wi', ',', 'F', 'ọ', 'to', 'yi', 'ya', ',', 'A', 'ko', 'pọ', 'a', 'wọ', 'lati', 'I', 'lu', 'O', 'a', 'ş', '),', 'Ne', 'gre', 'ș', 'ti', '-', 'O', 'a', 'ș', ',', '2017', ',', 'ISBN', '97', '8', '-', '97', '3', '-', '0', '-', '24', '68', '1', '-', '0', ',', 'G', 'bi', 'gba', 'C', 'D', '.']`

Token IDs : `[41, 3048, 85, 305, 3758, 3066, 71, 3087, 3065, 47, 65, 303, 12, 3897, 69, 3179, 73, 79, 303, 3465, 303, 3053, 26, 3897, 69, 3179, 73, 12, 4729, 3071, 3488, 3110, 73, 12, 35, 5544, 71, 3231, 3065, 5087, 5540, 3061, 3532, 304, 3111, 47, 65, 303, 85, 4305, 8, 6011, 69, 3203, 12, 38, 1552, 3071, 3226, 3057, 12, 33, 3135, 5308, 65, 3112, 3803, 41, 3205, 47, 65, 254, 3221, 3528, 4414, 303, 3053, 13, 47, 65, 303, 12, 4572, 12, 6552, 6155, 24, 13, 6155, 19, 13, 16, 13, 4283, 6673, 17, 13, 16, 12, 39, 3105, 3344, 35, 36, 14]`

### Yoruba

Original : Uchenna Kizito Okafor, ni kukuru bi Uche Okafor (8 August 1967 – 6 January 2011) lasan bi Uche Okafor (ojoibi 8 August 1967 ni Owerri) je agbaboolu-elese omo orile-ede Naijiria.

Tokens : `['U', 'chen', 'na', 'Ki', 'zi', 'to', 'O', 'ka', 'for', ',', 'ni', 'ku', 'kuru', 'bi', 'U', 'che', 'O', 'ka', 'for', '(', '8', 'August', '1967', '–', '6', 'January', '2011', ')', 'la', 'san', 'bi', 'U', 'che', 'O', 'ka', 'for', '(', 'ojoibi', '8', 'August', '1967', 'ni', 'O', 'wer', 'ri', ')', 'je', 'agba', 'bo', 'olu', '-', 'el', 'ese', 'omo', 'orile', '-', 'ede', 'Naijiria', '.']`

Token IDs : `[53, 8399, 3074, 3311, 3179, 3071, 47, 3062, 3160, 12, 3090, 3078, 8780, 3105, 53, 3382, 47, 3062, 3160, 8, 24, 5240, 6240, 1623, 22, 5840, 4412, 9, 3066, 3267, 3105, 53, 3382, 47, 3062, 3160, 8, 5971, 24, 5240, 6240, 3090, 47, 4877, 3081, 9, 3192, 6509, 3261, 3689, 13, 3103, 3687, 4045, 4244, 13, 3898, 5098, 14]`

### Yoruba

Original : Kúrùpù jẹ iṣẹlẹ ti o wọpọ ti a maa nri ninu ida marundinlogun ninu ọgọrun (15%)awọn ọmọde, ti ọjọ ori wọn jẹ oṣu mẹfa (6 months)si ọdun marun si mẹfa (5–6 years).

Tokens : `['K', 'ú', 'rù', 'pù', 'jẹ', 'iṣẹ', 'lẹ', 'ti', 'o', 'wọ', 'pọ', 'ti', 'a', 'maa', 'n', 'ri', 'ninu', 'ida', 'mar', 'un', 'din', 'lo', 'gun', 'ninu', 'ọ', 'g', 'ọ', 'run', '(', '15', '%)', 'awọn', 'ọmọ', 'de', ',', 'ti', 'ọjọ', 'ori', 'wọn', 'jẹ', 'o', 'ṣu', 'mẹ', 'fa', '(', '6', 'mon', 'ths', ')', 'si', 'ọdun', 'mar', 'un', 'si', 'mẹ', 'fa', '(', '5', '–', '6', 'years', ').']`

Token IDs : `[43, 177, 8333, 8048, 3876, 7119, 5201, 3053, 79, 3112, 5308, 3053, 65, 6767, 78, 3081, 4285, 3852, 3270, 3063, 3532, 3138, 3474, 4285, 1552, 71, 1552, 4661, 8, 3422, 8556, 3927, 3625, 3065, 12, 3053, 9902, 3219, 3141, 3876, 79, 6428, 9433, 3157, 8, 22, 3366, 7192, 9, 3085, 5012, 3270, 3063, 3085, 9433, 3157, 8, 21, 1623, 22, 5191, 3227]`

### Yoruba

Original : Prinsum-o jendarii asară Mândruleoara me-i Marie Nu mă țâi că știu strâga Mândră cu zadie scurtă Cine n-are mamă dragă

Tokens : `['Prin', 'sum', '-', 'o', 'j', 'end', 'ari', 'i', 'asar', 'ă', 'M', 'â', 'nd', 'ru', 'leo', 'ara', 'me', '-', 'i', 'Marie', 'Nu', 'm', 'ă', 'ț', 'â', 'i', 'c', 'ă', 'ș', 'ti', 'u', 'str', 'â', 'ga', 'M', 'â', 'nd', 'r', 'ă', 'cu', 'za', 'die', 's', 'cur', 't', 'ă', 'C', 'ine', 'n', '-', 'are', 'mam', 'ă', 'dra', 'g', 'ă']`

Token IDs : `[6152, 7220, 13, 79, 74, 4165, 3133, 73, 3475, 186, 45, 153, 5081, 3243, 5508, 3111, 3119, 13, 73, 8404, 7680, 77, 186, 305, 153, 73, 67, 186, 303, 3053, 85, 7996, 153, 3106, 45, 153, 5081, 82, 186, 3513, 3129, 5391, 83, 4582, 84, 186, 35, 3196, 78, 13, 3165, 7321, 186, 5615, 71, 186]`

### Yoruba

Original : Itálíà (; ) tabi Orílẹ̀-èdè Olómìnira Itálíà je orile-ede ni orile Europe. Itoka Italia

Tokens : `['It', 'á', 'lí', 'à', '(;', ')', 'tabi', 'Orílẹ̀', '-', 'èdè', 'Oló', 'mì', 'nira', 'It', 'á', 'lí', 'à', 'je', 'orile', '-', 'ede', 'ni', 'orile', 'Europe', '.', 'I', 'toka', 'Italia']`

Token IDs : `[3673, 152, 5306, 151, 7844, 9, 5666, 8249, 13, 3481, 7004, 4736, 9907, 3673, 152, 5306, 151, 3192, 4244, 13, 3898, 3090, 4244, 4605, 14, 41, 3259, 5166]`

### Yoruba

Original : Oṣòdì-Ìsọ̀lọ̀ jẹ́ Agbègbè Ìjọba Ìbílẹ̀ (LGA) kan láàrín Ìpínlẹ̀ Èkó.

Tokens : `['O', 'ṣò', 'dì', '-', 'Ì', 's', 'ọ̀', 'l', 'ọ̀', 'jẹ́', 'A', 'gbègbè', 'Ì', 'jọba', 'Ì', 'bí', 'lẹ̀', '(', 'L', 'G', 'A', ')', 'kan', 'láà', 'rín', 'Ìpínlẹ̀', 'Èkó', '.']`

Token IDs : `[47, 8640, 4237, 13, 132, 83, 3170, 76, 3170, 3319, 33, 5603, 132, 6542, 132, 3262, 3258, 8, 44, 39, 33, 9, 3180, 5702, 6183, 4440, 5852, 14]`

### Yoruba

Original : Attiéké jẹ́ ìpapánu tí a maá n ṣe látara ẹ̀gẹ́, èyí tí ó gbajúmọ̀ tó sì jẹ́ oúnjẹ àṣà orílẹ̀-èdè Côte d'Ivoire àti àwọn orílẹ̀-èdè mìíràn ní ìwọ-òrùn Áfríkà.

Tokens : `['At', 'ti', 'é', 'ké', 'jẹ́', 'ì', 'pa', 'pá', 'nu', 'tí', 'a', 'ma', 'á', 'n', 'ṣe', 'lá', 'tara', 'ẹ̀', 'gẹ́', ',', 'èyí', 'tí', 'ó', 'gbajúmọ̀', 'tó', 'sì', 'jẹ́', 'o', 'ún', 'jẹ', 'àṣà', 'orílẹ̀', '-', 'èdè', 'C', 'ô', 'te', 'd', "'", 'I', 'voire', 'àti', 'àwọn', 'orílẹ̀', '-', 'èdè', 'mìíràn', 'ní', 'ì', 'wọ', '-', 'òrùn', 'Áfríkà', '.']`

Token IDs : `[4143, 3053, 160, 4390, 3319, 163, 3145, 4988, 3622, 3168, 65, 3060, 152, 78, 3393, 3247, 4759, 3107, 3746, 12, 4711, 3168, 170, 7032, 3457, 3462, 3319, 79, 3182, 3876, 9598, 3809, 13, 3481, 35, 171, 3073, 68, 7, 41, 9007, 3330, 3266, 3809, 13, 3481, 7644, 3131, 163, 3112, 13, 6609, 7965, 14]`

### Yoruba

Original : Ní àkókò tí ọjà yí ń dàgbàsókè, ìlú Kano ti di ibi ọjà agbègbè fún àwọn ǹkan ọ̀gbìn pẹ̀lu ilé-iṣẹ́ tí wọ́n ti ńṣe àwọn iṣẹ́ bíi iṣẹ́ aṣọ híhun, aṣọ rírẹ, awọ ṣíṣe àti ìkòkò mímọ.

Tokens : `['Ní', 'àkó', 'kò', 'tí', 'ọ', 'jà', 'yí', 'ń', 'dàgbà', 'só', 'kè', ',', 'ìlú', 'Kano', 'ti', 'di', 'ibi', 'ọ', 'jà', 'agbègbè', 'fún', 'àwọn', 'ǹ', 'kan', 'ọ̀', 'gb', 'ìn', 'pẹ̀', 'lu', 'ilé', '-', 'iṣẹ́', 'tí', 'wọ́n', 'ti', 'ń', 'ṣe', 'àwọn', 'iṣẹ́', 'bíi', 'iṣẹ́', 'aṣ', 'ọ', 'h', 'í', 'hun', ',', 'aṣ', 'ọ', 'rí', 'rẹ', ',', 'a', 'wọ', 'ṣíṣe', 'àti', 'ì', 'kò', 'kò', 'mí', 'mọ', '.']`

Token IDs : `[3969, 6750, 3661, 3168, 1552, 4450, 3650, 232, 8945, 6440, 5163, 12, 3818, 5583, 3053, 3084, 3750, 1552, 4450, 6418, 3523, 3266, 302, 3180, 3170, 3120, 3363, 4233, 3205, 3778, 13, 3953, 3168, 3452, 3053, 232, 3393, 3266, 3953, 5092, 3953, 6090, 1552, 72, 164, 5561, 12, 6090, 1552, 3233, 3873, 12, 65, 3112, 9716, 3330, 163, 3661, 3661, 4287, 3446, 14]`

### Amharic

Original : የተቀበረውም በደጋ እስጢፋኖስ፣ ደጋ ደሴት፣ ጣና ሃይቅ ነው። የልጇ ዳግማዊ እያሱ ስልጣን እስኪረጋጋ ድረስ፣ ንግስት ምንትዋብ የባሏን ሞት ለብዙ ጊዜ ደብቃ እንደነበር ታሪክ ይዘግባል።ምክንያቱም ደግሞ ሀገሪቱን የመምራት ፍላጎት ስለነበራት ነው።

Tokens : `['የተ', 'ቀበ', 'ረው', 'ም', 'በ', 'ደጋ', 'እስ', 'ጢ', 'ፋ', 'ኖስ', '፣', 'ደጋ', 'ደ', 'ሴት', '፣', 'ጣ', 'ና', 'ሃይ', 'ቅ', 'ነው', '።', 'የል', 'ጇ', 'ዳግ', 'ማዊ', 'እያ', 'ሱ', 'ስ', 'ልጣን', 'እስ', 'ኪ', 'ረጋ', 'ጋ', 'ድረስ', '፣', 'ንግ', 'ስት', 'ምንት', 'ዋ', 'ብ', 'የ', 'ባ', 'ሏ', 'ን', 'ሞት', 'ለ', 'ብዙ', 'ጊዜ', 'ደብ', 'ቃ', 'እንደ', 'ነበር', 'ታሪክ', 'ይዘ', 'ግ', 'ባል', '።', 'ምክንያ', 'ቱም', 'ደግሞ', 'ሀገ', 'ሪ', 'ቱን', 'የመ', 'ም', 'ራት', 'ፍ', 'ላ', 'ጎ', 'ት', 'ስለ', 'ነበ', 'ራት', 'ነው', '።']`

Token IDs : `[3282, 7014, 4613, 1141, 1194, 6589, 3411, 1367, 1406, 6667, 1423, 6589, 1322, 5249, 1423, 1368, 1242, 5261, 1181, 3172, 1422, 9987, 1344, 8099, 5066, 6621, 1161, 1165, 6532, 3411, 1265, 9080, 1348, 4009, 1423, 3861, 3517, 9050, 1288, 1199, 1315, 1197, 1127, 1244, 5578, 1120, 3987, 3566, 3974, 1179, 3329, 3437, 4000, 6656, 1350, 3871, 1422, 5368, 5646, 3966, 6554, 1154, 4275, 3588, 1141, 4061, 1408, 1123, 1351, 1215, 3617, 3264, 4061, 3172, 1422]`

### Amharic

Original : መስህብነቱ፡- በአከባቢው ሸማግለዎች እንደምነገረው ለግርዝ ዕድሜያቸው የደረሱ ወጣት ወንዶች በእለተ ግርዝ ማልደው ፏፏቴ ይወረዱና ገላቸውን በደንብ ይታጠባሉ ፡፡ይህም ግርዝ የሚገባው በስለት ስለሆነ ተያይዘው ከምከሰት ማናቸውም በሽታና ‹‹ልክፍት››(እንድነሱ) ሁሉንም በመነጻጻት ለመታደግ ስባል ነው፡፡አሁን ከግንዛቤ መዳበርና ባዕድ አምልኮ ልየታ ደረጃ እያደገ መምጣት ጋር ቢቀርም ተጋቢ ሙሽራዋና ምዘዎቾ ከአንድ ቀን በፍት በፏፏቴ መታጠብ ግድ ነበር ይላሉ እነዚህም ተራክዎች፡፡ኮረዳዎችም እንደ ወንዶች

Tokens : `['መስ', 'ህ', 'ብ', 'ነቱ', '፡', '-', 'በአ', 'ከ', 'ባቢ', 'ው', 'ሸ', 'ማ', 'ግለ', 'ዎች', 'እንደ', 'ም', 'ነገ', 'ረው', 'ለ', 'ግር', 'ዝ', 'ዕድ', 'ሜ', 'ያ', 'ቸው', 'የ', 'ደረ', 'ሱ', 'ወጣ', 'ት', 'ወን', 'ዶች', 'በእ', 'ለ', 'ተ', 'ግር', 'ዝ', 'ማል', 'ደው', 'ፏ', 'ፏ', 'ቴ', 'ይ', 'ወረ', 'ዱ', 'ና', 'ገ', 'ላ', 'ቸውን', 'በ', 'ደን', 'ብ', 'ይታ', 'ጠ', 'ባሉ', '፡፡', 'ይህም', 'ግር', 'ዝ', 'የሚገ', 'ባ', 'ው', 'በስ', 'ለት', 'ስለሆነ', 'ተ', 'ያ', 'ይዘ', 'ው', 'ከም', 'ከሰ', 'ት', 'ማ', 'ናቸው', 'ም', 'በሽታ', 'ና', '‹', '‹', 'ል', 'ክፍ', 'ት', '›', '›', '(', 'እን', 'ድ', 'ነ', 'ሱ', ')', 'ሁሉ', 'ንም', 'በመ', 'ነጻ', 'ጻ', 'ት', 'ለመ', 'ታ', 'ደግ', 'ስ', 'ባል', 'ነው', '፡፡', 'አሁን', 'ከ', 'ግን', 'ዛ', 'ቤ', 'መ', 'ዳ', 'በር', 'ና', 'ባ', 'ዕድ', 'አም', 'ል', 'ኮ', 'ል', 'የታ', 'ደረጃ', 'እያ', 'ደ', 'ገ', 'መም', 'ጣት', 'ጋር', 'ቢ', 'ቀር', 'ም', 'ተ', 'ጋ', 'ቢ', 'ሙ', 'ሽ', 'ራ', 'ዋና', 'ም', 'ዘ', 'ዎ', 'ቾ', 'ከ', 'አንድ', 'ቀን', 'በ', 'ፍት', 'በ', 'ፏ', 'ፏ', 'ቴ', 'መ', 'ታ', 'ጠብ', 'ግድ', 'ነበር', 'ይ', 'ላሉ', 'እነዚህ', 'ም', 'ተራ', 'ክ', 'ዎች', '፡፡', 'ኮ', 'ረዳ', 'ዎች', 'ም', 'እንደ', 'ወን', 'ዶች']`

Token IDs : `[3900, 1117, 1199, 6917, 1421, 13, 3407, 1263, 4226, 1290, 1168, 1139, 8353, 3294, 3329, 1141, 3440, 4613, 1120, 5468, 1304, 9623, 1140, 1318, 3235, 1315, 3742, 1161, 5124, 1215, 4454, 5498, 7618, 1120, 1210, 5468, 1304, 6830, 6147, 1410, 1410, 1214, 1320, 4443, 1323, 1242, 1345, 1123, 4350, 1194, 5370, 1199, 5202, 1365, 6883, 3576, 5945, 5468, 1304, 4057, 1197, 1290, 5170, 3435, 8314, 1210, 1318, 6656, 1290, 9169, 6918, 1215, 1139, 3961, 1141, 8633, 1242, 1640, 1640, 1125, 3822, 1215, 1641, 1641, 8, 3164, 1327, 1239, 1161, 9, 4198, 4156, 3430, 6370, 1391, 1215, 3724, 1213, 3796, 1165, 3871, 3172, 3576, 6682, 1263, 3542, 1302, 1198, 1136, 1325, 3890, 1242, 1197, 9623, 4299, 1125, 1269, 1125, 7409, 6283, 6621, 1322, 1345, 8485, 7286, 3928, 1196, 5621, 1141, 1210, 1348, 1196, 1137, 1173, 1155, 4121, 1141, 1299, 1291, 1224, 1263, 3848, 3630, 1194, 5622, 1194, 1410, 1410, 1214, 1136, 1213, 9064, 8726, 3437, 1320, 5592, 5871, 1141, 5670, 1268, 3294, 3576, 1269, 6751, 3294, 1141, 3329, 4454, 5498]`

### Amharic

Original : አማኑኤል ካንት ( Immanuel Kant) ከ(1724-1804) የነበረ ጀርመናዊ ፈላስፋ ሲሆን በምስራቃዊ ፕሩሲያ፣ ኮይንበርግ ከተማ ተወልዶ፣ ከዕለተ ውልደቱ እስከ እለት ሞቱ ከኮይንበርግ 50 ማልይ በላይ ሳይሄድ በዛች በትወሰነች ከተማ ኑሮውን መርቷል።

Tokens : `['አማ', 'ኑ', 'ኤል', 'ካ', 'ንት', '(', 'I', 'm', 'manu', 'el', 'K', 'ant', ')', 'ከ', '(', '17', '24', '-', '180', '4', ')', 'የነበረ', 'ጀር', 'መ', 'ናዊ', 'ፈላ', 'ስፋ', 'ሲሆን', 'በም', 'ስራ', 'ቃ', 'ዊ', 'ፕ', 'ሩ', 'ሲያ', '፣', 'ኮ', 'ይን', 'በር', 'ግ', 'ከተማ', 'ተ', 'ወል', 'ዶ', '፣', 'ከ', 'ዕለተ', 'ውል', 'ደ', 'ቱ', 'እስከ', 'እ', 'ለት', 'ሞ', 'ቱ', 'ከ', 'ኮ', 'ይን', 'በር', 'ግ', '50', 'ማል', 'ይ', 'በላይ', 'ሳይ', 'ሄድ', 'በ', 'ዛ', 'ች', 'በት', 'ወሰ', 'ነ', 'ች', 'ከተማ', 'ኑ', 'ሮ', 'ውን', 'መር', 'ቷል', '።']`

Token IDs : `[6243, 1240, 4752, 1266, 7180, 8, 41, 77, 6228, 3103, 43, 3156, 9, 1263, 8, 3389, 4283, 13, 5763, 20, 9, 5566, 5016, 1136, 5083, 7212, 6022, 3688, 6757, 4578, 1179, 1287, 1416, 1153, 5104, 1423, 1269, 6096, 3890, 1350, 3722, 1210, 5924, 1328, 1423, 1263, 9315, 5959, 1322, 1211, 3786, 1260, 3435, 1142, 1211, 1263, 1269, 6096, 3890, 1350, 4325, 6830, 1320, 5010, 3719, 7950, 1194, 1302, 1223, 3436, 5426, 1239, 1223, 3722, 1240, 1158, 3589, 4101, 5970, 1422]`

### Amharic

Original : በኢትዮጵያ እና በጥሊያን መንግስት መካከል የነበረው የረጅም ዘመን ወዳጅነት ሲቀጥል፣ ጥሊያኖች ከምንሊክ ዘመን ጀምሮ አንኮብር ላይ የነበረውን የኤምባሲ ጽህፈት ቤታቸውን ወደ ቤላ አዘዋውረው ዘመናዊ ህንጻ ገንብተው አዲስ የዲፕሎማቲክግንኙነት ጀመሩ::

Tokens : `['በኢትዮጵያ', 'እና', 'በጥ', 'ሊ', 'ያን', 'መንግስት', 'መካከል', 'የነበረው', 'የ', 'ረ', 'ጅም', 'ዘመን', 'ወዳ', 'ጅ', 'ነት', 'ሲ', 'ቀጥ', 'ል', '፣', 'ጥ', 'ሊያ', 'ኖች', 'ከ', 'ምን', 'ሊክ', 'ዘመን', 'ጀምሮ', 'አን', 'ኮ', 'ብር', 'ላይ', 'የነበረ', 'ውን', 'የኤ', 'ም', 'ባ', 'ሲ', 'ጽ', 'ህ', 'ፈት', 'ቤ', 'ታቸውን', 'ወደ', 'ቤ', 'ላ', 'አ', 'ዘ', 'ዋ', 'ው', 'ረው', 'ዘመናዊ', 'ህን', 'ጻ', 'ገን', 'ብ', 'ተው', 'አዲስ', 'የ', 'ዲ', 'ፕ', 'ሎ', 'ማ', 'ቲክ', 'ግንኙ', 'ነት', 'ጀመ', 'ሩ', '::']`

Token IDs : `[4819, 3299, 8657, 1122, 3392, 6519, 5196, 7929, 1315, 1152, 9810, 3790, 7820, 1342, 3317, 1162, 5902, 1125, 1423, 1370, 5454, 4830, 1263, 3595, 6545, 3790, 4864, 3573, 1269, 4056, 3306, 5566, 3589, 6306, 1141, 1197, 1162, 1393, 1117, 7549, 1198, 7981, 3432, 1198, 1123, 1255, 1299, 1288, 1290, 4613, 7436, 6268, 1391, 4855, 1199, 4596, 5664, 1315, 1324, 1416, 1126, 1139, 8308, 9610, 3317, 3771, 1153, 9333]`

### Amharic

Original : በ1862 ያሳተመው "Notes from the Dead House"፣ እንዲሁም ከሁለት አመት በኋላ ያሳተመው "Notes from the Underground" በጣም አድናቆትን ያተረፉ የሥነ-ጽሁፍ ትርፋቶቹ ሲሆኑ በመቀጠልም "Crime and Punishment" የተሰኘውን ልብ-ወለድ ድርሰቱን በ1866፣ "The Gambler"ን በ1867፣ "The Idiot"ን በ1869፣ እንዲሁም "Demons"ን በ1872 አሳትሟል።

Tokens : `['በ', '186', '2', 'ያሳ', 'ተመ', 'ው', '"', 'Notes', 'from', 'the', 'De', 'ad', 'House', '"', '፣', 'እንዲሁም', 'ከ', 'ሁለት', 'አመት', 'በኋላ', 'ያሳ', 'ተመ', 'ው', '"', 'Notes', 'from', 'the', 'Un', 'der', 'ground', '"', 'በጣም', 'አድ', 'ና', 'ቆ', 'ትን', 'ያ', 'ተረ', 'ፉ', 'የ', 'ሥነ', '-', 'ጽ', 'ሁ', 'ፍ', 'ትር', 'ፋ', 'ቶቹ', 'ሲሆኑ', 'በመ', 'ቀ', 'ጠ', 'ልም', '"', 'C', 'ri', 'me', 'and', 'P', 'un', 'ish', 'ment', '"', 'የተሰ', 'ኘ', 'ውን', 'ልብ', '-', 'ወለ', 'ድ', 'ድር', 'ሰ', 'ቱን', 'በ', '186', '6', '፣', '"', 'The', 'G', 'amb', 'ler', '"', 'ን', 'በ', '186', '7', '፣', '"', 'The', 'I', 'dio', 't', '"', 'ን', 'በ', '186', '9', '፣', 'እንዲሁም', '"', 'De', 'mon', 's', '"', 'ን', 'በ', '187', '2', 'አ', 'ሳት', 'ሟ', 'ል', '።']`

Token IDs : `[1194, 4728, 18, 8919, 4853, 1290, 2, 8193, 3390, 3072, 3480, 3222, 7904, 2, 1423, 5011, 1263, 4851, 6939, 3753, 8919, 4853, 1290, 2, 8193, 3390, 3072, 4394, 3335, 9159, 2, 6232, 8244, 1242, 1182, 3805, 1318, 3986, 1404, 1315, 5292, 13, 1393, 1113, 1408, 3468, 1406, 8309, 9929, 3430, 1176, 1365, 5072, 2, 35, 3081, 3119, 3089, 48, 3063, 3559, 3144, 2, 7231, 1247, 3589, 6449, 13, 4743, 1327, 3686, 1160, 4275, 1194, 4728, 22, 1423, 2, 3198, 39, 6905, 4859, 2, 1244, 1194, 4728, 23, 1423, 2, 3198, 41, 4380, 84, 2, 1244, 1194, 4728, 25, 1423, 5011, 2, 3480, 3366, 83, 2, 1244, 1194, 4741, 18, 1255, 5118, 1143, 1125, 1422]`

### Amharic

Original : በአሁኑ ወቅት ካውንቲው አሜሪካ ውስጥ ከሚገኙ አውራጃዎች ሁሉ ሁለተኛ ከፍተኛ ገቢ ያላቸው ኗሪዎችን ይይዛል። ይህም ከአጎራባች አውራጃው ከላውደን ካውንቲ ቀጥሎ መሆኑ ነው።

Tokens : `['በአሁኑ', 'ወቅት', 'ካ', 'ውን', 'ቲ', 'ው', 'አሜሪካ', 'ውስጥ', 'ከሚ', 'ገኙ', 'አው', 'ራ', 'ጃ', 'ዎች', 'ሁሉ', 'ሁለተኛ', 'ከፍተኛ', 'ገ', 'ቢ', 'ያ', 'ላቸው', 'ኗ', 'ሪዎች', 'ን', 'ይ', 'ይ', 'ዛ', 'ል', '።', 'ይህም', 'ከአ', 'ጎ', 'ራ', 'ባ', 'ች', 'አው', 'ራ', 'ጃ', 'ው', 'ከ', 'ላው', 'ደን', 'ካ', 'ውን', 'ቲ', 'ቀጥሎ', 'መሆኑ', 'ነው', '።']`

Token IDs : `[8747, 5885, 1266, 3589, 1212, 1290, 6230, 3545, 5823, 6190, 4883, 1155, 1340, 3294, 4198, 8947, 5441, 1345, 1196, 1318, 4666, 1246, 6106, 1244, 1320, 1320, 1302, 1125, 1422, 5945, 5077, 1351, 1155, 1197, 1223, 4883, 1155, 1340, 1290, 1263, 8097, 5370, 1266, 3589, 1212, 9035, 7071, 3172, 1422]`

### Amharic

Original : ከ200 እስከ 1850 ዓም ድረስ የኩኔይፎርም ማንበብ ችሎታ አልኖረም፤ ከ1850 ዓም በኋላ ብቻ ሊፈታ የቻለ ነው። ደግሞ ይዩ

Tokens : `['ከ', '200', 'እስከ', '18', '50', 'ዓም', 'ድረስ', 'የ', 'ኩ', 'ኔ', 'ይ', 'ፎ', 'ር', 'ም', 'ማን', 'በብ', 'ች', 'ሎ', 'ታ', 'አል', 'ኖ', 'ረም', '፤', 'ከ', '18', '50', 'ዓም', 'በኋላ', 'ብቻ', 'ሊ', 'ፈ', 'ታ', 'የ', 'ቻ', 'ለ', 'ነው', '።', 'ደግሞ', 'ይዩ']`

Token IDs : `[1263, 3214, 3786, 3191, 4325, 4621, 4009, 1315, 1264, 1243, 1320, 1409, 1157, 1141, 4811, 4802, 1223, 1126, 1213, 3914, 1245, 6685, 1424, 1263, 3191, 4325, 4621, 3753, 4737, 1122, 1403, 1213, 1315, 1221, 1120, 3172, 1422, 3966, 8409]`

### Amharic

Original : አቤቱ፥ የሠራዊት ጌታ ሆይ፥ እነዚህ ሰባ ዓመት የተቈጣሃቸውን ኢየሩሳሌምንና የይሁዳን ከተሞች የማትምራቸው እስከ መቼ ነው ? አለ።

Tokens : `['አ', 'ቤቱ', '፥', 'የ', 'ሠ', 'ራዊት', 'ጌታ', 'ሆይ', '፥', 'እነዚህ', 'ሰባ', 'ዓመት', 'የተ', 'ቈ', 'ጣ', 'ሃ', 'ቸውን', 'ኢ', 'የሩ', 'ሳሌ', 'ምን', 'ና', 'የ', 'ይ', 'ሁ', 'ዳን', 'ከተሞች', 'የማ', 'ትም', 'ራቸው', 'እስከ', 'መ', 'ቼ', 'ነው', '?', 'አለ', '።']`

Token IDs : `[1255, 9190, 1425, 1315, 1144, 7116, 7160, 9458, 1425, 5871, 9874, 4598, 3282, 1184, 1368, 1115, 4350, 1257, 7911, 3249, 3595, 1242, 1315, 1320, 1113, 4210, 5703, 4248, 4117, 6246, 3786, 1136, 1222, 3172, 31, 4112, 1422]`

### Amharic

Original : ይልቅስ፤ መተማመኛዋን አላህን በማድረግ እሱ ራሱ ንጽህናዋን እስኪገልጽ ድረስ በጽናት ቆመች።

Tokens : `['ይል', 'ቅ', 'ስ', '፤', 'መ', 'ተ', 'ማ', 'መ', 'ኛ', 'ዋን', 'አላ', 'ህን', 'በማ', 'ድረግ', 'እ', 'ሱ', 'ራሱ', 'ን', 'ጽ', 'ህ', 'ና', 'ዋን', 'እስ', 'ኪ', 'ገል', 'ጽ', 'ድረስ', 'በ', 'ጽ', 'ናት', 'ቆ', 'መ', 'ች', '።']`

Token IDs : `[4983, 1181, 1165, 1424, 1136, 1210, 1139, 1136, 1250, 5693, 6713, 6268, 3972, 7629, 1260, 1161, 5415, 1244, 1393, 1117, 1242, 5693, 3411, 1265, 7421, 1393, 4009, 1194, 1393, 3946, 1182, 1136, 1223, 1422]`

### Amharic

Original : እጅጉን እንዴት ናችሁ፡ እኔ እግዚአብሔር ይመስገን ደህና ነኝ፡፡ እስካሁንም አለመላኬ ጠብና ድብልቅልቅ እያደረጋችሁ ባትስማሙ ነው።

Tokens : `['እጅ', 'ጉ', 'ን', 'እን', 'ዴት', 'ና', 'ችሁ', '፡', 'እኔ', 'እግዚአብሔር', 'ይመስ', 'ገን', 'ደ', 'ህ', 'ና', 'ነ', 'ኝ', '፡፡', 'እስ', 'ካ', 'ሁ', 'ንም', 'አ', 'ለመ', 'ላ', 'ኬ', 'ጠብ', 'ና', 'ድ', 'ብል', 'ቅ', 'ል', 'ቅ', 'እያ', 'ደረ', 'ጋ', 'ችሁ', 'ባት', 'ስማ', 'ሙ', 'ነው', '።']`

Token IDs : `[5422, 1346, 1244, 3164, 9023, 1242, 9020, 1421, 6927, 5501, 7285, 4855, 1322, 1117, 1242, 1239, 1252, 3576, 3411, 1266, 1113, 4156, 1255, 3724, 1123, 1267, 9064, 1242, 1327, 8119, 1181, 1125, 1181, 6621, 3742, 1348, 9020, 4763, 8622, 1137, 3172, 1422]`

## 9. Analyse des UNK

| language | text | problematic_token | unk_count |
|---|---|---|---:|
| English | After this success, Michels departed to become manager of Barcelona and was replaced by the Romanian Ștefan Kovács. | Ștefan | 1 |
| English | The Chinese abacus, also known as the suanpan (算盤/算盘, lit. | (算盤/算盘, | 4 |
| French | l'émoi par exemple. Il est possible de représenter d'autres sons à l'aide de hiraganas en utilisant des petites versions… | (ぁ, | ぃ, | ぅ, | ぇ, | ぉ). | 5 |
| French | l'ajout d'une version réduite de l'hiragana ya, yu ou yo (respectivement ゃ, ゅ ou ょ) transforme la voyelle i qui la précè… | ゃ, | ゅ | 2 |
| French | le suburitō (素振り刀 "sabre à suburi"), sabre en bois rigide et lourd, destiné à s'entraîner aux coupes dans le vide (subur… | (素振り刀 | 2 |
| French | : « bière » (du néerlandais bier), : « France », 仏国 restant littéraire, historique ou religieux (巴里山 仏国禅寺, temple zen de… | (巴里山 | 仏国禅寺, | 3 |
| French | le shinai (竹刀 "sabre de bambou"), formé par des lamelles de bambou maintenues par une gaine de cuir ; ce sabre permet de… | (竹刀 | 1 |
| Hausa | a guje mabiyansa suka dinga garzayawa domin sauraro da sa ran cewa wakar za tayi wuta.🔥 | wuta.🔥 | 1 |
| Hausa | Ədəbiyyat qəzeti – ana bugawa wata-wata Qoroskop – ana bugawa wata-wata Tumurcuq – ta yara, ana bugawa wata-wata | Ədəbiyyat | 1 |
| Hausa | Suruka : Sarauniya Jeonghyeon na ƙungiyar Papyeong Yun (21 ga Yuli 1462 - 13 Satumba 1530) (정현 왕후 윤씨) | (정현 | 왕후 | 윤씨) | 4 |
| Hausa | An: Yi Jeong, Babban Yariman Wolsan (1454 - 21 Disamba 1488) (이정 월산 대군) | (이정 | 1 |
| Hausa | Suruka : Sarauniya Jeheon na dangin Haman Yun (15 ga Yuli 1455 - 29 Agusta 1482) (제헌 왕후 윤씨) | 왕후 | 윤씨) | 3 |
| Swahili | Mto Frati (Kigiriki: Ευφράτης euphrátēs; Kiakkadi: Pu-rat-tu; Kiebrania: פְּרָת Pĕrāth; Kiaramu: ܦܪܬ Prâth; Kar.: الفرات… | ܦܪܬ | 2 |
| Yoruba | Awọn apejuwe awọn awo-orin 1999 - Noi umblăm să colindăm (awọn adarọ-ẹri Keresimesi ibile ti Ţara Oaşului) - Maria Tripo… | Ţara | 1 |
| Yoruba | tl:Titik ta:எழுத்து (இலக்கணம்) kab:Asekkil tr:Harf uk:Буква ur:حرف vec:Letera de l'alfabeto vi:Chữ cái | ta:எழுத்து | (இலக்கணம்) | 2 |
| Yoruba | Geography of Uganda Itokasi Jẹ́ọ́gráfì bíi orílẹ̀-èdè bn:উগান্ডা#ভূগোল | bn:উগান্ডা#ভূগোল | 1 |
| Yoruba | lb:Buschtaf lt:Raidė jbo:lerfu hu:Betű ml:അക്ഷരം mr:अक्षर ms:Huruf mwl:Letra mn:Үсэг nah:Machiyōtlahtōliztli nl:Letter | ml:അക്ഷരം | mn:Үсэг | 2 |
| Yoruba | Ó ti ṣe àtúnkọ orin rẹ̀ tí ó gbajúmọ̀ jù u ni ̂”Heartbeat “ pẹ̀lu Nas tí yóò si di kíkó jáde laipẹ jọjọ. | ̂”Heartbeat | 1 |
| Amharic | በነዚህ አልፋቤቶች ሁሉ እንዲሁም በጥንታዊ ኢታሊክ አልፋቤት፣ ይህ ፊደል 𐌆 (Z ወኡም /ዝ/) ሰባተኛው ነበር። | 𐌆 | 1 |
| Amharic | ዳ ዩ (ቻይንኛ፦ 大禹 «ታላቁ ዩ») በቻይና አፈ ታሪክ የጥንታዊ ቻይና ንጉሥና የሥያ ሥርወ መንግሥት መስራች ነበር። በአንዳንድ ምንጭ ዘንድ የዩ አባት ጉን ነበረ። | 大禹 | 1 |
| Amharic | locative case), Москвe/Москвѣ, Moskve/Moskvě (ጀነቲቭ ኬዝ)) ከኋለኞቹ ቅርጾች ዘመናዊው የሩስያ ስም Мосkva, Moskva መጣ, እሱም ከብዙ የስላቭ አ-ስቲም ስ… | Москвe/Москвѣ, | 1 |
| Amharic | ﻭَﺍﻟﺬَّﺍﻛِﺮِﻳﻦَ ﺍﻟﻠَّﻪَ ﻛَﺜِﻴﺮًﺍ ﻭَﺍﻟﺬَّﺍﻛِﺮَﺍﺕِ ﺃَﻋَﺪَّ ﺍﻟﻠَّﻪُ ﻟَﻬُﻢ ﻣَّﻐْﻔِﺮَﺓً ﻭَﺃَﺟْﺮًﺍ ﻋَﻈِﻴﻤًﺎ | ﻭَﺍﻟﺬَّﺍﻛِﺮِﻳﻦَ | ﺍﻟﻠَّﻪَ | ﻛَﺜِﻴﺮًﺍ | ﻭَﺍﻟﺬَّﺍﻛِﺮَﺍﺕِ | ﺃَﻋَﺪَّ | ﺍﻟﻠَّﻪُ | ﻟَﻬُﻢ | ﻣَّﻐْﻔِﺮَﺓً | ﻭَﺃَﺟْﺮًﺍ | ﻋَﻈِﻴﻤًﺎ | 23 |
| Amharic | ባይ-ዩዕ (ቻይንኛ፦ 百越) ወይም «መቶ ዩዕ» በጥንት (ቢያንስ ከ1200 ዓክልበ. በደቡብ ቻይና እና ስሜን ቬትናም የተገኙት ብሔሮች ነበሩ። ባሕል | 百越) | 2 |

A [UNK] appears when a character is absent from the BPE vocabulary (base alphabet = characters seen >= min_frequency=2 times in the whole train).

## 10. Environnement

| Package | Version |
|---|---|
| datasets | 4.8.5 |
| tokenizers | 0.23.1 |
| pandas | 2.2.3 |
| numpy | 2.1.3 |
| timestamp_utc | 2026-09-10T00:31:04Z |
| python | 3.13.15 |
