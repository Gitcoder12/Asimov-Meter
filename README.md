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

---

## Engineering Audit & Handover — 2026-11-17

**Reviewed commit:** `243f5287e5d9ea37dc0a13f6dbbaf379e2e52b31` (`main`). Static inspection covered the ledger implementation, methodology, data file, and tests; tests were not executed.

### Confirmed findings
- The ledger is intentionally empty (`data/observations.json` contains `[]`); no impact observations or findings are preloaded.
- The implementation validates required metadata, finite numeric values, date ordering, HTTP(S) source URLs, and duplicate observation IDs. Ledger saving uses an atomic temporary-file replacement path.
- The methodology correctly states that `independently_verified` is a human-entered label; the application does not authenticate reviewers or automatically verify sources.
- The methodology also warns that grouping by matching fields does not prove scientific comparability and that observational association does not establish causality.
- The tests cover validation, grouping separation, duplicate IDs, and ledger round-trip behavior. They were not run in this audit.

### Next actions
1. Run the full unittest suite and CI; preserve the exact result.
2. Add a documented human-review workflow and provenance record for who checked each extraction and when.
3. Add benchmark/fixture cases for malformed URLs, Unicode/large notes, export consistency, and interrupted writes.

**Verification status:** static source/test/methodology inspection only; test execution and real evidence-entry workflow remain unverified.


---

## Branch Activity & Development History

**Audit date:** 2026-11-18 · **Comparison base:** `main`

| Branch | Difference from `main` | Observed work / changed paths |
|---|---:|---|
| `docs/agent-guidance-and-skills-20261116` | 0 ahead / 3 behind | No unique commits relative to current `main`; branch is behind |
| `feat/company-landscape-visuals` | 7 / 1 | Company landscape dataset, visualization documentation, rendering tool and visualization tests |
| `feat/evidence-ledger-mvp-20261116` | 0 / 17 | No unique commits relative to current `main`; branch is behind |
| `feat/global-ai-robotics-intelligence-2026-11-16` | 0 / 2 | No unique commits relative to current `main`; branch is behind |

**Verification boundary:** No open PRs were returned by the repository search at audit time. The company landscape branch changes data and visualizations; verify source citations, freshness and rendering tests before merging. No branches have been merged or deleted by this documentation update.
