# Étape 2 — Balayage d'optimisation (métrique officielle)

*Dataset `Similoluwa/african-multilingual-tokenizer-challenge` @ `v1.0.0` — train utilisé : 240,000 textes, validation : 24,000 lignes.*

## Classement

| Config | Score ↓ | Guardrail | Hausa | Swahili | Yoruba | Amharic | UNK | lossy | vocab | en | fr | budget |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `c12-alph500-bf` | 1.8359 | PASS | 1.5847 | 1.7606 | 1.7565 | 2.2419 | 0 | 23,985 | 10000 | 1.8523 | 1.9320 | 2.1113 |
| `c17-alph1000-bf-b3` | 1.8376 | PASS | 1.5870 | 1.7672 | 1.7641 | 2.2322 | 0 | 23,985 | 10000 | 1.9173 | 2.0169 | 2.1133 |
| `c13-alph1000-bf-am3` | 1.8457 | PASS | 1.6193 | 1.8052 | 1.7960 | 2.1624 | 0 | 23,985 | 10000 | 1.8988 | 1.9799 | 2.1226 |
| `c11-alph1000-bf` | 1.8495 | PASS | 1.5951 | 1.7793 | 1.7661 | 2.2573 | 0 | 23,985 | 10000 | 1.8694 | 1.9477 | 2.1269 |
| `c10-alph2000-bf` | 1.8881 | PASS | 1.6251 | 1.8139 | 1.8008 | 2.3127 | 0 | 23,985 | 10000 | 1.9098 | 1.9883 | 2.1713 |
| `c9-bytefallback` | 1.9368 | PASS | 1.6658 | 1.8600 | 1.8404 | 2.3811 | 0 | 23,985 | 10000 | 1.9599 | 2.0367 | 2.2273 |
| `c15-sp-unigram` | 1.9674 | PASS | 1.6801 | 1.8578 | 1.8876 | 2.4441 | 0 | 0 | 10000 | 1.9424 | 2.0956 | 2.2625 |
| `c8-scoredboost` | 1.9799 | PASS | 1.7006 | 1.8516 | 1.8434 | 2.5241 | 255 | 23,949 | 10000 | 1.9503 | 2.0205 | 2.2112 |
| `c7-wssplit-mf10-alpha-amboost` | 2.0116 | PASS | 1.7773 | 1.9493 | 1.9107 | 2.4089 | 255 | 23,948 | 10000 | 1.9172 | 1.9671 | 2.2476 |
| `c2-wssplit-mf2` | 2.0229 | PASS | 1.7345 | 1.8938 | 1.8659 | 2.5975 | 255 | 23,958 | 10000 | 1.8648 | 1.9141 | 2.2607 |
| `c3-wssplit-mf5` | 2.0229 | PASS | 1.7345 | 1.8938 | 1.8659 | 2.5975 | 255 | 23,958 | 10000 | 1.8648 | 1.9141 | 2.2607 |
| `c4-wssplit-mf10-alpha` | 2.0229 | PASS | 1.7345 | 1.8938 | 1.8659 | 2.5975 | 255 | 23,958 | 10000 | 1.8648 | 1.9141 | 2.2607 |
| `c6-unigram-alpha` | 2.0341 | PASS | 1.7627 | 1.9463 | 1.8849 | 2.5424 | 228 | 23,986 | 10000 | 1.8608 | 1.9003 | 2.2793 |
| `b1-baseline` | 2.0600 | PASS | 1.7731 | 1.9137 | 1.8995 | 2.6536 | 255 | 23,987 | 10000 | 1.8893 | 1.9889 | 2.3033 |
| `c5-bytelevel` | 2.0826 | PASS | 1.7503 | 1.9431 | 2.0778 | 2.5591 | 0 | 0 | 10000 | 1.8889 | 2.0097 | 2.3950 |
| `c14-wordpiece` | 2.2523 | PASS | 1.9325 | 2.1675 | 2.1080 | 2.8012 | 182 | 23,998 | 10000 | 2.2484 | 2.3190 | 2.5468 |
| `c16-sp-bpe` | 2.6186 | PASS | 2.6063 | 2.8367 | 2.4325 | 2.5987 | 0 | 0 | 10000 | 2.7520 | 2.8209 | 3.0113 |

## Fertility brute par langue

| Config | en | fr | ha | sw | yo | am |
|---|---:|---:|---:|---:|---:|---:|
| `c12-alph500-bf` | 1.8523 | 1.9320 | 1.5847 | 1.7606 | 1.7565 | 2.2419 |
| `c17-alph1000-bf-b3` | 1.9173 | 2.0169 | 1.5870 | 1.7672 | 1.7641 | 2.2322 |
| `c13-alph1000-bf-am3` | 1.8988 | 1.9799 | 1.6193 | 1.8052 | 1.7960 | 2.1624 |
| `c11-alph1000-bf` | 1.8694 | 1.9477 | 1.5951 | 1.7793 | 1.7661 | 2.2573 |
| `c10-alph2000-bf` | 1.9098 | 1.9883 | 1.6251 | 1.8139 | 1.8008 | 2.3127 |
| `c9-bytefallback` | 1.9599 | 2.0367 | 1.6658 | 1.8600 | 1.8404 | 2.3811 |
| `c15-sp-unigram` | 1.9424 | 2.0956 | 1.6801 | 1.8578 | 1.8876 | 2.4441 |
| `c8-scoredboost` | 1.9503 | 2.0205 | 1.6528 | 1.8487 | 1.8294 | 2.3604 |
| `c7-wssplit-mf10-alpha-amboost` | 1.9172 | 1.9671 | 1.7294 | 1.9465 | 1.8967 | 2.2452 |
| `c2-wssplit-mf2` | 1.8648 | 1.9141 | 1.6867 | 1.8909 | 1.8519 | 2.4338 |
| `c3-wssplit-mf5` | 1.8648 | 1.9141 | 1.6867 | 1.8909 | 1.8519 | 2.4338 |
| `c4-wssplit-mf10-alpha` | 1.8648 | 1.9141 | 1.6867 | 1.8909 | 1.8519 | 2.4338 |
| `c6-unigram-alpha` | 1.8608 | 1.9003 | 1.7237 | 1.9435 | 1.8732 | 2.3875 |
| `b1-baseline` | 1.8893 | 1.9889 | 1.7252 | 1.9108 | 1.8855 | 2.4899 |
| `c5-bytelevel` | 1.8889 | 2.0097 | 1.7503 | 1.9431 | 2.0778 | 2.5591 |
| `c14-wordpiece` | 2.2484 | 2.3190 | 1.8913 | 2.1632 | 2.0870 | 2.7168 |
| `c16-sp-bpe` | 2.7520 | 2.8209 | 2.6063 | 2.8367 | 2.4325 | 2.5987 |

## Décision

- Baseline de référence : **2.0600**
- **Meilleure configuration (guardrail OK) : `c12-alph500-bf` — score 1.8359** (+0.2241)
- Guardrail : budget 2.1113, en 1.8523, fr 1.9320 → PASS
- Modèle : `/content/models/optimized_c12-alph500-bf/tokenizer.json`

## Configurations testées

- `b1-baseline` — référence : BPE+NFC+Whitespace, mf=2 (doit redonner ~2.0600) — score 2.0600 — guardrail PASS
- `c2-wssplit-mf2` — ponctuation collée au mot (WhitespaceSplit) — score 2.0229 — guardrail PASS
- `c3-wssplit-mf5` — WhitespaceSplit + min_frequency=5 — score 2.0229 — guardrail PASS
- `c4-wssplit-mf10-alpha` — WhitespaceSplit + mf=10 + alphabet complet (supprime les UNK connus) — score 2.0229 — guardrail PASS
- `c5-bytelevel` — ByteLevel(use_regex) : round-trip sans perte, zero UNK — score 2.0826 — guardrail PASS
- `c6-unigram-alpha` — modele Unigram + alphabet complet — score 2.0341 — guardrail PASS
- `c7-wssplit-mf10-alpha-amboost` — comme c4 + amharique sur-echantillonne x2 — score 2.0116 — guardrail PASS
- `c8-scoredboost` — sur-echantillonnage des 4 langues notees (teste la limite du guardrail) — score 1.9799 — guardrail PASS
- `c9-bytefallback` — EXP-004 : c8 + byte_fallback (256 tokens <0xXX>) -> supprime les [UNK] — score 1.9368 — guardrail PASS
- `c10-alph2000-bf` — alphabet limité à 2000 caractères + byte fallback (les rares passent en <0xXX>) — score 1.8881 — guardrail PASS
- `c11-alph1000-bf` — alphabet limité à 1000 caractères + byte fallback (~+2 000 merges vs c8) — score 1.8495 — guardrail PASS
- `c12-alph500-bf` — alphabet limité à 500 caractères + byte fallback (limite basse du levier) — score 1.8359 — guardrail PASS
- `c13-alph1000-bf-am3` — alphabet 1000 + byte fallback + amharique sur-échantillonné x3 — score 1.8457 — guardrail PASS
- `c17-alph1000-bf-b3` — alphabet 1000 + byte fallback + les 4 langues notées x3 (frontière du guardrail) — score 1.8376 — guardrail PASS
- `c14-wordpiece` — WordPiece (WhitespaceSplit, alphabet complet) — pas de byte fallback possible : l'option est ignorée pour WordPiece — score 2.2523 — guardrail PASS
- `c15-sp-unigram` — SentencePiece unigram + byte fallback, converti en tokenizer.json — score 1.9674 — guardrail PASS
- `c16-sp-bpe` — SentencePiece BPE + byte fallback, converti en tokenizer.json — score 2.6186 — guardrail PASS
