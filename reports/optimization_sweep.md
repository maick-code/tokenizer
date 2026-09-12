# Étape 2 — Balayage d'optimisation (métrique officielle)

*Dataset `Similoluwa/african-multilingual-tokenizer-challenge` @ `v1.0.0` — train utilisé : 240,000 textes, validation : 24,000 lignes.*

## Classement

| Config | Score ↓ | Jacc ↑ | Guardrail | Hausa | Swahili | Yoruba | Amharic | UNK | lossy | vocab | en | fr | budget |
|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `c30-lower-alph500-bf` | 1.7576 | 0.9642 | PASS | 1.4926 | 1.6653 | 1.6598 | 2.2128 | 0 | 23,989 | 10000 | 1.7432 | 1.8451 | 2.0212 |
| `c32-lower-alph1000-bf-b3` | 1.7577 | 0.9652 | PASS | 1.4939 | 1.6704 | 1.6630 | 2.2037 | 0 | 23,989 | 10000 | 1.8000 | 1.9269 | 2.0214 |
| `c31-lower-alph1000-bf` | 1.7711 | 0.9650 | PASS | 1.5039 | 1.6813 | 1.6674 | 2.2318 | 0 | 23,989 | 10000 | 1.7623 | 1.8608 | 2.0368 |
| `c23-alph500-bf-b4` | 1.8142 | 0.9038 | PASS | 1.5692 | 1.7408 | 1.7471 | 2.1996 | 0 | 23,985 | 10000 | 1.9287 | 2.0532 | 2.0863 |
| `c22-alph500-bf-am4b3` | 1.8211 | 0.9054 | PASS | 1.5920 | 1.7710 | 1.7703 | 2.1513 | 0 | 23,985 | 10000 | 1.9234 | 2.0241 | 2.0943 |
| `c20-alph500-bf-b3` | 1.8237 | 0.9041 | PASS | 1.5751 | 1.7520 | 1.7520 | 2.2159 | 0 | 23,985 | 10000 | 1.8997 | 1.9997 | 2.0973 |
| `c37-alph500-bf-am3` | 1.8317 | 0.9052 | PASS | 1.6078 | 1.7888 | 1.7825 | 2.1477 | 0 | 23,985 | 10000 | 1.8824 | 1.9618 | 2.1064 |
| `c38-alph500-bf-swyo3` | 1.8338 | 0.9026 | PASS | 1.5998 | 1.7177 | 1.7200 | 2.2976 | 0 | 23,985 | 10000 | 1.8638 | 1.9587 | 2.1088 |
| `c28-nfkc-alph500-bf` | 1.8343 | 0.9036 | PASS | 1.5846 | 1.7606 | 1.7564 | 2.2358 | 0 | 23,985 | 10000 | 1.8523 | 1.9319 | 2.1095 |
| `c12-alph500-bf` | 1.8359 | 0.9036 | PASS | 1.5847 | 1.7606 | 1.7565 | 2.2419 | 0 | 23,985 | 10000 | 1.8523 | 1.9320 | 2.1113 |
| `c39-alph500-bf-mf2` | 1.8359 | 0.9036 | PASS | 1.5847 | 1.7606 | 1.7565 | 2.2419 | 0 | 23,985 | 10000 | 1.8523 | 1.9320 | 2.1113 |
| `c40-alph500-bf-mf8` | 1.8359 | 0.9036 | PASS | 1.5847 | 1.7606 | 1.7565 | 2.2419 | 0 | 23,985 | 10000 | 1.8523 | 1.9320 | 2.1113 |
| `c17-alph1000-bf-b3` | 1.8376 | 0.9054 | PASS | 1.5870 | 1.7672 | 1.7641 | 2.2322 | 0 | 23,985 | 10000 | 1.9173 | 2.0169 | 2.1133 |
| `c13-alph1000-bf-am3` | 1.8457 | 0.9067 | PASS | 1.6193 | 1.8052 | 1.7960 | 2.1623 | 0 | 23,985 | 10000 | 1.8988 | 1.9796 | 2.1226 |
| `c11-alph1000-bf` | 1.8495 | 0.9049 | PASS | 1.5951 | 1.7793 | 1.7661 | 2.2573 | 0 | 23,985 | 10000 | 1.8694 | 1.9477 | 2.1269 |
| `c25-punctiso-alph500-bf-b3` | 1.8745 | 0.9385 | PASS | 1.6295 | 1.7830 | 1.7969 | 2.2885 | 0 | 23,985 | 10000 | 1.9281 | 2.0811 | 2.1556 |
| `c21-alph250-bf-b3` | 1.8856 | 0.9038 | PASS | 1.5844 | 1.7458 | 1.7624 | 2.4500 | 0 | 23,985 | 10000 | 1.8921 | 2.0189 | 2.1685 |
| `c29-nfkc-punctiso-alph500-bf` | 1.8864 | 0.9386 | PASS | 1.6368 | 1.7953 | 1.8028 | 2.3107 | 0 | 23,985 | 10000 | 1.8814 | 2.0154 | 2.1694 |
| `c24-punctiso-alph500-bf` | 1.8879 | 0.9386 | PASS | 1.6367 | 1.7953 | 1.8028 | 2.3165 | 0 | 23,985 | 10000 | 1.8815 | 2.0153 | 2.1710 |
| `c10-alph2000-bf` | 1.8881 | 0.9077 | PASS | 1.6251 | 1.8139 | 1.8008 | 2.3126 | 0 | 23,985 | 10000 | 1.9098 | 1.9883 | 2.1713 |
| `c27-punctdigits-alph500-bf` | 1.8892 | 0.9385 | PASS | 1.6367 | 1.7946 | 1.8074 | 2.3180 | 0 | 23,985 | 10000 | 1.8814 | 2.0139 | 2.1726 |
| `c18-alph250-bf` | 1.8993 | 0.9034 | PASS | 1.5922 | 1.7557 | 1.7673 | 2.4819 | 0 | 23,985 | 10000 | 1.8446 | 1.9418 | 2.1842 |
| `c9-bytefallback` | 1.9368 | 0.9106 | PASS | 1.6658 | 1.8600 | 1.8404 | 2.3811 | 0 | 23,985 | 10000 | 1.9599 | 2.0367 | 2.2273 |
| `c15-sp-unigram` | 1.9674 | 0.8777 | PASS | 1.6801 | 1.8578 | 1.8876 | 2.4441 | 0 | 0 | 10000 | 1.9424 | 2.0956 | 2.2625 |
| `c33-uni-alph500-bf` | 1.9674 | 0.9250 | PASS | 1.7221 | 1.9362 | 1.8777 | 2.3338 | 0 | 23,985 | 10000 | 1.9809 | 2.0551 | 2.2626 |
| `c8-scoredboost` | 1.9799 | 0.9098 | PASS | 1.7006 | 1.8516 | 1.8434 | 2.5241 | 255 | 23,949 | 10000 | 1.9503 | 2.0205 | 2.2112 |
| `c7-wssplit-mf10-alpha-amboost` | 2.0116 | 0.9114 | PASS | 1.7773 | 1.9493 | 1.9107 | 2.4089 | 255 | 23,948 | 10000 | 1.9172 | 1.9671 | 2.2476 |
| `c36-sp-unigram-cov995` | 2.0196 | 0.8820 | PASS | 1.6937 | 1.8565 | 1.9015 | 2.6266 | 0 | 0 | 10000 | 1.9484 | 2.1111 | 2.3225 |
| `c2-wssplit-mf2` | 2.0229 | 0.9092 | PASS | 1.7345 | 1.8938 | 1.8659 | 2.5975 | 255 | 23,958 | 10000 | 1.8648 | 1.9141 | 2.2607 |
| `c3-wssplit-mf5` | 2.0229 | 0.9092 | PASS | 1.7345 | 1.8938 | 1.8659 | 2.5975 | 255 | 23,958 | 10000 | 1.8648 | 1.9141 | 2.2607 |
| `c4-wssplit-mf10-alpha` | 2.0229 | 0.9092 | PASS | 1.7345 | 1.8938 | 1.8659 | 2.5975 | 255 | 23,958 | 10000 | 1.8648 | 1.9141 | 2.2607 |
| `c6-unigram-alpha` | 2.0341 | 0.9243 | PASS | 1.7627 | 1.9463 | 1.8849 | 2.5424 | 228 | 23,986 | 10000 | 1.8608 | 1.9003 | 2.2793 |
| `b1-baseline` | 2.0600 | 0.9386 | PASS | 1.7731 | 1.9137 | 1.8995 | 2.6536 | 255 | 23,987 | 10000 | 1.8893 | 1.9889 | 2.3033 |
| `c34-uni-punctiso-alph500-bf` | 2.0738 | 0.9407 | PASS | 1.8030 | 2.0788 | 2.0017 | 2.4118 | 0 | 23,985 | 10000 | 2.0896 | 2.2144 | 2.3849 |
| `c5-bytelevel` | 2.0826 | 0.8928 | PASS | 1.7503 | 1.9431 | 2.0778 | 2.5591 | 0 | 0 | 10000 | 1.8889 | 2.0097 | 2.3950 |
| `c35-sp-unigram-cov99` | 2.1133 | 0.8848 | PASS | 1.7025 | 1.8694 | 1.9384 | 2.9430 | 0 | 0 | 10000 | 1.9597 | 2.1323 | 2.4303 |
| `c14-wordpiece` | 2.2523 | 0.9023 | PASS | 1.9325 | 2.1675 | 2.1080 | 2.8012 | 182 | 23,998 | 10000 | 2.2484 | 2.3190 | 2.5468 |
| `c26-sp-unigram-cov98` | 2.3105 | 0.8862 | PASS | 1.7240 | 1.8747 | 2.0054 | 3.6379 | 0 | 0 | 10000 | 1.9882 | 2.1701 | 2.6571 |
| `c16-sp-bpe` | 2.6186 | 0.8896 | PASS | 2.6063 | 2.8367 | 2.4325 | 2.5987 | 0 | 0 | 10000 | 2.7520 | 2.8209 | 3.0113 |
| `c19-alph100-bf` | 2.8185 | 0.9041 | PASS | 1.6344 | 1.7492 | 2.0290 | 5.8612 | 0 | 23,985 | 10000 | 1.8416 | 2.0322 | 3.2412 |

## Fertility brute par langue

| Config | en | fr | ha | sw | yo | am |
|---|---:|---:|---:|---:|---:|---:|
| `c30-lower-alph500-bf` | 1.7432 | 1.8451 | 1.4926 | 1.6653 | 1.6598 | 2.2128 |
| `c32-lower-alph1000-bf-b3` | 1.8000 | 1.9269 | 1.4939 | 1.6704 | 1.6630 | 2.2037 |
| `c31-lower-alph1000-bf` | 1.7623 | 1.8608 | 1.5039 | 1.6813 | 1.6674 | 2.2318 |
| `c23-alph500-bf-b4` | 1.9287 | 2.0532 | 1.5692 | 1.7408 | 1.7471 | 2.1996 |
| `c22-alph500-bf-am4b3` | 1.9234 | 2.0241 | 1.5920 | 1.7710 | 1.7703 | 2.1513 |
| `c20-alph500-bf-b3` | 1.8997 | 1.9997 | 1.5751 | 1.7520 | 1.7520 | 2.2159 |
| `c37-alph500-bf-am3` | 1.8824 | 1.9618 | 1.6078 | 1.7888 | 1.7825 | 2.1477 |
| `c38-alph500-bf-swyo3` | 1.8638 | 1.9587 | 1.5998 | 1.7177 | 1.7200 | 2.2976 |
| `c28-nfkc-alph500-bf` | 1.8523 | 1.9319 | 1.5846 | 1.7606 | 1.7564 | 2.2358 |
| `c12-alph500-bf` | 1.8523 | 1.9320 | 1.5847 | 1.7606 | 1.7565 | 2.2419 |
| `c39-alph500-bf-mf2` | 1.8523 | 1.9320 | 1.5847 | 1.7606 | 1.7565 | 2.2419 |
| `c40-alph500-bf-mf8` | 1.8523 | 1.9320 | 1.5847 | 1.7606 | 1.7565 | 2.2419 |
| `c17-alph1000-bf-b3` | 1.9173 | 2.0169 | 1.5870 | 1.7672 | 1.7641 | 2.2322 |
| `c13-alph1000-bf-am3` | 1.8988 | 1.9796 | 1.6193 | 1.8052 | 1.7960 | 2.1623 |
| `c11-alph1000-bf` | 1.8694 | 1.9477 | 1.5951 | 1.7793 | 1.7661 | 2.2573 |
| `c25-punctiso-alph500-bf-b3` | 1.9281 | 2.0811 | 1.6295 | 1.7830 | 1.7969 | 2.2885 |
| `c21-alph250-bf-b3` | 1.8921 | 2.0189 | 1.5844 | 1.7458 | 1.7624 | 2.4500 |
| `c29-nfkc-punctiso-alph500-bf` | 1.8814 | 2.0154 | 1.6368 | 1.7953 | 1.8028 | 2.3107 |
| `c24-punctiso-alph500-bf` | 1.8815 | 2.0153 | 1.6367 | 1.7953 | 1.8028 | 2.3165 |
| `c10-alph2000-bf` | 1.9098 | 1.9883 | 1.6251 | 1.8139 | 1.8008 | 2.3126 |
| `c27-punctdigits-alph500-bf` | 1.8814 | 2.0139 | 1.6367 | 1.7946 | 1.8074 | 2.3180 |
| `c18-alph250-bf` | 1.8446 | 1.9418 | 1.5922 | 1.7557 | 1.7673 | 2.4819 |
| `c9-bytefallback` | 1.9599 | 2.0367 | 1.6658 | 1.8600 | 1.8404 | 2.3811 |
| `c15-sp-unigram` | 1.9424 | 2.0956 | 1.6801 | 1.8578 | 1.8876 | 2.4441 |
| `c33-uni-alph500-bf` | 1.9809 | 2.0551 | 1.7221 | 1.9362 | 1.8777 | 2.3338 |
| `c8-scoredboost` | 1.9503 | 2.0205 | 1.6528 | 1.8487 | 1.8294 | 2.3604 |
| `c7-wssplit-mf10-alpha-amboost` | 1.9172 | 1.9671 | 1.7294 | 1.9465 | 1.8967 | 2.2452 |
| `c36-sp-unigram-cov995` | 1.9484 | 2.1111 | 1.6937 | 1.8565 | 1.9015 | 2.6266 |
| `c2-wssplit-mf2` | 1.8648 | 1.9141 | 1.6867 | 1.8909 | 1.8519 | 2.4338 |
| `c3-wssplit-mf5` | 1.8648 | 1.9141 | 1.6867 | 1.8909 | 1.8519 | 2.4338 |
| `c4-wssplit-mf10-alpha` | 1.8648 | 1.9141 | 1.6867 | 1.8909 | 1.8519 | 2.4338 |
| `c6-unigram-alpha` | 1.8608 | 1.9003 | 1.7237 | 1.9435 | 1.8732 | 2.3875 |
| `b1-baseline` | 1.8893 | 1.9889 | 1.7252 | 1.9108 | 1.8855 | 2.4899 |
| `c34-uni-punctiso-alph500-bf` | 2.0896 | 2.2144 | 1.8030 | 2.0788 | 2.0017 | 2.4118 |
| `c5-bytelevel` | 1.8889 | 2.0097 | 1.7503 | 1.9431 | 2.0778 | 2.5591 |
| `c35-sp-unigram-cov99` | 1.9597 | 2.1323 | 1.7025 | 1.8694 | 1.9384 | 2.9430 |
| `c14-wordpiece` | 2.2484 | 2.3190 | 1.8913 | 2.1632 | 2.0870 | 2.7168 |
| `c26-sp-unigram-cov98` | 1.9882 | 2.1701 | 1.7240 | 1.8747 | 2.0054 | 3.6379 |
| `c16-sp-bpe` | 2.7520 | 2.8209 | 2.6063 | 2.8367 | 2.4325 | 2.5987 |
| `c19-alph100-bf` | 1.8416 | 2.0322 | 1.6344 | 1.7492 | 2.0290 | 5.8612 |

## Décision

- Baseline de référence : **2.0600**
- Meilleur score brut (guardrail OK) : `c30-lower-alph500-bf` — 1.7576 (jaccard 0.9642)
- **Sélection score + qualité : `c32-lower-alph1000-bf-b3` — score 1.7577** (+0.3022, jaccard 0.9652)
- Guardrail : budget 2.0214, en 1.8000, fr 1.9269 → PASS
- Modèle : `/content/models/optimized_c32-lower-alph1000-bf-b3/tokenizer.json`

## Configurations testées

- `b1-baseline` — référence : BPE+NFC+Whitespace, mf=2 (doit redonner ~2.0600) — score 2.0600 — jaccard 0.9386 — guardrail PASS
- `c2-wssplit-mf2` — ponctuation collée au mot (WhitespaceSplit) — score 2.0229 — jaccard 0.9092 — guardrail PASS
- `c3-wssplit-mf5` — WhitespaceSplit + min_frequency=5 — score 2.0229 — jaccard 0.9092 — guardrail PASS
- `c4-wssplit-mf10-alpha` — WhitespaceSplit + mf=10 + alphabet complet (supprime les UNK connus) — score 2.0229 — jaccard 0.9092 — guardrail PASS
- `c5-bytelevel` — ByteLevel(use_regex) : round-trip sans perte, zero UNK — score 2.0826 — jaccard 0.8928 — guardrail PASS
- `c6-unigram-alpha` — modele Unigram + alphabet complet — score 2.0341 — jaccard 0.9243 — guardrail PASS
- `c7-wssplit-mf10-alpha-amboost` — comme c4 + amharique sur-echantillonne x2 — score 2.0116 — jaccard 0.9114 — guardrail PASS
- `c8-scoredboost` — sur-echantillonnage des 4 langues notees (teste la limite du guardrail) — score 1.9799 — jaccard 0.9098 — guardrail PASS
- `c9-bytefallback` — EXP-004 : c8 + byte_fallback (256 tokens <0xXX>) -> supprime les [UNK] — score 1.9368 — jaccard 0.9106 — guardrail PASS
- `c10-alph2000-bf` — alphabet limité à 2000 caractères + byte fallback (les rares passent en <0xXX>) — score 1.8881 — jaccard 0.9077 — guardrail PASS
- `c11-alph1000-bf` — alphabet limité à 1000 caractères + byte fallback (~+2 000 merges vs c8) — score 1.8495 — jaccard 0.9049 — guardrail PASS
- `c12-alph500-bf` — alphabet limité à 500 caractères + byte fallback (limite basse du levier) — score 1.8359 — jaccard 0.9036 — guardrail PASS
- `c13-alph1000-bf-am3` — alphabet 1000 + byte fallback + amharique sur-échantillonné x3 — score 1.8457 — jaccard 0.9067 — guardrail PASS
- `c17-alph1000-bf-b3` — alphabet 1000 + byte fallback + les 4 langues notées x3 (frontière du guardrail) — score 1.8376 — jaccard 0.9054 — guardrail PASS
- `c18-alph250-bf` — alphabet limité à 250 caractères + byte fallback (sonde le genou du levier) — score 1.8993 — jaccard 0.9034 — guardrail PASS
- `c19-alph100-bf` — alphabet limité à 100 caractères + byte fallback (extrême basse du levier) — score 2.8185 — jaccard 0.9041 — guardrail PASS
- `c20-alph500-bf-b3` — alphabet 500 + les 4 langues notées x3 (croisement des deux leviers) — score 1.8237 — jaccard 0.9041 — guardrail PASS
- `c21-alph250-bf-b3` — alphabet 250 + les 4 langues notées x3 — score 1.8856 — jaccard 0.9038 — guardrail PASS
- `c22-alph500-bf-am4b3` — alphabet 500 + ha/sw/yo x3 et am x4 (l'amharique reste la langue la plus coûteuse) — score 1.8211 — jaccard 0.9054 — guardrail PASS
- `c23-alph500-bf-b4` — alphabet 500 + les 4 langues notées x4 (sonde la frontière du guardrail EN/FR) — score 1.8142 — jaccard 0.9038 — guardrail PASS
- `c24-punctiso-alph500-bf` — ponctuation isolée (\p{P}) + alphabet 500 + byte fallback — mots propres pour les merges — score 1.8879 — jaccard 0.9386 — guardrail PASS
- `c25-punctiso-alph500-bf-b3` — comme c24 avec les 4 langues notées x3 — score 1.8745 — jaccard 0.9385 — guardrail PASS
- `c26-sp-unigram-cov98` — SentencePiece unigram, character_coverage=0.98 (levier alphabet appliqué au unigram) — score 2.3105 — jaccard 0.8862 — guardrail PASS
- `c27-punctdigits-alph500-bf` — c24 + chiffres isolés (\d+) : formes de type « 2024, » nettoyées — score 1.8892 — jaccard 0.9385 — guardrail PASS
- `c28-nfkc-alph500-bf` — c12 + NFKC : variantes de compatibilité pliées (présentation arabes, fullwidth…) — score 1.8343 — jaccard 0.9036 — guardrail PASS
- `c29-nfkc-punctiso-alph500-bf` — NFKC + ponctuation isolée + alphabet 500 + byte fallback — score 1.8864 — jaccard 0.9386 — guardrail PASS
- `c30-lower-alph500-bf` — c12 + lowercase : « The »/« the » fusionnés (variante n°1 du test Jaccard) — score 1.7576 — jaccard 0.9642 — guardrail PASS
- `c31-lower-alph1000-bf` — c11 + lowercase — score 1.7711 — jaccard 0.9650 — guardrail PASS
- `c32-lower-alph1000-bf-b3` — c17 + lowercase (le lowercase fait-il rentrer x3 dans le guardrail ?) — score 1.7577 — jaccard 0.9652 — guardrail PASS
- `c33-uni-alph500-bf` — Unigram HF + alphabet 500 + byte fallback + notées x2 — score 1.9674 — jaccard 0.9250 — guardrail PASS
- `c34-uni-punctiso-alph500-bf` — Unigram HF + ponctuation isolée + alphabet 500 + byte fallback — score 2.0738 — jaccard 0.9407 — guardrail PASS
- `c35-sp-unigram-cov99` — SentencePiece unigram, character_coverage=0.99 (entre c26 et c15) — score 2.1133 — jaccard 0.8848 — guardrail PASS
- `c36-sp-unigram-cov995` — SentencePiece unigram, character_coverage=0.995 — score 2.0196 — jaccard 0.8820 — guardrail PASS
- `c37-alph500-bf-am3` — c12 + amharique x3 seul (entre c12 et c22) — score 1.8317 — jaccard 0.9052 — guardrail PASS
- `c38-alph500-bf-swyo3` — c12 + sw/yo x3 (les deuxièmes langues les plus chères) — score 1.8338 — jaccard 0.9026 — guardrail PASS
- `c39-alph500-bf-mf2` — c12 + min_frequency=2 — score 1.8359 — jaccard 0.9036 — guardrail PASS
- `c40-alph500-bf-mf8` — c12 + min_frequency=8 — score 1.8359 — jaccard 0.9036 — guardrail PASS
- `c14-wordpiece` — WordPiece (WhitespaceSplit, alphabet complet) — pas de byte fallback possible : l'option est ignorée pour WordPiece — score 2.2523 — jaccard 0.9023 — guardrail PASS
- `c15-sp-unigram` — SentencePiece unigram + byte fallback, converti en tokenizer.json — score 1.9674 — jaccard 0.8777 — guardrail PASS
- `c16-sp-bpe` — SentencePiece BPE + byte fallback, converti en tokenizer.json — score 2.6186 — jaccard 0.8896 — guardrail PASS
