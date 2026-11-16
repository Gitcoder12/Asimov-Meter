# Asimov-Meter — Skills Index

Read root `AGENTS.md` first, then load the skill that matches the task.

## `source-to-observation`

Extract structured AI/robotics impact observations from papers, reports or datasets into Asimov-Meter. Use when deciding whether a source supports a numeric ledger record.

- Canonical instructions: [`.agents/skills/source-to-observation/SKILL.md`](.agents/skills/source-to-observation/SKILL.md)
- Claude Code discovery entry: [`.claude/skills/source-to-observation/SKILL.md`](.claude/skills/source-to-observation/SKILL.md)

## `evidence-quality-review`

Audit source provenance and methodological strength. Use when checking a source, verification label, causal claim, sample definition, study limitation or conflicting result.

- Canonical instructions: [`.agents/skills/evidence-quality-review/SKILL.md`](.agents/skills/evidence-quality-review/SKILL.md)
- Claude Code discovery entry: [`.claude/skills/evidence-quality-review/SKILL.md`](.claude/skills/evidence-quality-review/SKILL.md)

## `comparability-and-trend-analysis`

Analyze observations without combining incompatible units, populations or methods. Use for summaries, comparisons, trends and dashboard design.

- Canonical instructions: [`.agents/skills/comparability-and-trend-analysis/SKILL.md`](.agents/skills/comparability-and-trend-analysis/SKILL.md)
- Claude Code discovery entry: [`.claude/skills/comparability-and-trend-analysis/SKILL.md`](.claude/skills/comparability-and-trend-analysis/SKILL.md)


## Required workflow
1. Inspect existing implementation, data and tests.
2. State assumptions; stop rather than invent missing facts.
3. Make a minimal patch with regression tests.
4. Run and report exact checks.
5. Update docs and status only when evidence supports the change.

## Discovery locations
- Codex/repository agents: `.agents/skills/<skill-name>/SKILL.md`.
- Claude Code: `.claude/skills/<skill-name>/SKILL.md`.
- Other models: read this index and open the canonical skill. Claude entries are short pointers to canonical text; keep paths synchronized.

## `multi-agent-review-handoff`

Coordinate paper research, evidence extraction, implementation, independent methodological review and verification for Asimov-Meter. Use for source ingestion, schema or analysis changes.

- Canonical: [`.agents/skills/multi-agent-review-handoff/SKILL.md`](.agents/skills/multi-agent-review-handoff/SKILL.md)
- Claude discovery: [`.claude/skills/multi-agent-review-handoff/SKILL.md`](.claude/skills/multi-agent-review-handoff/SKILL.md)
