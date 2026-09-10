# EXP-004 — `c9-bytefallback` : vérifications locales (le score reste à mesurer)

*Aucun score n'est annoncé ici : le dataset officiel n'est pas accessible depuis cet environnement (réseau HF bloqué). Tout ce qui pouvait être mesuré sans les données l'a été.*

## Ce que fait `c9-bytefallback`

`c8-scoredboost` **plus** le byte fallback : les 256 tokens `<0xXX>` représentent tous les octets UTF-8 possibles, donc **tout caractère**, même jamais vu à l'entraînement.

| Élément | Valeur (mesurée) |
|---|---|
| Modèle | `BPE(unk_token='[UNK]', byte_fallback=True)` |
| Normaliseur / pré-tokeniseur | `NFC` / `WhitespaceSplit` |
| Trainer | `BpeTrainer(vocab_size=10_000, min_frequency=5, special_tokens=['[UNK]'] + 256 tokens '<0xXX>', initial_alphabet=<alphabet du train>)` |
| Décodeur | `ByteFallback()` |
| `[UNK]` sur les 52 caractères fautifs | **0/52** |
| Coût d'un caractère (octets → tokens) | 2o octets → 2 tokens, 3o octets → 3 tokens, 4o octets → 4 tokens |
| `decode(skip_special_tokens=True)` conserve les octets | **True** |
| Checker officiel | **valid = True** (vocab 1,847, 6/6 contrôles) |

## Les deux pièges mesurés (ils auraient fait échouer un run Colab)

1. **`BPE(byte_fallback=True)` seul ne suffit pas** : sans les 256 tokens `<0xXX>` dans le vocabulaire du modèle, le tokenizer continue d'émettre `[UNK]` (mesuré : 41/41 mots fautifs).
2. **`add_tokens()` après entraînement ne marche pas non plus** (mesuré : 41/41 mots fautifs restent en `[UNK]`). La seule recette qui fonctionne est de passer les 256 tokens byte dans les `special_tokens` **du trainer** — puis de retirer leur entrée `added_tokens` pour qu'ils redeviennent des tokens ordinaires (forme Llama-2). C'est ce que fait la cellule 10.

## Budget de vocabulaire (vérifié)

- Corpus saturant, `vocab_size=1 000` : c8 → 1000 tokens / 986 merges ; c9 → 1000 tokens / 730 merges.
- **Dépassement : +0** → les 256 tokens byte sont comptés **dans** `vocab_size`. Le total reste donc 10 000 côté Colab, la règle des 10 000 tokens est respectée.
- Contrepartie : **256 merges appris en moins** (6,955 → ~6,700). C'est le seul coût non mesurable ici, et c'est précisément ce que le run Colab va chiffrer.

## Estimation du gain (mesures réelles, pas un score)

- Pénalité `[UNK]` retirée : **−0.05711**
- Coût des séquences byte : **+0.00112**
- **Gain net estimé : +0.05599 → score ≈ 1.9239** (avant coût des 255 merges perdus)

| Langue | Caractères distincts (échantillon) | Tokens en plus par `[UNK]` | `[UNK]` mesurés | Tokens en plus |
|---|---:|---:|---:|---:|
| English | 4 | +1.75 | 5 | +9 |
| French | 12 | +2.0 | 63 | +126 |
| Hausa | 6 | +2.0 | 43 | +86 |
| Swahili | 2 | +1.0 | 2 | +2 |
| Yoruba | 7 | +1.57 | 12 | +19 |
| Amharic | 21 | +2.0 | 130 | +260 |

_ESTIMATION a partir de mesures reelles, ce n'est PAS le score officiel : le score de c9 doit etre mesure dans Colab sur le split de validation officiel._
