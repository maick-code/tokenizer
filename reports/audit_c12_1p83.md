# Audit de la soumission à 1.8359 — `c12-alph500-bf`

*Audit local basé uniquement sur le rapport du run Colab réel et les tokenizer.json publiés. 
Aucun score ici n'est une projection affirmée : les projections sont marquées « estimation ».*

## 1. Où va le score (moyenne officielle ha/sw/yo/am)

| Langue | Fertility | Contribution au score (÷4) | Écart à la moyenne |
|---|---:|---:|---:|
| ha | 1.5847 | 0.3962 | -0.2512 |
| sw | 1.7606 | 0.4402 | -0.0753 |
| yo | 1.7565 | 0.4391 | -0.0795 |
| am | 2.2419 | 0.5605 | +0.4060 |
| **Score** | — | **1.8359** | — |

**L'amharique pèse à lui seul +0.4060 au-dessus de la moyenne.** Les trois autres langues notées sont déjà à 1.7006 de moyenne.

## 2. Le vocabulaire : où sont passées les 10 000 places

| Composant | `c9` (alphabet complet) | `c12` (alphabet 500) |
|---|---:|---:|
| Tokens d'UN caractère | 3,044 | 500 |
| Tokens byte `<0xXX>` | 256 | 256 |
| Merges (pièces multi-caractères) | **6,699** | **9,243** |
| Vocab total | 10,000 | 10,000 |

- Passer de 3,044 à 500 caractères a libéré **+2,544 merges** — c'est exactement le levier qui a fait descendre 1.9368 → 1.8359.
- Parmi les 2544 caractères sacrifiés par `limit_alphabet=500`, **74 sont éthiopiques** : l'amharique paie 2-3 tokens (`<0xXX>`) par caractère rare, mais les merges gagnés compensent largement (am : 2.3811 → 2.2419).
- Prochaines réductions (250, 100 : `c18`, `c19`) ne libèrent plus que +250/+400 places : gain attendu en **forte décélération** (estimation : −0.002 à −0.008). En contrepartie, plus l'alphabet rétrécit, plus les caractères *fréquents* risquent de tomber dedans (le smoke synthétique de `c19` montrait une fertility en explosion).

## 3. La frontière du guardrail EN/FR (le vrai plafond)

Le guardrail impose `fertility(en,fr) ≤ 1.15 × score`. Ratio fertility/score constaté :

| Config | en/score | fr/score |
|---|---:|---:|
| `c9-bytefallback` | 1.0119 | 1.0516 |
| `c11-alph1000-bf` | 1.0108 | 1.0531 |
| `c12-alph500-bf` | 1.0089 | 1.0523 |
| `c17-alph1000-bf-b3` | 1.0434 | 1.0975 |

- `c12` : budget 2.1113, fr à 1.9320 → **marge +0.1793** (`en` : +0.2590).
- Le boost ×3 (c17 vs c11) monte le ratio fr/score de ~1.052 à ~1.098 ; la limite est 1.15. Il reste donc de la place pour ×3, et ×4 (`c23`) touche la frontière — c'est voulu, c'est une sonde.
- **Attention** : le budget est *relatif au score*. Plus le score baisse, plus le budget diminue. À score 1.75, le budget fr serait ~2.01 : le ×3 passerait encore, le ×4 non.

## 4. Chemins vers < 1.70 (arithmétique, pas des scores)

Il faut gagner **0.1359** points. Trois chemins équivalents :

1. **Amharique seul** : le faire passer de 2.2419 à 1.6982 (−0.5436, soit −24 %) — irréaliste avec le seul vocabulaire alloué.
2. **Uniforme** : −0.0340 sur CHAQUE langue notée.
3. **Réaliste (estimation)** : EXP-006b (c18–c23) combine alphabet 250–500 et boost ×3–×4 : deltas mesurés comparables → **−0.010 à −0.025 attendus, vers ~1.81–1.83**. 
   Le levier suivant est **structurel** :
   - **EXP-008, isolation de la ponctuation** (`c24`, `c25`) : avec `WhitespaceSplit`, `mot,` « mot. » etc. sont des mots d'entraînement distincts qui diluent les statistiques de merges ; isoler `\p{P}` rend les mots propres et la ponctuation en 1 token — les merges apprennent les vraies fréquences de mots. Gain typique des pré-tokeniseurs BERT-style : de l'ordre du centième, à confirmer par mesure.
   - **EXP-008, unigram SentencePiece à coverage réduit** (`c26`) : le unigram optimise globally au lieu des fusions gloutonnes ; `character_coverage=0.98` lui applique le levier alphabet qui a rapporté −0.10 à BPE. `c15` (coverage 0.9995) avait perdu de 0.031 contre `c9` — le coverage réduit est la variable non testée.
   - Après mesure : empiler les gagnants (ponctuation isolée + meilleur alphabet + meilleur boost).

## 5. Vérifications d'intégrité (rappel)

- Vérification officielle complète : **24/24 PASS** (dossier, metadata, tokenizer, sha, 
  score recalculé 1.835905, guardrail budget 2.111291).
- Vitesse : c12 ~6.4 Mcar/s vs baseline ~6.0 (limite officielle 5×) — zéro risque, 
  et atout pour le départage à score égal (throughput).
- Aucune fuite : entraînement sur `train` uniquement (vérifié par lecture des cellules).

## 6. Conclusion de l'audit

1. La soumission actuelle (1.8359) est **intègre et conforme** (24/24).
2. **EXP-006b (c18–c23) + sondes structurelles (c24–c26)** sont prêts dans le notebook 02 : 
   un seul run Colab mesure tout ; attendu ~1.81–1.83 (estimation), pas 1.70.
3. Pour viser < 1.75 puis < 1.70 : empiler les leviers gagnants mesurés (alphabet optimal × boost optimal × pré-tokenisation ponctuation isolée), puis allocation fine du vocabulaire.
4. Le guardrail relatif (1.15 × score) est le vrai plafond du boost — les sondes c23/c25 
   existent précisément pour trouver la frontière sans la franchir.
