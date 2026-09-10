# Maick Dane Nkou

Individual entry — tokenizer `c8-scoredboost`.

## Approach

- Model: BPE with `[UNK]` as unknown token; vocabulary 10,000 / 10,000
- Normalizer: NFC (no ASCII folding, no accent stripping, no lowercasing)
- Pre-tokenizer: `WhitespaceSplit` — punctuation stays attached to its word, so no token is
  spent on isolated `,` `.` `)` …
- Byte fallback: no — the few `[UNK]` left are rare non-African residues of the source
  text (Arabic presentation forms, CJK, kana, hangul, emoji)
- Training corpus: official `train` split only, balanced round-robin over the six
  languages with am/ha/sw/yo oversampled x2; no external corpus and no pre-trained tokenizer
- Post-processor / decoder: none
- Built with `tokenizers==0.22.1`

## Results (official validation split, official metric)

| Language | Fertility | UNK rate | Score |
|---|---:|---:|---:|
| Hausa | 1.6528 | 0.000479 | 1.7006 |
| Swahili | 1.8487 | 0.000029 | 1.8516 |
| Yoruba | 1.8294 | 0.000140 | 1.8434 |
| Amharic | 2.3604 | 0.001637 | 2.5241 |
| English | 1.9503 | 0.000057 | 1.9560 |
| French | 2.0205 | 0.000695 | 2.0900 |

- **Score (mean of ha, sw, yo, am): 1.9799** — baseline BPE 10k 2.0600, i.e. a gain of +0.0800 (3.9 %)
- Context guardrail EN/FR: **PASS** (budget 2.2112, en 1.9503, fr 2.0205)
- UNK emitted on validation: 255

## Files

- `tokenizer.json` — the submitted tokenizer
- `metadata.yml` — team metadata
- `notebook.ipynb` — the notebook that built this tokenizer (`notebooks/02_optimization_sweep.ipynb`)
- `README.md` — this file
