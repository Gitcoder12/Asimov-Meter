# Methodology and interpretation

## Unit of analysis

One record represents one reported measurement from one source, for one named AI/robotics system or intervention, one indicator, one population/scope and one measurement period.

Do not turn a paper's narrative conclusion into a numeric record unless the paper reports a specific measurement that can be captured with a clear unit and scope. Qualitative findings can be preserved in source notes outside the numeric summary rather than assigned an invented number.

## Evidence status

- `reported`: the observation is transcribed from a cited source but has not been independently checked by the maintainer.
- `independently_verified`: a human reviewer has inspected the source and checked the extraction. This is still a user-entered provenance label; the application does not authenticate reviewers, access publisher databases or verify the evidence automatically.

Keep a record `reported` when uncertain. Never promote a record just because its URL resolves.

## Direction

- `benefit`: the source reports a beneficial direction for the specified outcome.
- `harm`: the source reports an adverse direction.
- `mixed`: the source reports meaningful benefits and harms, or mixed direction depending on subgroup/context.
- `unknown`: direction is not established from the source.

Direction is a qualitative label. It is not a score or effect-size adjustment.

## Comparability

The report groups records by system, sector, indicator, unit, population and method. This is a conservative safeguard, not proof of comparability. Researchers must still inspect definitions, sample design, baseline, measurement instrument, confounders and study limitations before interpreting a mean or trend.

Do not average values with different units. Do not combine percentage and percentage-point changes. Keep relative risk, odds ratios, raw counts, rates and model-reported scores distinct.

## Causality

A before/after comparison, correlation or observational association does not by itself prove that an AI system caused the measured change. Record the study design and source limitations. Strong causal claims require a design and analysis that support them.

## Missing and negative findings

Do not replace missing data with zero. Zero is a measured value; missing means no usable value was reported. Preserve adverse findings and null results. Do not omit findings solely because they conflict with a desired narrative.

## Limitations of this MVP

The application does not assess source quality, detect retractions, deduplicate studies, normalize indicators across domains, estimate causal effects or validate reported results. Human literature review remains essential.
