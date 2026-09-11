# Soumission finale — métrique officielle

*Dataset `Similoluwa/african-multilingual-tokenizer-challenge` @ `v1.0.0` — train : 240,000 textes, validation : 24,000 lignes.*

## Résultat

- **Score (moyenne ha/sw/yo/am) : 1.8359** — baseline 2.0600, gain +0.2241
- Guardrail EN/FR : PASS (budget 2.1113, en 1.8523, fr 1.9320)
- UNK émis sur la validation : 0
- Modèle : `tokenizer.json` (630,664 octets)

## Détail par langue

| Langue | Fertility | UNK rate | Pénalisé |
|---|---:|---:|---:|
| en | 1.8523 | 0.000000 | 1.8523 |
| fr | 1.9320 | 0.000000 | 1.9320 |
| ha | 1.5847 | 0.000000 | 1.5847 |
| sw | 1.7606 | 0.000000 | 1.7606 |
| yo | 1.7565 | 0.000000 | 1.7565 |
| am | 2.2419 | 0.000000 | 2.2419 |

## Configuration

```json
{
  "name": "c12-alph500-bf",
  "model": "bpe",
  "pre": "whitespace_split",
  "min_freq": 5,
  "alphabet": false,
  "limit_alphabet": 500,
  "byte_fallback": true,
  "boost": {
    "ha": 2,
    "sw": 2,
    "yo": 2,
    "am": 2
  }
}
```
