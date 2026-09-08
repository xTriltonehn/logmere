# logmere

Opinionated log housekeeping tool with dry-run support

## Getting started

```bash
pip install -r requirements.txt
python -m logwash --help
```

## Usage

```bash
# show what would be cleaned, change nothing
logwash ./logs --older-than 30 --dry-run

# archive logs older than 30 days
logwash ./logs --older-than 30 --archive ./backup
```

## What it does

- Archive matched logs into a timestamped .tar.gz
- Filter by age (--older-than) or size (--larger-than)
- Scan directories for log files by glob pattern
- Dry-run mode shows what would happen, touches nothing
- Exit codes friendly for cron and CI

## Project structure

```text
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   └── bug_report.md
│   └── workflows/
│       └── ci.yml
├── docs/
│   ├── configuration.md
│   ├── development.md
│   └── usage.md
├── examples/
│   └── quickstart.md
├── logwash/
│   ├── __init__.py
│   ├── __main__.py
│   ├── cli.py
│   └── utils.py
├── tests/
│   └── test_cli.py
├── .editorconfig
├── .gitattributes
├── .gitignore
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── pyproject.toml
└── requirements.txt
```

## Changelog

- `0.1.1` - fix edge case in argument parsing
- `0.1.0` - first working version

## License

MIT licensed, see LICENSE.
