# Maick Dane Nkou

Individual entry — tokenizer `c9-bytefallback`.

## Approach

- Model: BPE with `[UNK]` as unknown token; vocabulary 10,000 / 10,000
- Normalizer: NFC (no ASCII folding, no accent stripping, no lowercasing)
- Pre-tokenizer: `WhitespaceSplit` — punctuation stays attached to its word, so no token is
  spent on isolated `,` `.` `)` …
- Byte fallback: yes — the 256 `<0xXX>` tokens cover every possible UTF-8 character, so
  no `[UNK]` can ever be emitted
- Training corpus: official `train` split only, balanced round-robin over the six
  languages with am/ha/sw/yo oversampled x2; no external corpus and no pre-trained tokenizer
- Post-processor / decoder: none
- Built with `tokenizers==0.22.1`

## Results (official validation split, official metric)

| Language | Fertility | UNK rate | Score |
|---|---:|---:|---:|
| English | 1.9599 | 0.000000 | 1.9599 |
| French | 2.0367 | 0.000000 | 2.0367 |
| Hausa | 1.6658 | 0.000000 | 1.6658 |
| Swahili | 1.8600 | 0.000000 | 1.8600 |
| Yoruba | 1.8404 | 0.000000 | 1.8404 |
| Amharic | 2.3811 | 0.000000 | 2.3811 |

- **Score (mean of ha, sw, yo, am): 1.9368** — baseline BPE 10k 2.0600, i.e. a gain of +0.1232 (6.0 %)
- Context guardrail EN/FR: **PASS** (budget 2.2273, en 1.9599, fr 2.0367)
- UNK emitted on validation: 0

## Files

- `tokenizer.json` — the submitted tokenizer
- `metadata.yml` — team metadata
- `notebook.ipynb` — the notebook that built this tokenizer (`notebooks/02_optimization_sweep.ipynb`)
- `README.md` — this file
