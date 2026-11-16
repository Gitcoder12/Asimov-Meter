---
name: source-to-observation
description: Extract structured AI/robotics impact observations from papers, reports or datasets into Asimov-Meter. Use when deciding whether a source supports a numeric ledger record.
---

# source-to-observation

## Procedure
1. Read the relevant full source section, tables, captions, footnotes, methods and limitations; do not rely on an abstract alone.
2. Record the exact title, authors, publication type/status, year, DOI or stable URL, page/table/figure locator and access date in research notes. If the schema lacks a field, do not hide it in an unrelated column.
3. Extract the system/intervention, sector, exact indicator definition, value, unit, period, population/scope and study method.
4. Assign direction (benefit, harm, mixed, unknown) from the source's stated outcome, not the desired narrative.
5. Preserve baseline/comparator information. Distinguish percentage from percentage points, relative from absolute change, counts from rates and benchmark scores from real-world outcomes.
6. If a numeric value is not directly reported or cannot be calculated unambiguously, do not invent it. Keep qualitative findings in separate source notes.
7. Default to `verification: reported`. Only a human who inspected the source may mark a record independently verified.
8. Confirm the source URL and locator point to the exact work. Never invent a DOI.

## Extraction gate
Produce a field-by-field table with the extracted value, exact source location and ambiguity. Stop if unit, population, method or period is unclear. A numeric ledger record requires a supported value, unit, population, period, method and source locator.

## Reject
Do not create a record from an unsupported estimate, uncited statement, marketing claim, abstract-only inference or incomparable metric.
