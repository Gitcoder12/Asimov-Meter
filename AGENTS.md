# Asimov-Meter — Agent Engineering Contract

## Mission
An evidence-first ledger for sourced observations about AI and robotics impacts over time. It is descriptive infrastructure, not a universal AI score or causal-inference engine.

## Codebase map
`asimov_meter.py` validates observations, stores the local JSON ledger, groups compatible records and exports CSV. `data/observations.json` is intentionally empty. The JSON Schema, methodology, data dictionary and tests define current behavior.

## Before every task
1. Read this file, `SKILLS.md`, `PROJECT_STATUS.md` and the relevant skill.
2. Inspect the current branch, working tree and relevant files; do not trust stale summaries.
3. Trace callers, data flow, tests and documentation before editing.
4. State the problem, expected behavior, files at risk, assumptions and verification plan.
5. Prefer the smallest coherent, reviewable patch.

## Non-negotiable invariants
- Never invent observations, numbers, units, populations, study methods, authors, DOI values or source URLs.
- Keep the initial ledger empty unless the user supplies or approves source-derived records.
- A syntactically valid URL has not thereby been fetched, read, authenticated or independently verified.
- The independently_verified label is human-entered. Agents must never promote it automatically.
- Do not pool measurements across system, sector, indicator, unit, population or method; even matching keys do not prove scientific comparability.
- Association, before/after change and descriptive statistics do not by themselves establish causality.
- Missing values are not zero. Preserve null, unavailable and unreported as distinct states when extending the schema.

## Verification commands
- `python -m unittest discover -s tests -v`
- `python -m py_compile asimov_meter.py tests/test_asimov_meter.py`
- `python asimov_meter.py --help`
- `python asimov_meter.py list`
- `python asimov_meter.py report`

Run relevant checks after edits. If an environment prevents a command, mark it **not run**; do not infer success. Add regression tests for behavior changes and inspect the actual generated outputs.

## Engineering standards
- Use type hints, cohesive functions and explicit input validation.
- Keep deterministic behavior wherever possible.
- Minimize dependencies; justify additions by correctness, maintenance and licensing.
- Avoid hidden network access, telemetry, background work and mutable global state.
- Preserve provenance and source data. Guard destructive writes.
- Do not fabricate data, benchmark numbers, scientific claims or product capabilities.
- Keep error messages actionable without leaking secrets or private data.

## Documentation standards
Update README, examples and `PROJECT_STATUS.md` when behavior changes. Clearly distinguish implemented, experimental, planned and unsupported functionality. Never mark a feature complete from a README claim alone.

## Review and delivery
Every handoff must include: what changed, why, files changed, exact commands and actual results, checks not run, limitations, safety/security implications and manual review steps.

Do not edit `main`, merge, force-push, rewrite history or close PRs unless the user explicitly asks. Never claim perfection; state residual uncertainty.

## Skills
Canonical skill instructions are in `.agents/skills/<name>/SKILL.md`. Claude Code discovery wrappers are in `.claude/skills/<name>/SKILL.md`. See `SKILLS.md`.