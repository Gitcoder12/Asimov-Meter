"""Print a Mermaid mind map for the sourced AI/robotics company catalogue."""

from pathlib import Path

from visualizations import company_mindmap, load_company_catalogue

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    catalogue = load_company_catalogue(ROOT / "data" / "company_landscape.json")
    print(company_mindmap(catalogue))


if __name__ == "__main__":
    main()
