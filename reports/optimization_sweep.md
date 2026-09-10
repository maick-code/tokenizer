# Étape 2 — Balayage d'optimisation (métrique officielle)

*Dataset `Similoluwa/african-multilingual-tokenizer-challenge` @ `v1.0.0` — train utilisé : 240,000 textes, validation : 24,000 lignes.*

## Classement

| Config | Score ↓ | Guardrail | Hausa | Swahili | Yoruba | Amharic | UNK | lossy | vocab | en | fr | budget |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `c9-bytefallback` | 1.9368 | PASS | 1.6658 | 1.8600 | 1.8404 | 2.3811 | 0 | 23,985 | 10000 | 1.9599 | 2.0367 | 2.2273 |
| `c8-scoredboost` | 1.9799 | PASS | 1.7006 | 1.8516 | 1.8434 | 2.5241 | 255 | 23,949 | 10000 | 1.9503 | 2.0205 | 2.2112 |
| `c7-wssplit-mf10-alpha-amboost` | 2.0116 | PASS | 1.7773 | 1.9493 | 1.9107 | 2.4089 | 255 | 23,948 | 10000 | 1.9172 | 1.9671 | 2.2476 |
| `c2-wssplit-mf2` | 2.0229 | PASS | 1.7345 | 1.8938 | 1.8659 | 2.5975 | 255 | 23,958 | 10000 | 1.8648 | 1.9141 | 2.2607 |
| `c3-wssplit-mf5` | 2.0229 | PASS | 1.7345 | 1.8938 | 1.8659 | 2.5975 | 255 | 23,958 | 10000 | 1.8648 | 1.9141 | 2.2607 |
| `c4-wssplit-mf10-alpha` | 2.0229 | PASS | 1.7345 | 1.8938 | 1.8659 | 2.5975 | 255 | 23,958 | 10000 | 1.8648 | 1.9141 | 2.2607 |
| `c6-unigram-alpha` | 2.0341 | PASS | 1.7627 | 1.9463 | 1.8849 | 2.5424 | 228 | 23,986 | 10000 | 1.8608 | 1.9003 | 2.2793 |
| `b1-baseline` | 2.0600 | PASS | 1.7731 | 1.9137 | 1.8995 | 2.6536 | 255 | 23,987 | 10000 | 1.8893 | 1.9889 | 2.3033 |
| `c5-bytelevel` | 2.0826 | PASS | 1.7503 | 1.9431 | 2.0778 | 2.5591 | 0 | 0 | 10000 | 1.8889 | 2.0097 | 2.3950 |

## Fertility brute par langue

| Config | en | fr | ha | sw | yo | am |
|---|---:|---:|---:|---:|---:|---:|
| `c9-bytefallback` | 1.9599 | 2.0367 | 1.6658 | 1.8600 | 1.8404 | 2.3811 |
| `c8-scoredboost` | 1.9503 | 2.0205 | 1.6528 | 1.8487 | 1.8294 | 2.3604 |
| `c7-wssplit-mf10-alpha-amboost` | 1.9172 | 1.9671 | 1.7294 | 1.9465 | 1.8967 | 2.2452 |
| `c2-wssplit-mf2` | 1.8648 | 1.9141 | 1.6867 | 1.8909 | 1.8519 | 2.4338 |
| `c3-wssplit-mf5` | 1.8648 | 1.9141 | 1.6867 | 1.8909 | 1.8519 | 2.4338 |
| `c4-wssplit-mf10-alpha` | 1.8648 | 1.9141 | 1.6867 | 1.8909 | 1.8519 | 2.4338 |
| `c6-unigram-alpha` | 1.8608 | 1.9003 | 1.7237 | 1.9435 | 1.8732 | 2.3875 |
| `b1-baseline` | 1.8893 | 1.9889 | 1.7252 | 1.9108 | 1.8855 | 2.4899 |
| `c5-bytelevel` | 1.8889 | 2.0097 | 1.7503 | 1.9431 | 2.0778 | 2.5591 |

## Décision

- Baseline de référence : **2.0600**
- **Meilleure configuration (guardrail OK) : `c9-bytefallback` — score 1.9368** (+0.1232)
- Guardrail : budget 2.2273, en 1.9599, fr 2.0367 → PASS
- Modèle : `/content/models/optimized_c9-bytefallback/tokenizer.json`

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
