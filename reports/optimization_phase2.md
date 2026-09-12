# Phase 2 — Optimisation ciblée (score + qualité)

*Dataset `Similoluwa/african-multilingual-tokenizer-challenge` @ `v1.0.0` — train utilisé : 240,000 textes, validation : 24,000 lignes.*

## Classement

| Config | Score ↓ | Jacc ↑ | Guardrail | Hausa | Swahili | Yoruba | Amharic | UNK | lossy | vocab | en | fr | budget |
|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `c42-lower-alph500-b4` | 1.7363 | 0.9646 | PASS | 1.4784 | 1.6487 | 1.6514 | 2.1668 | 0 | 23,989 | 10000 | 1.8094 | 1.9603 | 1.9968 |
| `c41-lower-alph500-b3` | 1.7440 | 0.9645 | PASS | 1.4839 | 1.6548 | 1.6535 | 2.1838 | 0 | 23,989 | 10000 | 1.7828 | 1.9107 | 2.0056 |
| `c54-lower-alph400-b3` | 1.7450 | 0.9645 | PASS | 1.4842 | 1.6535 | 1.6525 | 2.1898 | 0 | 23,989 | 10000 | 1.7802 | 1.9100 | 2.0067 |
| `c55-lower-alph750-b3` | 1.7496 | 0.9649 | PASS | 1.4888 | 1.6620 | 1.6567 | 2.1911 | 0 | 23,989 | 10000 | 1.7924 | 1.9183 | 2.0121 |
| `c46-lower-alph500-swyo3` | 1.7538 | 0.9637 | PASS | 1.5017 | 1.6250 | 1.6282 | 2.2604 | 0 | 23,989 | 10000 | 1.7530 | 1.8703 | 2.0169 |
| `c53-nfkclower-alph500` | 1.7561 | 0.9642 | PASS | 1.4925 | 1.6652 | 1.6597 | 2.2068 | 0 | 23,989 | 10000 | 1.7431 | 1.8450 | 2.0195 |
| `c43-lower-alph500-am4` | 1.7573 | 0.9657 | PASS | 1.5346 | 1.7185 | 1.7019 | 2.0742 | 0 | 23,989 | 10000 | 1.7947 | 1.9039 | 2.0209 |
| `c30-lower-alph500-bf` | 1.7576 | 0.9642 | PASS | 1.4926 | 1.6653 | 1.6598 | 2.2128 | 0 | 23,989 | 10000 | 1.7432 | 1.8451 | 2.0212 |
| `c32-lower-alph1000-bf-b3` | 1.7577 | 0.9652 | PASS | 1.4939 | 1.6703 | 1.6630 | 2.2036 | 0 | 23,989 | 10000 | 1.8000 | 1.9269 | 2.0214 |
| `c44-lower-alph500-am5` | 1.7623 | 0.9666 | PASS | 1.5513 | 1.7391 | 1.7216 | 2.0373 | 0 | 23,989 | 10000 | 1.8169 | 1.9293 | 2.0266 |
| `c45-lower-alph500-am6` | 1.7673 | 0.9669 | PASS | 1.5650 | 1.7565 | 1.7374 | 2.0102 | 0 | 23,989 | 10000 | 1.8366 | 1.9519 | 2.0324 |
| `c47-lower-alph500-ha1am4` | 1.7709 | 0.9666 | PASS | 1.6190 | 1.7118 | 1.6986 | 2.0543 | 0 | 23,989 | 10000 | 1.7848 | 1.8916 | 2.0365 |
| `c51-lower-punctiso-alph500` | 1.8121 | 1.0000 | PASS | 1.5487 | 1.7038 | 1.7128 | 2.2830 | 0 | 23,989 | 10000 | 1.7781 | 1.9292 | 2.0839 |
| `c50-lower-geztopup` | 1.8462 | 0.9679 | PASS | 1.5594 | 1.7528 | 1.7298 | 2.3428 | 0 | 23,989 | 10000 | 1.8411 | 1.9429 | 2.1231 |
| `c48-lower-cleanalpha-v1` | 1.8472 | 0.9679 | PASS | 1.5599 | 1.7536 | 1.7312 | 2.3441 | 0 | 23,989 | 10000 | 1.8421 | 1.9433 | 2.1243 |
| `c49-lower-cleanalpha-v2` | 1.8473 | 0.9679 | PASS | 1.5599 | 1.7536 | 1.7314 | 2.3444 | 0 | 23,989 | 10000 | 1.8424 | 1.9433 | 2.1244 |
| `c52-lower-uni-alph500` | 1.8816 | 0.9855 | PASS | 1.6233 | 1.8272 | 1.7776 | 2.2985 | 0 | 23,989 | 10000 | 1.8666 | 1.9516 | 2.1639 |

## Fertility brute par langue

| Config | en | fr | ha | sw | yo | am |
|---|---:|---:|---:|---:|---:|---:|
| `c42-lower-alph500-b4` | 1.8094 | 1.9603 | 1.4784 | 1.6487 | 1.6514 | 2.1668 |
| `c41-lower-alph500-b3` | 1.7828 | 1.9107 | 1.4839 | 1.6548 | 1.6535 | 2.1838 |
| `c54-lower-alph400-b3` | 1.7802 | 1.9100 | 1.4842 | 1.6535 | 1.6525 | 2.1898 |
| `c55-lower-alph750-b3` | 1.7924 | 1.9183 | 1.4888 | 1.6620 | 1.6567 | 2.1911 |
| `c46-lower-alph500-swyo3` | 1.7530 | 1.8703 | 1.5017 | 1.6250 | 1.6282 | 2.2604 |
| `c53-nfkclower-alph500` | 1.7431 | 1.8450 | 1.4925 | 1.6652 | 1.6597 | 2.2068 |
| `c43-lower-alph500-am4` | 1.7947 | 1.9039 | 1.5346 | 1.7185 | 1.7019 | 2.0742 |
| `c30-lower-alph500-bf` | 1.7432 | 1.8451 | 1.4926 | 1.6653 | 1.6598 | 2.2128 |
| `c32-lower-alph1000-bf-b3` | 1.8000 | 1.9269 | 1.4939 | 1.6703 | 1.6630 | 2.2036 |
| `c44-lower-alph500-am5` | 1.8169 | 1.9293 | 1.5513 | 1.7391 | 1.7216 | 2.0373 |
| `c45-lower-alph500-am6` | 1.8366 | 1.9519 | 1.5650 | 1.7565 | 1.7374 | 2.0102 |
| `c47-lower-alph500-ha1am4` | 1.7848 | 1.8916 | 1.6190 | 1.7118 | 1.6986 | 2.0543 |
| `c51-lower-punctiso-alph500` | 1.7781 | 1.9292 | 1.5487 | 1.7038 | 1.7128 | 2.2830 |
| `c50-lower-geztopup` | 1.8411 | 1.9429 | 1.5594 | 1.7528 | 1.7298 | 2.3428 |
| `c48-lower-cleanalpha-v1` | 1.8421 | 1.9433 | 1.5599 | 1.7536 | 1.7312 | 2.3441 |
| `c49-lower-cleanalpha-v2` | 1.8424 | 1.9433 | 1.5599 | 1.7536 | 1.7314 | 2.3444 |
| `c52-lower-uni-alph500` | 1.8666 | 1.9516 | 1.6233 | 1.8272 | 1.7776 | 2.2985 |

## Décision

- Baseline originelle : **2.0600**
- Référence phase 1 : `c32-lower-alph1000-bf-b3` — 1.7577 (jaccard 0.9652)
- Meilleur score brut phase 2 : `c42-lower-alph500-b4` — 1.7363 (jaccard 0.9646)
- **Sélection phase 2 (score + qualité) : `c42-lower-alph500-b4` — score 1.7363** (vs réf +0.0214, jaccard 0.9646)
- Guardrail : budget 1.9968, en 1.8094, fr 1.9603 → PASS
- Modèle : `/content/models/phase2_best/tokenizer.json`

## Configurations testées

- `c30-lower-alph500-bf` — CALIBRATEUR : meilleur brut phase 1 (1.7576) — score 1.7576 — jaccard 0.9642 — guardrail PASS
- `c32-lower-alph1000-bf-b3` — CALIBRATEUR : sélection phase 1 (1.7577, jaccard 0.9652) — score 1.7577 — jaccard 0.9652 — guardrail PASS
- `c41-lower-alph500-b3` — LA case manquante : c30 + boost x3 (priorité n°1) — score 1.7440 — jaccard 0.9645 — guardrail PASS
- `c42-lower-alph500-b4` — SONDE frontière : lower+x4 (sélection seulement si marge ≥ 0.04) — score 1.7363 — jaccard 0.9646 — guardrail PASS
- `c43-lower-alph500-am4` — c30 + amharique x4 seul (bottleneck, frugal en guardrail) — score 1.7573 — jaccard 0.9657 — guardrail PASS
- `c44-lower-alph500-am5` — c30 + amharique x5 seul — score 1.7623 — jaccard 0.9666 — guardrail PASS
- `c45-lower-alph500-am6` — SONDE : c30 + amharique x6 seul (rendements décroissants ?) — score 1.7673 — jaccard 0.9669 — guardrail PASS
- `c46-lower-alph500-swyo3` — c38 sous lowercase : sw/yo x3 (deuxièmes langues les plus chères) — score 1.7538 — jaccard 0.9637 — guardrail PASS
- `c47-lower-alph500-ha1am4` — réallocation parité : ha déjà à 1.49 → sa part va à am x4 — score 1.7709 — jaccard 0.9666 — guardrail PASS
- `c48-lower-cleanalpha-v1` — alphabet nettoyé v1 (arabe gardé, hypothèse Ajami) + byte fallback — score 1.8472 — jaccard 0.9679 — guardrail PASS
- `c49-lower-cleanalpha-v2` — SONDE : alphabet nettoyé v2 SANS arabe (teste l'hypothèse Ajami) — score 1.8473 — jaccard 0.9679 — guardrail PASS
- `c50-lower-geztopup` — top-500 + TOUT l'éthiopien du train (couverture guèze totale) — score 1.8462 — jaccard 0.9679 — guardrail PASS
- `c51-lower-punctiso-alph500` — lower × ponctuation isolée (cartographie score×qualité) — score 1.8121 — jaccard 1.0000 — guardrail PASS
- `c52-lower-uni-alph500` — dernière chance unigram : c33 sous lowercase — score 1.8816 — jaccard 0.9855 — guardrail PASS
- `c53-nfkclower-alph500` — NFKC + lowercase (point final normalisation) — score 1.7561 — jaccard 0.9642 — guardrail PASS
- `c54-lower-alph400-b3` — alphabet 400 + lower + x3 (entre le genou 250 et l'optimum 500) — score 1.7450 — jaccard 0.9645 — guardrail PASS
- `c55-lower-alph750-b3` — alphabet 750 + lower + x3 (entre 500 et 1000) — score 1.7496 — jaccard 0.9649 — guardrail PASS
