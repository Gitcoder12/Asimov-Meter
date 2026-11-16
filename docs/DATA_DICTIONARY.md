# Data dictionary

Each JSON object in `data/observations.json` is one sourced numeric observation.

| Field | Meaning | Example form (illustrative only) |
|---|---|---|
| `id` | Stable unique record identifier | UUID |
| `system` | AI/robotics system or intervention being studied | Research system name |
| `sector` | Application domain | `education`, `healthcare`, `manufacturing` |
| `indicator` | Exact measured outcome; keep definitions consistent | `task_completion_rate_change` |
| `direction` | Reported direction: benefit, harm, mixed or unknown | `mixed` |
| `value` | Numeric value as reported | `4.2` |
| `unit` | Unit exactly corresponding to value | `percentage_points` |
| `period_start`, `period_end` | Measurement period in ISO `YYYY-MM-DD` | `2025-01-01` |
| `population` | People, tasks, devices or other scope measured | Cohort description |
| `method` | Study design or measurement method | Randomized trial, survey, benchmark, audit |
| `source_url` | URL to the source supporting this observation | Publisher or official report URL |
| `verification` | Human-entered evidence status | `reported` or `independently_verified` |
| `notes` | Limitations, baseline, context, extraction notes | Free text |
| `recorded_at` | UTC timestamp when record was entered | ISO-8601 timestamp |

## Naming guidance

- Use stable snake_case indicator identifiers.
- Store units explicitly; do not encode units only in the indicator name.
- Include enough population detail to avoid combining unlike cohorts.
- State whether a value is absolute, relative, percentage or percentage-point change in the indicator/unit definitions.
- Keep study-specific caveats in notes and cite the source.
