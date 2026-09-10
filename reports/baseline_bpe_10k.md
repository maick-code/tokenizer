# Baseline BPE 10K — AIMS Africa Multilingual Tokenizer Challenge

*Généré le 2026-09-10 01:00 UTC par `notebooks/01_baseline_bpe_10k.ipynb`.*

## 1. Dataset utilisé

- Nom : `Similoluwa/african-multilingual-tokenizer-challenge`
- URL : https://huggingface.co/datasets/Similoluwa/african-multilingual-tokenizer-challenge
- Révision : `v1.0.0`
- Colonnes : ['language', 'text']
- Train : 2,400 exemples — Validation : 480 exemples

### Nombre d'exemples par langue

| Langue | Code | Train | Validation |
|---|---|---:|---:|
| English | en | 400 | 80 |
| French | fr | 400 | 80 |
| Hausa | ha | 400 | 80 |
| Swahili | sw | 400 | 80 |
| Yoruba | yo | 400 | 80 |
| Amharic | am | 400 | 80 |

## 2. Statistiques du dataset

| language | split | examples | words | characters | avg_words | avg_chars | distinct_unicode_chars |
|---|---|---:|---:|---:|---:|---:|---:|
| English | train | 400 | 2,788 | 14,348 | 6.97 | 35.87 | 25 |
| French | train | 400 | 2,804 | 16,001 | 7.01 | 40.00 | 22 |
| Hausa | train | 400 | 2,783 | 13,998 | 6.96 | 34.99 | 24 |
| Swahili | train | 400 | 2,793 | 16,131 | 6.98 | 40.33 | 27 |
| Yoruba | train | 400 | 2,747 | 10,170 | 6.87 | 25.43 | 28 |
| Amharic | train | 400 | 2,844 | 11,489 | 7.11 | 28.72 | 34 |
| English | validation | 80 | 581 | 2,996 | 7.26 | 37.45 | 26 |
| French | validation | 80 | 583 | 3,300 | 7.29 | 41.25 | 23 |
| Hausa | validation | 80 | 560 | 2,785 | 7.00 | 34.81 | 25 |
| Swahili | validation | 80 | 565 | 3,289 | 7.06 | 41.11 | 28 |
| Yoruba | validation | 80 | 549 | 2,054 | 6.86 | 25.68 | 29 |
| Amharic | validation | 80 | 560 | 2,269 | 7.00 | 28.36 | 35 |

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
- Vocabulaire réel : 258 (<= 10 000, OK)
- Tokens spéciaux : ['[UNK]']
- Tokens longueur 1 / 2 / 3 : 69 / 74 / 51
- Longueur moyenne / maximale : 2.8093 / 13

## 5. Résultats par langue (validation)

| Language | Words | Tokens | Fertility | UNK | UNK Rate | Score |
|---|---:|---:|---:|---:|---:|---:|
| English | 581 | 599 | 1.0310 | 1 | 0.001721 | 1.2031 |
| French | 583 | 600 | 1.0292 | 1 | 0.001715 | 1.2007 |
| Hausa | 560 | 662 | 1.1821 | 1 | 0.001786 | 1.3607 |
| Swahili | 565 | 585 | 1.0354 | 1 | 0.001770 | 1.2124 |
| Yoruba | 549 | 567 | 1.0328 | 1 | 0.001821 | 1.2149 |
| Amharic | 560 | 573 | 1.0232 | 1 | 0.001786 | 1.2018 |

## 6. Target average (ha, sw, yo, am)

| Langue | Score |
|---|---:|
| Hausa | 1.3607 |
| Swahili | 1.2124 |
| Yoruba | 1.2149 |
| Amharic | 1.2018 |
| **Target average** | **1.2475** |

## 7. English / French et guardrails

- English : score = 1.2031 (fertility = 1.0310, unk_rate = 0.001721, unk = 1)
- French : score = 1.2007 (fertility = 1.0292, unk_rate = 0.001715, unk = 1)

- Budget guardrail = 1.068386 x 1.15 = 1.228643
- English guardrail : PASS (fertility 1.030981)
- French guardrail : PASS (fertility 1.029160)

**Guardrail officiel :** `budget = 1.15 x moyenne(fertility brute des langues notées)` ; échec si `fertility(en)` ou `fertility(fr)` dépasse ce budget (constantes officielles `CONTEXT_FERTILITY_RATIO = 1.15`, `SCORED_LANGUAGES`, `CONTEXT_LANGUAGES`).

## 8. Exemples de tokenisation (10 par langue)

### English

Original : with ☃for with for knowledge with knowledge knowledge shared?

Tokens : `['with', '[UNK]', 'for', 'with', 'for', 'knowledge', 'with', 'knowledge', 'knowledge', 'shared', '?']`

Token IDs : `[239, 0, 184, 239, 184, 255, 239, 255, 255, 232, 5]`

### English

Original : for is is with of the with on in።

Tokens : `['for', 'is', 'is', 'with', 'of', 'the', 'with', 'on', 'in', '።']`

Token IDs : `[184, 162, 162, 239, 207, 257, 239, 78, 243, 67]`

### English

Original : for to on is of knowledge።

Tokens : `['for', 'to', 'on', 'is', 'of', 'knowledge', '።']`

Token IDs : `[184, 168, 78, 162, 207, 255, 67]`

### English

Original : language the with is language with on development of።

Tokens : `['language', 'the', 'with', 'is', 'language', 'with', 'on', 'development', 'of', '።']`

Token IDs : `[226, 257, 239, 162, 226, 239, 78, 224, 207, 67]`

### English

Original : with was development of to development to with grows።

Tokens : `['with', 'was', 'development', 'of', 'to', 'development', 'to', 'with', 'grows', '።']`

Token IDs : `[239, 222, 224, 207, 168, 224, 168, 239, 240, 67]`

### English

Original : grows shared for in knowledge shared and

Tokens : `['grows', 'shared', 'for', 'in', 'knowledge', 'shared', 'and']`

Token IDs : `[240, 232, 184, 243, 255, 232, 96]`

### English

Original : is with for is on language shared with in

Tokens : `['is', 'with', 'for', 'is', 'on', 'language', 'shared', 'with', 'in']`

Token IDs : `[162, 239, 184, 162, 78, 226, 232, 239, 243]`

### English

Original : the in language shared to and!

Tokens : `['the', 'in', 'language', 'shared', 'to', 'and', '!']`

Token IDs : `[257, 243, 226, 232, 168, 96, 1]`

### English

Original : on shared of language to the and

Tokens : `['on', 'shared', 'of', 'language', 'to', 'the', 'and']`

Token IDs : `[78, 232, 207, 226, 168, 257, 96]`

### English

Original : shared is for on to grows is.

Tokens : `['shared', 'is', 'for', 'on', 'to', 'grows', 'is', '.']`

Token IDs : `[232, 162, 184, 78, 168, 240, 162, 4]`

### French

Original : grandit en édition développement et la la partagé?

Tokens : `['grandit', 'en', 'édition', 'développement', 'et', 'la', 'la', 'partagé', '?']`

Token IDs : `[190, 74, 171, 183, 175, 202, 202, 238, 5]`

### French

Original : le de langue région grandit les édition de développement!

Tokens : `['le', 'de', 'langue', 'région', 'grandit', 'les', 'édition', 'de', 'développement', '!']`

Token IDs : `[76, 73, 201, 218, 190, 176, 171, 73, 183, 1]`

### French

Original : édition la en partagé les et édition développement!

Tokens : `['édition', 'la', 'en', 'partagé', 'les', 'et', 'édition', 'développement', '!']`

Token IDs : `[171, 202, 74, 238, 176, 175, 171, 183, 1]`

### French

Original : langue développement en la grandit les région édition?

Tokens : `['langue', 'développement', 'en', 'la', 'grandit', 'les', 'région', 'édition', '?']`

Token IDs : `[201, 183, 74, 202, 190, 176, 218, 171, 5]`

### French

Original : en région les et développement édition de,

Tokens : `['en', 'région', 'les', 'et', 'développement', 'édition', 'de', ',']`

Token IDs : `[74, 218, 176, 175, 183, 171, 73, 3]`

### French

Original : en grandit développement langue de en savoir développement

Tokens : `['en', 'grandit', 'développement', 'langue', 'de', 'en', 'savoir', 'développement']`

Token IDs : `[74, 190, 183, 201, 73, 74, 188, 183]`

### French

Original : savoir des développement la région développement

Tokens : `['savoir', 'des', 'développement', 'la', 'région', 'développement']`

Token IDs : `[188, 165, 183, 202, 218, 183]`

### French

Original : et savoir région les et la

Tokens : `['et', 'savoir', 'région', 'les', 'et', 'la']`

Token IDs : `[175, 188, 218, 176, 175, 202]`

### French

Original : la grandit des région et savoir édition langue développement

Tokens : `['la', 'grandit', 'des', 'région', 'et', 'savoir', 'édition', 'langue', 'développement']`

Token IDs : `[202, 190, 165, 218, 175, 188, 171, 201, 183]`

### French

Original : région savoir région des en savoir de partagé édition

Tokens : `['région', 'savoir', 'région', 'des', 'en', 'savoir', 'de', 'partagé', 'édition']`

Token IDs : `[218, 188, 218, 165, 74, 188, 73, 238, 171]`

### Hausa

Original : ƙaruwa jami'a harshe yana najeriya da da da

Tokens : `['ƙaruwa', 'jami', "'", 'a', 'harshe', 'yana', 'najeriya', 'da', 'da', 'da']`

Token IDs : `[211, 195, 2, 6, 174, 159, 212, 177, 177, 177]`

### Hausa

Original : jami'☃a ƙaruwa an harshe shi ɗan yana najeriya najeriya

Tokens : `['jami', "'", '[UNK]', 'a', 'ƙaruwa', 'an', 'harshe', 'shi', 'ɗan', 'yana', 'najeriya', 'najeriya']`

Token IDs : `[195, 2, 0, 6, 211, 70, 174, 203, 219, 159, 212, 212]`

### Hausa

Original : ƙaruwa ƙaruwa ƙaruwa an shi ƙasa jami'a!

Tokens : `['ƙaruwa', 'ƙaruwa', 'ƙaruwa', 'an', 'shi', 'ƙasa', 'jami', "'", 'a', '!']`

Token IDs : `[211, 211, 211, 70, 203, 140, 195, 2, 6, 1]`

### Hausa

Original : jami'a yana an shi ɗan a,

Tokens : `['jami', "'", 'a', 'yana', 'an', 'shi', 'ɗan', 'a', ',']`

Token IDs : `[195, 2, 6, 159, 70, 203, 219, 6, 3]`

### Hausa

Original : jami'a shi ƙaruwa da yana

Tokens : `['jami', "'", 'a', 'shi', 'ƙaruwa', 'da', 'yana']`

Token IDs : `[195, 2, 6, 203, 211, 177, 159]`

### Hausa

Original : raba harshe shi ilimi harshe shi

Tokens : `['raba', 'harshe', 'shi', 'ilimi', 'harshe', 'shi']`

Token IDs : `[200, 174, 203, 250, 174, 203]`

### Hausa

Original : idan idan idan ƙaruwa da an ilimi

Tokens : `['idan', 'idan', 'idan', 'ƙaruwa', 'da', 'an', 'ilimi']`

Token IDs : `[167, 167, 167, 211, 177, 70, 250]`

### Hausa

Original : ɗan ƙasa ƙasa jami'a a najeriya an shi

Tokens : `['ɗan', 'ƙasa', 'ƙasa', 'jami', "'", 'a', 'a', 'najeriya', 'an', 'shi']`

Token IDs : `[219, 140, 140, 195, 2, 6, 6, 212, 70, 203]`

### Hausa

Original : shi an da an ilimi jami'a idan harshe da

Tokens : `['shi', 'an', 'da', 'an', 'ilimi', 'jami', "'", 'a', 'idan', 'harshe', 'da']`

Token IDs : `[203, 70, 177, 70, 250, 195, 2, 6, 167, 174, 177]`

### Hausa

Original : ilimi idan idan ƙaruwa najeriya da shi ɗan

Tokens : `['ilimi', 'idan', 'idan', 'ƙaruwa', 'najeriya', 'da', 'shi', 'ɗan']`

Token IDs : `[250, 167, 167, 211, 212, 177, 203, 219]`

### Swahili

Original : kubwa lugha tafiti wa na maarifa wa wa pamoja።

Tokens : `['kubwa', 'lugha', 'tafiti', 'wa', 'na', 'maarifa', 'wa', 'wa', 'pamoja', '።']`

Token IDs : `[119, 107, 141, 72, 87, 157, 72, 72, 130, 67]`

### Swahili

Original : pamoja habari hukua maendeleo habari።

Tokens : `['pamoja', 'habari', 'hukua', 'maendeleo', 'habari', '።']`

Token IDs : `[130, 123, 164, 147, 123, 67]`

### Swahili

Original : wa habari maendeleo maarifa tafiti ya።

Tokens : `['wa', 'habari', 'maendeleo', 'maarifa', 'tafiti', 'ya', '።']`

Token IDs : `[72, 123, 147, 157, 141, 88, 67]`

### Swahili

Original : ya ya pamoja hukua maarifa tafiti tafiti maarifa።

Tokens : `['ya', 'ya', 'pamoja', 'hukua', 'maarifa', 'tafiti', 'tafiti', 'maarifa', '።']`

Token IDs : `[88, 88, 130, 164, 157, 141, 141, 157, 67]`

### Swahili

Original : pamoja na maarifa tafiti pamoja chuo habari።

Tokens : `['pamoja', 'na', 'maarifa', 'tafiti', 'pamoja', 'chuo', 'habari', '።']`

Token IDs : `[130, 87, 157, 141, 130, 134, 123, 67]`

### Swahili

Original : tafiti maarifa maarifa maarifa kubwa hukua wa maendeleo

Tokens : `['tafiti', 'maarifa', 'maarifa', 'maarifa', 'kubwa', 'hukua', 'wa', 'maendeleo']`

Token IDs : `[141, 157, 157, 157, 119, 164, 72, 147]`

### Swahili

Original : tafiti pamoja na habari hukua

Tokens : `['tafiti', 'pamoja', 'na', 'habari', 'hukua']`

Token IDs : `[141, 130, 87, 123, 164]`

### Swahili

Original : wa ya hukua habari chuo chuo na ya

Tokens : `['wa', 'ya', 'hukua', 'habari', 'chuo', 'chuo', 'na', 'ya']`

Token IDs : `[72, 88, 164, 123, 134, 134, 87, 88]`

### Swahili

Original : maendeleo maendeleo na ya habari ya!

Tokens : `['maendeleo', 'maendeleo', 'na', 'ya', 'habari', 'ya', '!']`

Token IDs : `[147, 147, 87, 88, 123, 88, 1]`

### Swahili

Original : habari maendeleo pamoja pamoja pamoja maarifa maarifa wa

Tokens : `['habari', 'maendeleo', 'pamoja', 'pamoja', 'pamoja', 'maarifa', 'maarifa', 'wa']`

Token IDs : `[123, 147, 130, 130, 130, 157, 157, 72]`

### Yoruba

Original : ní ọmọ ìmọ̀ èdè pọ̀.

Tokens : `['ní', 'ọmọ', 'ìmọ̀', 'èdè', 'pọ̀', '.']`

Token IDs : `[102, 199, 221, 194, 193, 4]`

### Yoruba

Original : ọmọ pọ̀ pín ọmọ ìlú ìwé èdè èdè,

Tokens : `['ọmọ', 'pọ̀', 'pín', 'ọmọ', 'ìlú', 'ìwé', 'èdè', 'èdè', ',']`

Token IDs : `[199, 193, 214, 199, 143, 228, 194, 194, 3]`

### Yoruba

Original : ní pọ̀ tí ṣe ìmọ̀?

Tokens : `['ní', 'pọ̀', 'tí', 'ṣe', 'ìmọ̀', '?']`

Token IDs : `[102, 193, 160, 136, 221, 5]`

### Yoruba

Original : pọ̀ ṣe ìmọ̀ pín pín nígbà ìmọ̀ ṣe ọmọ።

Tokens : `['pọ̀', 'ṣe', 'ìmọ̀', 'pín', 'pín', 'nígbà', 'ìmọ̀', 'ṣe', 'ọmọ', '።']`

Token IDs : `[193, 136, 221, 214, 214, 246, 221, 136, 199, 67]`

### Yoruba

Original : ṣe ìwé ìlú pọ̀ pọ̀።

Tokens : `['ṣe', 'ìwé', 'ìlú', 'pọ̀', 'pọ̀', '።']`

Token IDs : `[136, 228, 143, 193, 193, 67]`

### Yoruba

Original : sí sí pọ̀ ṣe ṣe ní

Tokens : `['sí', 'sí', 'pọ̀', 'ṣe', 'ṣe', 'ní']`

Token IDs : `[230, 230, 193, 136, 136, 102]`

### Yoruba

Original : bá ní ìmọ̀ sí nígbà

Tokens : `['bá', 'ní', 'ìmọ̀', 'sí', 'nígbà']`

Token IDs : `[161, 102, 221, 230, 246]`

### Yoruba

Original : èdè bá ní nígbà ní sí

Tokens : `['èdè', 'bá', 'ní', 'nígbà', 'ní', 'sí']`

Token IDs : `[194, 161, 102, 246, 102, 230]`

### Yoruba

Original : ìmọ̀ èdè ìwé àti ní sí

Tokens : `['ìmọ̀', 'èdè', 'ìwé', 'àti', 'ní', 'sí']`

Token IDs : `[221, 194, 228, 245, 102, 230]`

### Yoruba

Original : sí ìmọ̀ pín sí èdè pọ̀ pọ̀

Tokens : `['sí', 'ìmọ̀', 'pín', 'sí', 'èdè', 'pọ̀', 'pọ̀']`

Token IDs : `[230, 221, 214, 230, 194, 193, 193]`

### Amharic

Original : በ ሀገር ቋንቋ ታሪክ ታሪክ ያድጋል?

Tokens : `['በ', 'ሀገር', 'ቋንቋ', 'ታሪክ', 'ታሪክ', 'ያድጋል', '?']`

Token IDs : `[50, 112, 109, 133, 133, 117, 5]`

### Amharic

Original : ጥናት በ እና ያድጋል ሲካፈል ልማት.

Tokens : `['ጥናት', 'በ', 'እና', 'ያድጋል', 'ሲካፈል', 'ልማት', '.']`

Token IDs : `[129, 50, 110, 117, 124, 114, 4]`

### Amharic

Original : እውቀት ሲካፈል ሰዎች ያድጋል እና ትምህርት በ እውቀት!

Tokens : `['እውቀት', 'ሲካፈል', 'ሰዎች', 'ያድጋል', 'እና', 'ትምህርት', 'በ', 'እውቀት', '!']`

Token IDs : `[154, 124, 137, 117, 110, 153, 50, 154, 1]`

### Amharic

Original : ያድጋል እውቀት ትምህርት ሰዎች በ?

Tokens : `['ያድጋል', 'እውቀት', 'ትምህርት', 'ሰዎች', 'በ', '?']`

Token IDs : `[117, 154, 153, 137, 50, 5]`

### Amharic

Original : ልማት ያድጋል ሲካፈል ያድጋል ጥናት ልማት ሲካፈል ልማት እውቀት!

Tokens : `['ልማት', 'ያድጋል', 'ሲካፈል', 'ያድጋል', 'ጥናት', 'ልማት', 'ሲካፈል', 'ልማት', 'እውቀት', '!']`

Token IDs : `[114, 117, 124, 117, 129, 114, 124, 114, 154, 1]`

### Amharic

Original : እውቀት ያድጋል እውቀት ሲካፈል እና ትምህርት

Tokens : `['እውቀት', 'ያድጋል', 'እውቀት', 'ሲካፈል', 'እና', 'ትምህርት']`

Token IDs : `[154, 117, 154, 124, 110, 153]`

### Amharic

Original : በ ቋንቋ ጥናት ሲካፈል ቋንቋ እውቀት ታሪክ ቋንቋ?

Tokens : `['በ', 'ቋንቋ', 'ጥናት', 'ሲካፈል', 'ቋንቋ', 'እውቀት', 'ታሪክ', 'ቋንቋ', '?']`

Token IDs : `[50, 109, 129, 124, 109, 154, 133, 109, 5]`

### Amharic

Original : ሀገር ጥናት ልማት ሰዎች ያድጋል

Tokens : `['ሀገር', 'ጥናት', 'ልማት', 'ሰዎች', 'ያድጋል']`

Token IDs : `[112, 129, 114, 137, 117]`

### Amharic

Original : ሲካፈል እውቀት ሀገር ሀገር ጥናት ያድጋል ሰዎች

Tokens : `['ሲካፈል', 'እውቀት', 'ሀገር', 'ሀገር', 'ጥናት', 'ያድጋል', 'ሰዎች']`

Token IDs : `[124, 154, 112, 112, 129, 117, 137]`

### Amharic

Original : ታሪክ ሰዎች በ ቋንቋ ታሪክ

Tokens : `['ታሪክ', 'ሰዎች', 'በ', 'ቋንቋ', 'ታሪክ']`

Token IDs : `[133, 137, 50, 109, 133]`

## 9. Analyse des UNK

| language | text | problematic_token | unk_count |
|---|---|---|---:|
| English | with ☃for with for knowledge with knowledge knowledge shared? | ☃for | 1 |
| French | grand☃it partagé savoir de de savoir | grand☃it | 1 |
| Hausa | jami'☃a ƙaruwa an harshe shi ɗan yana najeriya najeriya | jami'☃a | 1 |
| Swahili | kubwa☃ chuo habari lugha wa lugha maarifa tafiti pamoja | kubwa☃ | 1 |
| Yoruba | pọ̀ t☃í èdè àti ní ní tí | t☃í | 1 |
| Amharic | ልማት በ☃ ጥናት ሰዎች በ ቋንቋ ሲካፈል ያድጋል እና | በ☃ | 1 |

A [UNK] appears when a character is absent from the BPE vocabulary (base alphabet = characters seen >= min_frequency=2 times in the whole train).

## 10. Environnement

| Package | Version |
|---|---|
| datasets | 5.0.1 |
| tokenizers | 0.22.1 |
| pandas | 3.0.5 |
| numpy | 2.4.6 |
| timestamp_utc | 2026-09-10T01:00:26Z |
| python | 3.11.2 |
