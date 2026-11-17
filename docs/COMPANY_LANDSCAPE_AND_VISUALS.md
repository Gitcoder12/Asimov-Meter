# Asimov-Meter — company landscape, mind maps and evidence charts

## Company and product landscape

The sourced product directory lives in data/company_landscape.json. It includes OpenAI, Anthropic, Google DeepMind, NVIDIA, Boston Dynamics, Figure and Neuralink. Each product entry includes an official source link and is a factual catalogue only: no ranking, safety certification, market-share claim or efficacy claim is inferred.

## Mind map

Generate the Mermaid mind map from the catalogue:

    python tools/render_company_mindmap.py

This shows company → sector → products. It is a directory, not a performance comparison.

## Charts

Numeric charts are generated only for compatible observations. The compatibility key is system, sector, indicator, unit, population and method. A trend chart rejects mixed units or methods rather than normalizing them silently.

Recommended visual layers:
- Company/product mind map: organizations and their public products/services.
- Evidence graph: source → extracted observation → reviewer → verification status.
- Trend chart: one compatible measurement series over time.
- Benefit/harm/unknown distribution: separate counts; missing values remain missing.
- Evidence coverage: sectors and products with no record are labelled "unknown", never zero.

## Asimov-Meter interpretation limits

The ledger remains the source of measured impact observations. Product catalogues are not evidence that a product produces benefit or harm. No global AI goodness score is introduced. Association is not causation; independent verification remains a human review label.
