# ShopSmart sales dashboard design

Prepared for Joseph Barragan, September 22, 2026. Status: approved by Joseph Barragan in conversation on September 22, 2026.

## Purpose

Implement Phase 1 of the supplied [PRD](../../../prd/ecommerce-analytics.md): an executive dashboard displaying total sales, order count, a monthly sales line chart, and descending category and region bar charts from the supplied public CSV. The tutorial is separate from the Meridian wiki and contains no Meridian client data.

## Design

Use Streamlit, pandas, and Plotly with Python 3.11 or later. Keep CSV validation and calculations in `sales.py`, presentation in `app.py`, and meaningful calculation tests in `tests/test_sales.py`. Install dependencies in `venv/` using `requirements.txt`; use no uv or conda. Run with `streamlit run app.py` from the project directory.

Recommended layout: a clear ShopSmart title, sample-data period, two KPI cards, full-width monthly trend, and two side-by-side horizontal bar charts. Hover labels show precise currency values. Blue/teal colors and descriptive titles make the page readable without extra controls. Alternatives considered: native Streamlit charts reduce dependencies but give less formatting control; filters add interaction but are explicitly out of Phase 1 scope.

## Data behavior

Read `data/sales-data.csv` relative to the app file, so working-directory differences do not break loading. Validate required columns, valid dates, numeric finite nonnegative sales, nonblank order/category/region values, and one row per unique order ID. The sample schema defines one transaction per order; reject duplicate IDs rather than silently double count. Display a useful error and stop on malformed/missing/empty files.

Total Sales is the sum of `total_amount`; Total Orders is the number of validated transaction rows. Trend aggregates by calendar month, sorted chronologically; category and region aggregate the same amounts and sort descending. Tests reconcile every grouping to the overall sum and use a small independent fixture with hand-calculated expectations.

## Scope and quality

No login, database, real-time claims, filtering, exports, or Meridian records. Clearly identify the static tutorial data. Test missing/invalid input, order counts, chronological aggregation, sorting, and reconciliation. Run Streamlit's AppTest and inspect the rendered page for two metrics and three charts. Check measured load behavior and document any unverified browser compatibility.

## Delivery

Track five milestones in `TASKS.md`: setup/loading, KPIs, trend, breakdowns, and validation/deployment. Each code commit includes its milestone ID and the board records the commit. Preserve the upstream tutorial material. Publish the completed code to Joseph's public `ai-dev-workflow-tutorial` repository, then deploy `main` / `app.py` on Streamlit Community Cloud and verify the public URL and charts. Account authorization remains a user step when required.

## Review

Codex checked this design against Phase 1 and the tutorial's requirements for separate calculations, pytest, plain venv, inline execution, and milestone traceability. Joseph approved this written design before the implementation plan was created.

