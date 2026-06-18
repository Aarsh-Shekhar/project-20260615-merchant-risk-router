# Merchant Risk Router

Routes synthetic merchant cases by risk and impact.

## What it includes

- deterministic sample data
- scoring and ranking logic
- command line report
- unit tests
- continuous validation workflow

## Run

```bash
python3 -m merchant_risk_router.cli --input data/sample_merchants.json
```

## Test

```bash
python3 -m unittest discover tests
```
