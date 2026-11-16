---
name: comparability-and-trend-analysis
description: Analyze observations without combining incompatible units, populations or methods. Use for summaries, comparisons, trends and dashboard design.
---

# comparability-and-trend-analysis

## Comparability gate
Check system/intervention identity and version, sector/use case, indicator definition and direction, unit/denominator, population/geography, method/baseline/period and measurement instrument. The current CLI grouping keys are a minimum guardrail, not scientific proof of comparability.

## Allowed summaries
Descriptive counts, ranges and means only within documented compatible groups. Show observation count, number of sources, period, verification-label counts and limitations.

## Prohibited summaries
- No universal AI score assembled from unrelated metrics.
- No averaging percentages, percentage points, counts, rates, currency and benchmark scores together.
- No missing-to-zero conversion.
- No treating a higher value as a benefit without understanding indicator direction.
- No forecasts or causal explanations from the descriptive ledger.

## Trend workflow
1. Inspect chronological coverage and missing periods.
2. Check whether definitions and measurement methods remain stable.
3. Identify source dependence; several reports may reuse one dataset.
4. Report uncertainty and sample size when present.
5. Separate observed trend from proposed explanations.
6. Compare subgroups only when denominators and definitions support it.

Every table or chart must state indicator, unit, population, method, period, n, source coverage and whether analysis is descriptive or inferential.
