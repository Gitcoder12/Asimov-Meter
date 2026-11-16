---
name: multi-agent-review-handoff
description: Coordinate paper research, evidence extraction, implementation, independent methodological review and verification for Asimov-Meter. Use for source ingestion, schema or analysis changes.
---

# Multi-Agent Review Handoff — Asimov-Meter

## Roles
- **Research lead (for example, Claude):** read primary papers/reports, extract exact source locators, definitions, units, population, study method, period and limitations. Return an evidence table; do not invent missing values or edit the ledger without approval.
- **Implementation engineer (for example, ChatGPT/Codex):** implement schema, CLI, validation, export or reporting changes after the evidence contract is agreed.
- **Independent methodological reviewer (for example, DeepSeek):** read source extracts and code read-only. Challenge unit consistency, population matching, causal overreach, duplicate-source dependence and retraction/version issues.
- **Verifier:** run tests, validate JSON/CSV round-trips and reconcile each output to the source record.
- **Human maintainer:** decides whether source facts are acceptable and whether any observation may be labelled independently verified.

## Required evidence handoff
For every proposed observation include:
- Exact title/authors/publication type and stable source URL/DOI.
- Page/table/figure locator.
- Value, unit, denominator, baseline/comparator and measurement period.
- Population/scope, method, direction and disclosed limitations.
- Ambiguities or fields the source does not report.

If a field is unsupported, keep it unknown or do not create a numeric observation. Never use a language model's paraphrase as the sole evidence for a numeric result.

## Parallel-work rules
- Researcher proposes records; human confirms them.
- Only one writer edits a given ledger/schema file at a time.
- Independent reviewer receives a pinned commit/source set and does not edit it.
- Do not let agents independently change verification labels.
- Resolve disagreements by returning to the primary source and methodology, not by averaging model opinions.

## Release gate
The report states source coverage, exact data changes, validation/test results, unverified fields, methodological caveats and remaining non-comparability. Do not release a universal AI-impact score or causal claim from descriptive summaries.
