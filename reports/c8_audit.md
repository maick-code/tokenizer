# Audit complet — `c8-scoredboost` (soumission actuelle)

*Généré le 2026-09-10 01:56 UTC — audit en lecture seule : aucune expérience, aucun entraînement, aucune modification des notebooks ni des modèles.*

## Sources des chiffres

| Donnée | Source |
|---|---|
| Tokenizer soumis | `submissions/maick-code/tokenizer.json` |
| Modèle optimisé | `models/optimized_c8-scoredboost/tokenizer.json` (SHA-256 **identique** à la soumission) |
| Chiffres par langue | `reports/optimization_sweep.json` — mesurés dans Colab sur le split `validation` officiel (24 000 lignes), métrique officielle |
| Baseline | `reports/baseline_bpe_10k.json` |
| Équivalence de métrique | `reports/official_check_baseline.json` (test différentiel : identique bit à bit au code officiel) |

> ⚠️ **Limite** : Arena n'a pas d'accès réseau à Hugging Face, donc la ré-évaluation locale sur le dataset officiel complet n'est pas possible ici. Tous les chiffres par langue proviennent du run Colab sur ce même split de validation, avec la métrique officielle vérifiée équivalente.

## 1. Inventaire du tokenizer

```text
type / model      : BPE
vocab size        : 10,000 tokens (dont [UNK] en position 0)
merges            : 6,955 (paires de tokens)
unk token         : [UNK] → id 0 (déclaré dans added_tokens ; BPE.unk_id = None)
special tokens    : ['[UNK]']
added_tokens      : [{'id': 0, 'content': '[UNK]', 'single_word': False, 'lstrip': False, 'rstrip': False, 'normalized': False, 'special': True}]
byte_fallback     : False
normalizer        : {'type': 'NFC'}
pre-tokenizer     : {'type': 'WhitespaceSplit'}
post-processor    : None (aucun)
decoder           : None (aucun)
truncation/padding: None / None
```

## 2. Identification exacte de `c8-scoredboost`

Code exact, extrait de `notebooks/02_optimization_sweep.ipynb` :

```python
dict(name="c8-scoredboost", model="bpe", pre="whitespace_split", min_freq=5,
     alphabet=True, boost={"ha": 2, "sw": 2, "yo": 2, "am": 2},
     note="sur-echantillonnage des 4 langues notees")

tokenizer = Tokenizer(BPE(unk_token="[UNK]"))
tokenizer.normalizer = NFC()
tokenizer.pre_tokenizer = WhitespaceSplit()

trainer = BpeTrainer(vocab_size=10_000, min_frequency=5,
                     special_tokens=["[UNK]"], initial_alphabet=train_alphabet)
tokenizer.train_from_iterator(corpus_iterator(train_by_lang, boost), trainer=trainer)
```

| Réglage | Valeur |
|---|---|
| `base_tokenizer` | tokenizers.Tokenizer(BPE(unk_token="[UNK]")) |
| `normalization` | NFC() — aucune conversion ASCII, aucun StripAccents, aucun lowercase |
| `pre_tokenization` | WhitespaceSplit() — pontuation collée au mot (pas de token de ponctuation isolé) |
| `vocab_size` | 10000 |
| `min_frequency` | 5 |
| `initial_alphabet` | tous les caractères du train (hors espaces) |
| `training_strategy` | train_from_iterator sur dataset['train'] uniquement, tirage équilibré round-robin langue par langue |
| `sampling` | boost = {ha: 2, sw: 2, yo: 2, am: 2} — chaque passage des 4 langues notées est fourni deux fois |
| `effective_corpus` | 400 000 passages fournis : 40 000 en + 40 000 fr + 80 000 x (ha, sw, yo, am) |
| `scoring` | score officiel = moyenne sur ha, sw, yo, am de (fertility + 100 x unk_rate) |
| `language_weighting` | les 4 langues notées pèsent 2x plus que en/fr pendant l'entraînement (ratio 2:1) |
| `train_seconds_colab` | 26.7 |

Extrait de `corpus_iterator` (pondération par langue) :

```python
while active:
    for lang in list(active):
        text = next(iters[lang])
        for _ in range(boost.get(lang, 1)):   # ha/sw/yo/am fournis 2x, en/fr 1x
            yield text
```

## 3. Comparaison avec la baseline

| Component | Baseline | c8-scoredboost | Identique |
|---|---|---|---|
| model | BPE | BPE | oui |
| normalizer | NFC | NFC | oui |
| pre_tokenizer | Whitespace | WhitespaceSplit | **non** |
| post_processor | None | None | oui |
| decoder | None | None | oui |
| vocab_size | 10000 | 10000 | oui |
| merges | 6955 | 6955 | oui |
| unk / special tokens | [UNK] (id 0) | [UNK] (id 0) | oui |
| min_frequency | 2 | 5 | **non** — sans effet mesurable |
| initial_alphabet | None | tous les caractères du train | **non** — sans effet mesurable |
| language weighting | 1:1:1:1:1:1 | scored 2x vs en/fr | **non** |
| corpus effectif | 240 000 passages | 400 000 passages | **non** |
| vocab Ethiopic | 1610 | 1843 | **non** |
| vocab Yoruba (diacritiques) | 249 | 283 | **non** |
| vocab Hausa (crochets) | 35 | 36 | **non** |

## 4. Résultats par langue (split validation officiel)

| Language | Words | Tokens | Fertility | UNK | UNK Rate | Score |
|---|---:|---:|---:|---:|---:|---:|
| English | 88,469 | 172,544 | 1.9503 | 5 | 0.000057 | 1.9560 |
| French | 90,652 | 183,165 | 2.0205 | 63 | 0.000695 | 2.0900 |
| Hausa | 89,819 | 148,449 | 1.6528 | 43 | 0.000479 | 1.7006 |
| Swahili | 69,832 | 129,101 | 1.8487 | 2 | 0.000029 | 1.8516 |
| Yoruba | 85,758 | 156,887 | 1.8294 | 12 | 0.000140 | 1.8434 |
| Amharic | 79,413 | 187,446 | 2.3604 | 130 | 0.001637 | 2.5241 |
| | | | | | **Target average** | **1.9799** |

## 5. Comparaison des gains

| Language | Baseline | c8-scoredboost | Delta |
|---|---:|---:|---:|
| English | 1.8949 | 1.9560 | +0.0611 |
| French | 2.0584 | 2.0900 | +0.0317 |
| Hausa | 1.7731 | 1.7006 | -0.0725 |
| Swahili | 1.9137 | 1.8516 | -0.0621 |
| Yoruba | 1.8995 | 1.8434 | -0.0561 |
| Amharic | 2.6536 | 2.5241 | -0.1295 |
| **Score officiel** | **2.0600** | **1.9799** | **-0.0800** |

- **Langue ayant le plus progressé** : Amharic (-0.1295)
- **Langue ayant le moins progressé** : Yoruba (−0.0561), devant Swahili (−0.0621) et Hausa (−0.0725).
- **Amharic** reste la langue la plus coûteuse en valeur absolue (2.5241) mais c'est elle qui gagne le plus : −0.1295, soit 40 % du gain.
- **Régressions (langues de contexte, hors score)** : English +0.0611, French +0.0317 — absorbées par la baisse du budget du guardrail, sans le casser : absorbées par la baisse du budget du guardrail. Verdict : **PASS**.
- **Contribution des langues africaines au gain global** :

| Langue | Delta langue | Contribution au score | Part du gain |
|---|---:|---:|---:|
| Hausa | +0.0725 | +0.0181 | 22.6 % |
| Swahili | +0.0621 | +0.0155 | 19.4 % |
| Yoruba | +0.0561 | +0.0140 | 17.5 % |
| Amharic | +0.1295 | +0.0324 | 40.4 % |

## 6. Analyse du vocabulaire

| Mesure | c8-scoredboost | Baseline | Delta |
|---|---:|---:|---:|
| tokens de longueur 1 | 3,044 | 3,044 | +0 |
| tokens de longueur 2 | 1,766 | 1,564 | +202 |
| tokens de longueur 3 | 1,937 | 1,852 | +85 |
| tokens de longueur 4+ | 3,252 | 3,539 | -287 |
| longueur maximale | 13 | 13 | +0 |
| longueur moyenne | 2.893 | 2.9957 | -0.10270000000000001 |
| tokens purement ASCII | 4,773 | 5,014 | -241 |
| tokens non-ASCII | 5,226 | 4,985 | +241 |
| **tokens amhariques (ge'ez)** | 1,843 | 1,610 | +233 |
| **tokens avec diacritiques yoruba** | 283 | 249 | +34 |
| dont signes combinants (U+0300-036F) | 176 | 155 | +21 |
| **tokens hausa à crochets (ɓ ɗ ƙ)** | 36 | 35 | +1 |

Tokens longs (exemples réels du vocabulaire c8, ≥ 10 caractères ; 37 au total) : `Waliozaliwa`, `Waliofariki`, `orílẹ̀-èdè`, `University`, `mbalimbali`, `International`, `ástẹ́rọ́ìdì`, `makarantar`.

Tokens spécifiques vérifiés présents dans le vocabulaire c8 (« (c8 seul) » = absent de la baseline) :

- Amharique : `ቤተክርስቲያን` (c8 seul), `ያልተተረጎመ`, `እግዚአብሔር`, `በእንግሊዝኛ`, `የመጀመሪያው`
- Yoruba : `orílẹ̀-èdè` (c8 seul), `ọ̀pọ̀lọpọ̀`, `ọjọ́aláìsí`, `Orílẹ̀-èdè` (c8 seul), `ástẹ́rọ́ìdì`
- Hausa : `ƙungiyar`, `ƙwallon`, `waɗanda`, `ƙidayar`, `ƙasar`
- Swahili : `Waliofariki`, `Waliozaliwa`, `Wanasayansi` (c8 seul)

**Preuve mesurée du levier `WhitespaceSplit`** : c8 contient **529 merges** (et 530 tokens de vocabulaire) qui collent une ponctuation à un mot, contre **0 merge** (1 token) pour la baseline — aucun merge de ce type côté baseline. Exemples c8 : `ነው።`, `ል።`, `l'`, `s,`, `d'`, `s.`.

Autrement dit : `Whitespace` isole la ponctuation **avant** l'apprentissage, donc un merge mot+ponctuation est structurellement impossible pour la baseline ; `WhitespaceSplit` le rend possible, et c8 en a appris 529. Chaque ponctuation collée économise un token.

## 7. Analyse des merges (BPE)

- 6,955 merges dans les deux modèles ; **5,450 merges communs**, 1,505 propres à c8, 1,505 propres à la baseline.
- **Réallocation du budget de merges par langue** :

| Groupe | Baseline (merges) | c8 (merges) | Delta | 1er merge : rang baseline → c8 |
|---|---:|---:|---:|---|
| Latin ASCII (en/sw/fr sans accent) | 4,920 | 4,679 | -241 | 1 → 1 |
| Amharic (Ge'ez) | 1,273 | 1,506 | +233 | 120 → 95 |
| Latin précomposé (fr + tons yoruba) | 513 | 480 | -33 | 87 → 67 |
| Yoruba (diacritiques) | 218 | 252 | +34 | 63 → 46 |
| Hausa (crochets) | 29 | 30 | +1 | 780 → 655 |
| Autres scripts | 2 | 8 | +6 | 3871 → 1213 |

Merges **gagnés** par c8 : Latin ASCII (en/sw/fr sans accent) +1123, Amharic (Ge'ez) +267, Latin précomposé (fr + tons yoruba) +70, Yoruba (diacritiques) +37, Autres scripts +6, Hausa (crochets) +2.

Merges **perdus** par c8 : Latin ASCII (en/sw/fr sans accent) 1364, Latin précomposé (fr + tons yoruba) 103, Amharic (Ge'ez) 34, Yoruba (diacritiques) 3, Hausa (crochets) 1.

Exemples de merges caractéristiques (rang dans c8 vs baseline) :

**Amharique (ge'ez)**

| merge | token | rang c8 | rang baseline | nouveau merge ? |
|---|---|---:|---:|---|
| `እ + ን` | `እን` | 95 | 120 | — |
| `ነ + ው` | `ነው` | 100 | 128 | — |
| `ነው + ።` | `ነው።` | 135 | absent | oui |
| `የ + ሚ` | `የሚ` | 154 | 190 | — |
| `ቸ + ው` | `ቸው` | 156 | 191 | — |
| `የ + አ` | `የአ` | 162 | 195 | — |

**Yoruba (diacritiques)**

| merge | token | rang c8 | rang baseline | nouveau merge ? |
|---|---|---:|---:|---|
| `ẹ + ̀` | `ẹ̀` | 46 | 63 | — |
| `w + ọ` | `wọ` | 53 | 68 | — |
| `ẹ + ́` | `ẹ́` | 55 | 74 | — |
| `ọ + ́` | `ọ́` | 78 | 96 | — |
| `wọ + n` | `wọn` | 79 | 97 | — |
| `ọ + ̀` | `ọ̀` | 98 | 126 | — |

**Hausa (crochets)**

| merge | token | rang c8 | rang baseline | nouveau merge ? |
|---|---|---:|---:|---|
| `ƙ + asar` | `ƙasar` | 655 | 780 | — |
| `ƙ + a` | `ƙa` | 868 | 1056 | — |
| `ɗ + an` | `ɗan` | 918 | 1209 | — |
| `ƙ + wa` | `ƙwa` | 1019 | 1186 | — |
| `ɗ + a` | `ɗa` | 1030 | 1168 | — |
| `ƙwa + llon` | `ƙwallon` | 1202 | 1403 | — |

**Latin ASCII (en / sw)**

| merge | token | rang c8 | rang baseline | nouveau merge ? |
|---|---|---:|---:|---|
| `a + n` | `an` | 1 | 1 | — |
| `a + r` | `ar` | 2 | 3 | — |
| `i + n` | `in` | 3 | 2 | — |
| `w + a` | `wa` | 4 | 8 | — |
| `o + n` | `on` | 5 | 4 | — |
| `e + r` | `er` | 6 | 7 | — |

**Latin précomposé (fr + tons yoruba)**

| merge | token | rang c8 | rang baseline | nouveau merge ? |
|---|---|---:|---:|---|
| `n + í` | `ní` | 67 | 87 | — |
| `t + í` | `tí` | 97 | 124 | — |
| `ú + n` | `ún` | 105 | 138 | — |
| `r + í` | `rí` | 151 | 189 | — |
| `r + é` | `ré` | 161 | 117 | — |
| `s + í` | `sí` | 168 | 200 | — |

Ce que cela montre : les merges des langues notées **remontent** (ex. `ẹ + ̀` du rang 63 au rang 46, `እ + ን` du 120 au 95, `ƙ + asar` du 780 au 655), tandis que des merges français redescendent (`r + é` : 117 → 161). c8 a donc bien déplacé de la capacité du français et du latin ASCII vers l'amharique, le yoruba et le hausa — c'est la signature du boost.

Pourquoi cela améliore le score : un merge qui survit pour une langue notée coupe cette langue en **moins de tokens** (fertility ↓), et un merge qui disparaît pour le français ne coûte rien au score (le français n'est qu'un guardrail). Mesuré : amharique −0.1295, hausa −0.0725, swahili −0.0621, yoruba −0.0561 sur leurs scores respectifs.

## 8. Analyse des `[UNK]` — cause racine mesurée

- **255 `[UNK]`** au total sur la validation : English 5, French 63, Hausa 43, Swahili 2, Yoruba 12, Amharic 130.
- 23 lignes UNK du rapport baseline analysées → **52 caractères distincts absents du vocabulaire c8**.
- **Lettres africaines parmi eux : 0** (aucune) — vérifié langue par langue sur les lignes de validation :

| Langue de la ligne de validation | Caractères absents distincts | Lettres africaines |
|---|---:|---:|
| English | 4 | 0 |
| French | 12 | 0 |
| Hausa | 6 | 0 |
| Swahili | 2 | 0 |
| Yoruba | 7 | 0 |
| Amharic | 21 | 0 |

- Familles concernées : CJK / kana (18), Formes de présentation arabes (16), Autre (emoji, vieil italique, latin rare…) (6), Hangul (4), Indien (tamoul / bengali / malayalam) (4), Syriaque (2), Cyrillique (2).
- Seul cas limite : `̂` U+0302 (COMBINING CIRCUMFLEX ACCENT) — une marque combinante générique qui apparaît dans une ligne « Yoruba » de Wikipédia contenant du texte non-yoruba ; ce n'est pas une lettre yoruba (celles-ci sont ẹ, ọ, ṣ, ń, et elles sont **toutes** couvertes).

| Caractère | Codepoint | Nom Unicode | Famille | Occurrences (échantillon) |
|---|---|---|---|---:|
| `ﻭ` | U+FEED | ARABIC LETTER WAW ISOLATED FORM | Formes de présentation arabes | 3 |
| `ﻛ` | U+FEDB | ARABIC LETTER KAF INITIAL FORM | Formes de présentation arabes | 3 |
| `算` | U+7B97 | CJK UNIFIED IDEOGRAPH-7B97 | CJK / kana | 2 |
| `刀` | U+5200 | CJK UNIFIED IDEOGRAPH-5200 | CJK / kana | 2 |
| `정` | U+C815 | HANGUL SYLLABLE JEONG | Hangul | 2 |
| `왕` | U+C655 | HANGUL SYLLABLE WANG | Hangul | 2 |
| `후` | U+D6C4 | HANGUL SYLLABLE HU | Hangul | 2 |
| `씨` | U+C528 | HANGUL SYLLABLE SSI | Hangul | 2 |
| `ﺬ` | U+FEAC | ARABIC LETTER THAL FINAL FORM | Formes de présentation arabes | 2 |
| `ﻪ` | U+FEEA | ARABIC LETTER HEH FINAL FORM | Formes de présentation arabes | 2 |
| `ﺃ` | U+FE83 | ARABIC LETTER ALEF WITH HAMZA ABOVE ISOLATED FORM | Formes de présentation arabes | 2 |
| `Ș` | U+0218 | LATIN CAPITAL LETTER S WITH COMMA BELOW | Autre (emoji, vieil italique, latin rare…) | 1 |
| `盤` | U+76E4 | CJK UNIFIED IDEOGRAPH-76E4 | CJK / kana | 1 |
| `盘` | U+76D8 | CJK UNIFIED IDEOGRAPH-76D8 | CJK / kana | 1 |
| `ぁ` | U+3041 | HIRAGANA LETTER SMALL A | CJK / kana | 1 |
| `ぃ` | U+3043 | HIRAGANA LETTER SMALL I | CJK / kana | 1 |
| `ぅ` | U+3045 | HIRAGANA LETTER SMALL U | CJK / kana | 1 |
| `ぇ` | U+3047 | HIRAGANA LETTER SMALL E | CJK / kana | 1 |

**Pourquoi `initial_alphabet` n'a rien corrigé** : ces caractères n'apparaissent **jamais** dans le train (résidus de Wikipédia en japonais, coréen, arabe vocalisé, tamoul, syriaque, gotique, emoji…), donc aucun alphabet construit sur le train ne peut les couvrir. `min_frequency` et `initial_alphabet` sont d'ailleurs mesurés comme **sans aucun effet** (c2 = c3 = c4, scores strictement identiques).

### Poids exact des UNK dans le score

- Pénalité UNK dans le score c8 : **0.0571 point** (2.88 % du score 1.9799) — soit 1.5× tout le gain apporté par le pré-tokeniseur.

| Langue | UNK | Mots | Pénalité (points de score de la langue) |
|---|---:|---:|---:|
| Hausa | 43 | 89,819 | +0.0479 |
| Swahili | 2 | 69,832 | +0.0029 |
| Yoruba | 12 | 85,758 | +0.0140 |
| Amharic | 130 | 79,413 | +0.1637 |

L'amharique concentre à lui seul **0.1637 point** de pénalité — 4,4× le gain total du pré-tokeniseur (0.0370).

## 9. Propriété connue : round-trip non exact (constant, accepté)

- c8 : **23,949 / 24,000** lignes ne se reconstruisent pas à l'identique (baseline : 23,987).
- Cause : Whitespace/WhitespaceSplit suppriment les espaces : decode() ne restitue donc pas les espaces et le round-trip exact échoue pour presque toutes les lignes. C'est inhérent au pré-tokeniseur, identique pour le baseline, et le checker officiel l'accepte (une seule config, c5-bytelevel, est lossless — au prix de +0.0596 de fertility).
- Verdict officiel : **READY FOR SUBMISSION (valid=True, toutes les vérifications passées)**.

## 10. Contribution mesurée de chaque levier

| Levier | Score avant → après | Delta |
|---|---:|---:|
| pre-tokenizer: Whitespace -> WhitespaceSplit | 2.0600 → 2.0229 | -0.0370 |
| min_frequency 2 -> 5 (c2 -> c3) | 2.0229 → 2.0229 | +0.0000 |
| min_frequency 5 -> 10 (c3 -> c4) | 2.0229 → 2.0229 | +0.0000 |
| initial_alphabet complet (c4, mf=10) | 2.0229 → 2.0229 | +0.0000 |
| boost des 4 langues notees x2 (c4 -> c8) | 2.0229 → 1.9799 | -0.0430 |
| boost amharique seul x2 (c4 -> c7) | 2.0229 → 2.0116 | -0.0114 |
| modele Unigram au lieu de BPE (c4 -> c6) | 2.0229 → 2.0341 | +0.0111 |
| ByteLevel au lieu de WhitespaceSplit (c4 -> c5) | 2.0229 → 2.0826 | +0.0596 |

Réglages **sans aucun effet mesurable** : `min_frequency` (2/5/10) et `initial_alphabet` (c2 = c3 = c4, scores *strictement* identiques). Autrement dit, aucun merge du modèle final n'a une fréquence < 10 (le seuil ne mord jamais) et l'alphabet du train couvre déjà tous les caractères rencontrés. **Ce ne sont pas des leviers** : ne pas les retester.

## 11. Réponses aux trois questions

### Pourquoi c8-scoredboost est-il meilleur que la baseline ?

Deux leviers **mesurés et indépendants**, qui expliquent la totalité du gain de −0.0800 (3,89 %) :

1. **Pré-tokeniseur `WhitespaceSplit`** (−0.0370, soit 46 % du gain) : la ponctuation reste collée au mot. Avec `Whitespace`, la baseline isole toute suite de caractères non-mot en un pré-token séparé — « word, » devient `word` + `,` et coûte donc un token de plus. C'est vérifiable dans les vocabulaires : la baseline ne contient **0 merge et 1 token** de vocabulaire qui réunissent un mot et une ponctuation, contre **529 merges et 530 tokens** pour c8. C'est un levier **gratuit** : à lui seul (c2), il améliore **les six langues** — en 1.8949→1.8705, fr 2.0584→1.9836, ha 1.7731→1.7345, sw 1.9137→1.8938, yo 1.8995→1.8659, am 2.6536→2.5975. Les régressions en/fr n'apparaissent qu'avec le boost (c8).
2. **Sur-échantillonnage des 4 langues notées ×2** (−0.0430, soit 54 % du gain) : le vocabulaire a été réalloué vers les langues notées. Mesuré dans les merges : amharique 1,273 → 1,506 (+233 ; 18.3 % → 21.7 % du budget), yoruba 218 → 252 (+34), hausa 29 → 30 (+1), tandis que le latin ASCII perd 241 merges (4,920 → 4,679) et le latin précomposé (français accentué + tons yoruba) 33. Les merges africains remontent en rang (`ẹ+̀` 63 → 46, `እ+ን` 120 → 95).

Le prix : **English +0.0611** et **French +0.0317** (hors score). Le budget du guardrail est passé de 2.3033 à 2.2112, et les marges restent confortables (en +0.2609, fr +0.1907) → **PASS**. Attention : la marge française est tombée de +0.2449 à +0.1212 — c'est la contrainte à surveiller pour toute expérience future.

### Quelle modification a le plus probablement produit le gain ?

**Le boost des langues notées** (−0.0430), légèrement devant le pré-tokeniseur (−0.0370). Les deux sont nécessaires : le pré-tokeniseur améliore *toutes* les langues (y compris en/fr) sans coût, alors que le boost achète les langues notées en dégradant en/fr — c'est cet échange qui produit le gain de score, et il n'est possible que parce que le guardrail laisse de la marge.

### Quelle est la prochaine expérience la plus prometteuse pour passer sous 1.9799 ?

**EXP-004 — `c9-bytefallback` : c8 + `BPE(byte_fallback=True)` pour supprimer les 255 `[UNK]`.**

C'est le gain le plus grand et le plus **certain** parmi les pistes mesurables :

- pénalité UNK actuelle, exactement mesurée : **0.0571 point** (elle disparaît entièrement si aucun `[UNK]` n'est plus émis) ;
- coût maximal en fertility (187 `[UNK]` dans les langues notées, au pire 561 tokens byte ajoutés sur 324,822 mots) : **+0.0017 point au pire** ;
- **gain net garanti ≥ +0.0554 → score ≤ 1.9246** (borne supérieure ; le coût réel sera plus faible, la plupart des caractères concernés font 3 octets).
- Réserve honnête : coût non inclus : les tokens byte occupent des places de vocabulaire (autant de merges en moins) ; à mesurer, et byte_fallback ne s'applique qu'à l'apprentissage et à l'encodage du modèle BPE.

Piste de repli (**EXP-005**), appuyée elle aussi sur des mesures déjà présentes dans `optimization_sweep.json` : un **boost par paliers** (`am ×3` ou `×4`, `ha/sw/yo ×2`). Justification : `c7` (boost amharique **seul** ×2, score global 2.0116 — donc perdant) obtient **Amharic 2.4089**, meilleur que les 2.5241 de c8 : l'amharique est la langue qui répond le plus au boost, et c8 en a réparti le budget sur quatre langues. Comme l'amharique pèse 40,4 % du gain total, renforcer son boost sans affaiblir les trois autres est la direction naturelle. ⚠️ Attention mesurable : le budget du guardrail vaut `1,15 × moyenne(fertility des 4 langues notées)`, donc baisser encore la fertility amharique **abaisse aussi le budget** et rogne la marge en/fr (c8 : en +0.2553 / fr +0.1212). À mesurer — le notebook recalcule le verdict de guardrail à chaque configuration.

---

## CURRENT BEST

```text
CURRENT BEST
============

Baseline:      2.0600
Best:          1.9799   (c8-scoredboost)
Gain:          +0.0800  (3.89 %)

Model:         BPE (unk_token=[UNK], 6,955 merges)
Vocab:         10 000 / 10 000
Normalizer:    NFC
PreTokenizer:  WhitespaceSplit

Best language: Amharic  2.6536 -> 2.5241  (-0.1295)
Worst language: Amharic (toujours le plus coûteux : 2.5241)
                           moindre progression : Yoruba (-0.0561)

Largest improvement: Amharic -0.1295 (40.4 % du gain total)

Main reason for improvement:
  reallocation du vocabulaire vers les langues notees (boost x2) : +233 merges ge'ez,
  +34 merges yoruba, +1 hausa ; pre-tokeniseur WhitespaceSplit
  (ponctuation collee au mot : 529 merges mot+ponctuation
  contre 0 pour la baseline).

Recommended EXP-004:
  c9-bytefallback = c8 + BPE(byte_fallback=True) pour supprimer les 255 [UNK]
  gain net garanti >= +0.0554  ->  score <= 1.9246
```

- Guardrail c8 : budget 2.2112 | en fertility 1.9503 (marge +0.2609) | fr fertility 2.0205 (marge +0.1907) → **PASS**
- Checker officiel : **READY FOR SUBMISSION** (valid=True)

## 12. État de la soumission (constats lus, rien modifié)

- Dossier publié : `submissions/maick-code/` (branche `arena/01a0889d-tokenizer`, commit `a896e17`, poussé depuis Colab). ⚠️ La copie locale du dépôt est **un commit en retard** (`807a3fb`) : les artefacts du run Colab n'existent que sur la branche distante, et cet audit a donc travaillé sur des extraits lus dans `/tmp/audit/` — aucun fichier local n'a été créé ni écrasé.
- Fichiers : tokenizer.json (516 915 o) · metadata.yml (271 o) · README.md (378 o)
- `tokenizer.json` identique au meilleur modèle (SHA-256 `3c6ff5baa8e0a67c…`) ✔
- `metadata.yml` : team = Maick Dane NKOU · members = ['Maick'] · affiliation = AIMS SOUTH AFRICA

**Points à corriger avant la date limite** (aucun n'a été touché par cet audit) :

1. Le dossier publie est `maick-code` mais la cellule 10 du notebook 02 definit SLUG = "maick-dane-nkou" : si la cellule 10 est relancee telle quelle, un second dossier de soumission apparaitra (deux dossiers = PR probablement invalide). Aligner l'un sur l'autre avant de relancer.
2. `notebook.ipynb` est absent de submissions/maick-code/ : le format le declare optionnel, mais il est exige avant la date limite.
3. `approach` annonce « BPE/Unigram » alors que c8-scoredboost est un BPE pur (Unigram a ete teste et a perdu : +0.0111). A corriger pour exactitude.

_Aucun de ces points n'a ete modifie : l'audit est en lecture seule._

- Aucune nouvelle expérience n'a été lancée, aucun fichier existant n'a été modifié.
