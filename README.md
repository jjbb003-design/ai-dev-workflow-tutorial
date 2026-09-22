# ShopSmart sales dashboard

Joseph Barragan's AI Dev Workflow Tutorial: a Streamlit dashboard using the course's public sample CSV. It shows total sales, total orders, monthly sales, and descending category and region breakdowns.

**Verified sample totals:** $116,500.21 · 482 orders · five categories · four regions. Static 2024 sample data, not live business reporting.

## Run locally

Requires Python 3.11 or later.

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
python -m pytest -q
streamlit run app.py
```

On macOS/Linux activate with `source venv/bin/activate`. Runtime dependencies are pinned in `requirements.txt`; pytest is separate.

## How it works

`sales.py` validates inputs and calculates metrics. `app.py` displays results with Streamlit and Plotly. Tests use hand-calculated fixtures and an independent CSV/Decimal control total. Invalid files produce an error rather than understated totals. The sample assumes one row per order and rejects duplicate IDs.

## Project record

- [Task board](TASKS.md)
- [Approved design](docs/superpowers/specs/2026-09-22-sales-dashboard-design.md)
- [Approved plan](docs/superpowers/plans/2026-09-22-sales-dashboard.md)
- [Original tutorial](TUTORIAL.md)
- [Product requirements](prd/ecommerce-analytics.md)
- [Project instructions and lessons](AGENTS.md)

## Deployment and verification

Deploy this repository's `main` branch and `app.py` on [Streamlit Community Cloud](https://share.streamlit.io/). Dependencies come from `requirements.txt`. Live dashboard: [ShopSmart — Joseph Barragan](https://shopsmart-joseph-barragan.streamlit.app/).

Current state: deployed and verified September 22, 2026; 19 tests pass. Codex visually checked the live dashboard in the in-app Chromium browser: $116,500.21, 482 orders, monthly trend, five categories, and four regions. Anonymous HTTP access returned 200. Firefox/Safari and cold-cloud startup timing have not been verified. AppTest emits a bare-mode context warning from its testing harness; the app itself has no displayed error or exception.

Source: [LMU tutorial](https://github.com/LMU-ISBA/ai-dev-workflow-tutorial). Original tutorial and public data are retained. Joseph supplied design and plan approvals. Codex performed the automated and visual checks; they are not represented as Joseph's independent review.
