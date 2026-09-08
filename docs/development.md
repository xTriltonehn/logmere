# Development

## Setup

```bash
pip install -r requirements.txt
python -m logwash --help
```

## Tests

```bash
python -m pytest -q
```

## Conventions

- functions stay small; extract early
- comments explain *why*, not *what*
- no new dependencies without a good reason
