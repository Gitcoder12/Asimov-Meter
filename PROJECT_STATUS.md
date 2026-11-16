# Project Status — Asimov-Meter

**Updated:** 2026-11-16  
**Current stage:** Evidence-ledger CLI MVP  
**Verification scope:** Local tests and CLI smoke checks; no external impact data has been collected.

## Implemented

- Append observations to a local JSON ledger with unique IDs and UTC entry timestamps.
- Capture system, sector, indicator, direction, numeric value, unit, measurement period, population, method, source URL and verification label.
- Validate dates, finite numeric values, non-empty metadata and HTTP(S) source URLs.
- Reject duplicate observation IDs when loading a ledger.
- Produce descriptive summaries separated by system, sector, indicator, unit, population and method.
- Export observations to CSV.
- Keep the starting ledger empty; no impact findings or example statistics are fabricated.
- Include JSON Schema, data dictionary, methodology guide and a blank example template.

## Not implemented

- Global AI-impact score or cross-domain normalization.
- Causal inference or automatic study-quality assessment.
- Automatic collection, scraping, monitoring or forecasting.
- Automatic source verification, retraction tracking or deduplication across papers.
- Dashboard or policy recommendations.

## Known limitations

- `independently_verified` is a human-entered label, not an automated or cryptographic verification result.
- Shared indicator names and units do not guarantee scientific comparability. Groups are also separated by population and method, but researchers must still inspect study definitions and limitations.
- The tool is descriptive and does not establish causality.

## Next steps

1. Add source-review metadata (reviewer, checked date and evidence notes).
2. Add optional sample-size and uncertainty fields with clear definitions.
3. Add reproducible report snapshots and export provenance.
4. Consider visual trend views only after enough compatible, sourced observations exist.

## Verification

Run `make check` or `python -m unittest discover -s tests -v`. The CI workflow covers Python 3.10–3.13. CI results should be checked after the initial GitHub push.
