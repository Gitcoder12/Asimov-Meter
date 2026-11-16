---
name: evidence-quality-review
description: Audit source provenance and methodological strength. Use when checking a source, verification label, causal claim, sample definition, study limitation or conflicting result.
---

# evidence-quality-review

## Review dimensions
1. Source identity and publication status: journal, conference, preprint, official dataset, technical report, news or vendor material.
2. Primary evidence versus secondary summary.
3. Study design: randomized experiment, quasi-experiment, observational study, benchmark, survey, case study or descriptive report.
4. Population, sample size, inclusion criteria and representativeness where reported.
5. Outcome definition, measurement instrument, baseline and comparator.
6. Missingness, uncertainty intervals, statistical analysis and confounders.
7. Funding/conflicts of interest and disclosed limitations.
8. Retraction, correction and version status when verifiable.

## Label discipline
- `reported` means transcribed from a source but not independently checked by the maintainer.
- `independently_verified` is an explicit human review state, not a quality grade, truth guarantee or causal-validity claim.
- Agents may recommend human review but must never change this field automatically.

## Claim discipline
Correlation is not causation. Benchmark improvement is not necessarily real-world impact. A survey is not automatically representative. Vendor-reported productivity is not independent evidence. A preprint is not peer-reviewed merely because it has a DOI.

## Output
Write a concise audit note: supported claim, source locator, study design, limitations, unknowns/conflicts, verification recommendation and exact proposed correction. Preserve original records until a human approves edits.
