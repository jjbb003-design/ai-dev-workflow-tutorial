# ShopSmart dashboard project instructions

This is Joseph Barragan's Phase 1 LMU AI Dev Workflow Tutorial. The original tutorial is preserved in `TUTORIAL.md`; requirements are in `prd/ecommerce-analytics.md`. Use the supplied public sample CSV only. Keep Meridian client data out of this project.

## Files and commands

- `sales.py`: CSV validation, KPI totals, monthly aggregation, category/region rankings.
- `app.py`: Streamlit presentation and Plotly charts.
- `data/sales-data.csv`: unchanged upstream public sample.
- `tests/`: fixture-based calculations, malformed data, and app smoke checks.
- `TASKS.md`: versioned milestone board and evidence.
- `docs/superpowers/`: approved design and plan.

Create a plain environment with `python -m venv venv`. Install with `python -m pip install -r requirements-dev.txt` after activating it. Run `python -m pytest -q` and `streamlit run app.py`. On Windows, activation is `venv\Scripts\Activate.ps1`; on macOS/Linux use `source venv/bin/activate`.

## Lessons and constraints

These are agent-observed lessons, not invented student reflections:

- The CSV contains 482 unique orders totaling $116,500.21. The PRD's rounded total is not the exact control total.
- The sample uses one row per order. Reject duplicates instead of assuming future line-item data uses the same contract.
- Parse dates before grouping and keep monthly output chronological. Horizontal chart order must explicitly put the largest bar at the top.
- Validate invalid data; do not silently coerce it into dropped rows and understated totals.
- Loading is relative to the app file, not the shell's current directory.
- Keep filters and databases out of Phase 1. The data is static, so do not claim real-time updates.
- Run the full test suite after changes and visually check chart labels. AppTest alone cannot establish visual quality or cross-browser compatibility.
- Never claim Joseph performed an agent-run check. Record actual student decisions separately.
