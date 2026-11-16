# Asimov-Meter

**An evidence-first ledger for tracking observed AI and robotics impacts over time.**

Asimov-Meter records sourced observations about benefits, harms, mixed outcomes and unknown effects. It helps researchers ask: *what was measured, for whom, over what period, using which method, and where is the evidence?*

It deliberately does **not** calculate a universal score for whether AI is good or bad. It does not infer causality from unrelated studies, invent missing measurements or automatically decide whether a source is trustworthy.

## Current MVP

- Add, list and export observations from a local JSON ledger.
- Capture system, sector, indicator, direction, numeric value, unit, period, population, method, source URL and verification label.
- Validate dates, numbers, required metadata and HTTP(S) source links.
- Summarize only compatible groups: same system, sector, indicator, unit, population and method.
- Keep `reported` separate from `independently_verified` (a human review label, not an automatic verification result).
- Start with an empty ledger. No impact metrics or sample findings are preloaded.

## Repository structure

```text
Asimov-Meter/
├── .github/workflows/tests.yml
├── data/
│   ├── observations.json
│   └── observation.schema.json
├── docs/
│   ├── DATA_DICTIONARY.md
│   └── METHODOLOGY.md
├── examples/
│   └── observation-template.json
├── tests/
│   └── test_asimov_meter.py
├── asimov_meter.py
├── Makefile
├── pyproject.toml
├── LICENSE
├── .gitignore
└── README.md
```

## Requirements

- Python 3.10 or later
- No third-party runtime dependencies

## Run from source

```bash
python asimov_meter.py --help
python asimov_meter.py list
python asimov_meter.py report
```

Add one observation (replace every value with information from a real source you have inspected):

```bash
python asimov_meter.py add \
  --system "System name" \
  --sector education \
  --indicator completion_rate_change \
  --direction benefit \
  --value 4.2 \
  --unit percentage_points \
  --period-start 2025-01-01 \
  --period-end 2025-03-31 \
  --population "Describe the measured population" \
  --method "Describe the study design" \
  --source-url https://example.org/report \
  --verification reported
```

The command above is a **usage template**, not an actual study result. Do not record it as evidence.

Export observations:

```bash
python asimov_meter.py export-csv exports/observations.csv
```

Use a separate ledger by placing `--ledger path/to/ledger.json` before the subcommand. The default ledger is `data/observations.json`.

Run tests:

```bash
python -m unittest discover -s tests -v
```

## Data and evidence rules

1. Every observation must link to a source and state the measurement method, population/scope, unit and time period.
2. Preserve the original source and extraction notes where licensing permits.
3. `independently_verified` means a human reviewer inspected the source and checked the extraction. The software does not fetch or verify the source.
4. Do not compare unlike indicators, units, populations or methods. A shared label alone does not guarantee that two studies are scientifically comparable.
5. Descriptive association is not causal evidence. Confounders and study limitations belong in the notes/source review.
6. Missing data stays missing. Never fill gaps with generated or guessed values.

See [Methodology](docs/METHODOLOGY.md) and [Data dictionary](docs/DATA_DICTIONARY.md) before entering research records.

## Not implemented

Automatic web collection, causal inference, cross-domain normalization, prediction, policy recommendations, dashboards, source-credibility scoring and a global AI-impact index are deliberately outside this first MVP.

## Working with coding agents

Start with [`AGENTS.md`](AGENTS.md) for repository-wide invariants, architecture, commands and review rules. Use [`SKILLS.md`](SKILLS.md) to select a task-specific workflow. Canonical skills are stored in `.agents/skills/`; Claude Code discovery entries are stored in `.claude/skills/`. Read the relevant skill before changing domain logic. All agent output remains subject to human review; documentation and tests do not replace scientific, operational or safety validation.
