# Maick Dane Nkou

Individual entry — tokenizer `c12-alph500-bf`.

## Approach

- Model: BPE with `[UNK]` as unknown token; vocabulary 10,000 / 10,000
- Normalizer: NFC
- Alphabet: limited to the 500 most frequent train characters (`limit_alphabet`); the characters left out are still covered by the byte fallback, so no `[UNK]` appears
- Pre-tokenizer: `WhitespaceSplit` — punctuation stays attached to its word, so no token is spent on isolated `,` `.` `)` …
- Byte fallback: yes — the 256 `<0xXX>` tokens cover every possible UTF-8 character, so
  no `[UNK]` can ever be emitted
- Training corpus: official `train` split only, balanced round-robin over the six
  languages with am/ha/sw/yo oversampled x2; no external corpus and no pre-trained tokenizer
- Post-processor: none | Decoder: ByteFallback
- Built with `tokenizers==0.22.1`

## Results (official validation split, official metric)

| Language | Fertility | UNK rate | Score |
|---|---:|---:|---:|
| English | 1.8523 | 0.000000 | 1.8523 |
| French | 1.9320 | 0.000000 | 1.9320 |
| Hausa | 1.5847 | 0.000000 | 1.5847 |
| Swahili | 1.7606 | 0.000000 | 1.7606 |
| Yoruba | 1.7565 | 0.000000 | 1.7565 |
| Amharic | 2.2419 | 0.000000 | 2.2419 |

- **Score (mean of ha, sw, yo, am): 1.8359** — baseline BPE 10k 2.0600, i.e. a gain of +0.2241 (10.9 %)
- Context guardrail EN/FR: **PASS** (budget 2.1113, en 1.8523, fr 1.9320)
- UNK emitted on validation: 0

## Files

- `tokenizer.json` — the submitted tokenizer
- `metadata.yml` — team metadata
- `notebook.ipynb` — the notebook that built this tokenizer (`notebooks/02_optimization_sweep.ipynb`)
- `README.md` — this file
