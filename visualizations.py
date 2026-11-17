"""Evidence-preserving visual helpers for Asimov-Meter."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


def load_company_catalogue(path: Path) -> dict[str, Any]:
    """Load a versioned product catalogue and verify required source links."""
    catalogue = json.loads(path.read_text(encoding="utf-8"))
    if catalogue.get("schema_version") != "1.0":
        raise ValueError("unsupported company catalogue schema_version")
    companies = catalogue.get("companies")
    if not isinstance(companies, list) or not companies:
        raise ValueError("catalogue companies must be a non-empty array")
    names: set[str] = set()
    for company in companies:
        name = company.get("company") if isinstance(company, dict) else None
        products = company.get("products") if isinstance(company, dict) else None
        if not isinstance(name, str) or not name.strip() or name in names:
            raise ValueError("company names must be non-empty and unique")
        names.add(name)
        if not isinstance(products, list):
            raise ValueError(f"{name}: products must be an array")
        for product in products:
            if (
                not isinstance(product, dict)
                or not isinstance(product.get("name"), str)
                or not product["name"].strip()
                or not isinstance(product.get("source_url"), str)
                or not product["source_url"].startswith(("https://", "http://"))
            ):
                raise ValueError(f"{name}: each product needs a name and HTTP(S) source_url")
    return catalogue


def _mermaid_safe(label: str) -> str:
    return re.sub(r"[\[\]{}()#]", "", label).replace('"', "'").strip()


def company_mindmap(catalogue: dict[str, Any]) -> str:
    """Render a Mermaid mind map from sourced company/product catalogue data."""
    lines = ["mindmap", "  root((AI + Robotics Landscape))"]
    for company in catalogue["companies"]:
        lines.append(f"    {_mermaid_safe(company['company'])}")
        lines.append(f"      {_mermaid_safe(company.get('sector', 'Unclassified'))}")
        for product in company["products"]:
            lines.append(f"        {_mermaid_safe(product['name'])}")
    return "\n".join(lines)


def compatible_trend_chart(observations: list[dict[str, Any]]) -> str:
    """Render a Mermaid xychart only for one comparable series.

    Compatibility requires identical system, sector, indicator, unit, population
    and method. The function never normalizes or combines unlike measurements.
    """
    if not observations:
        raise ValueError("at least one observation is required")
    keys = ("system", "sector", "indicator", "unit", "population", "method")
    baseline = tuple(observations[0].get(key) for key in keys)
    if any(not value for value in baseline):
        raise ValueError("observations are missing comparability metadata")
    for observation in observations[1:]:
        if tuple(observation.get(key) for key in keys) != baseline:
            raise ValueError("cannot chart observations with different comparability fields")
    rows = sorted(observations, key=lambda item: item["period_start"])
    labels = [str(item["period_start"]) for item in rows]
    values = []
    for item in rows:
        value = item.get("value")
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError("chart values must be numeric")
        values.append(float(value))
    x_labels = ", ".join(json.dumps(label) for label in labels)
    y_values = ", ".join(f"{value:g}" for value in values)
    title = _mermaid_safe(f"{baseline[0]} - {baseline[2]} ({baseline[3]})")
    return (
        "xychart-beta\n"
        f'  title "{title}"\n'
        f"  x-axis [{x_labels}]\n"
        f'  y-axis "{_mermaid_safe(baseline[3])}"\n'
        f"  line [{y_values}]"
    )
