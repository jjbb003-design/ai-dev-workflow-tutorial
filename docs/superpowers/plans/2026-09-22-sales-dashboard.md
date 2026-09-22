# ShopSmart Dashboard Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans inline, task-by-task. No subagents, consistent with the course's explicit execution instructions.

**Goal:** Deliver and verify the Phase 1 ShopSmart dashboard for Joseph Barragan.

**Architecture:** `sales.py` validates and aggregates the public CSV; `app.py` displays the results with Streamlit and Plotly. Tests check computations separately from rendering.

**Tech Stack:** Python 3.11+, pandas, Plotly, Streamlit, pytest, plain `venv/` and `requirements.txt`.

**Spec:** [Sales dashboard design](../specs/2026-09-22-sales-dashboard-design.md), approved by Joseph in conversation September 22, 2026.

## Global constraints

- Work in this separate tutorial repo on `codex/sales-dashboard`; retain the upstream tutorial.
- Use only `data/sales-data.csv`, not Meridian records.
- Display two KPI cards and three charts. No out-of-scope filters or databases.
- Separate calculations from UI; write calculation tests before implementation.
- Maintain `TASKS.md` with milestone status, acceptance criteria, evidence, and real commit hashes.
- GitHub and Streamlit account authorization must be completed by Joseph where required. Never claim deployment is done before checking its public URL.

## Review focus

- Missing, empty, or malformed CSV: display a clear error rather than misleading zero metrics.
- Duplicate order IDs: reject duplicates under this sample's one-row-per-order contract.
- Invalid dates or nonfinite sales: reject them instead of silently dropping rows.
- Unsorted input: months must remain chronological; bars must descend by sales.
- Totals: all three chart aggregations must reconcile with the displayed sales KPI.

## Task 1 — TASK-1: Setup and data loading

Files: `requirements.txt`, `requirements-dev.txt`, `sales.py`, `tests/test_sales.py`, `app.py`, `TASKS.md`.

Interface: `load_sales(path: Path) -> pandas.DataFrame`; required columns `date`, `order_id`, `category`, `region`, `total_amount`; normalize dates and sales numeric types.

- [ ] Create a five-milestone board from the PRD and mark TASK-1 in progress.
- [ ] Create `venv/`, install pandas/Streamlit/Plotly and pytest, and record tested dependency versions.
- [ ] Write fixture tests for a three-row valid CSV and missing file, missing column, empty input, invalid date, blank categories, negative/nonfinite amounts, and duplicate order IDs. Expect explicit `ValueError` or `FileNotFoundError`; observe failure before implementation.
- [ ] Implement validation with explicit messages and add a title-only app that catches load errors and stops.
- [ ] Run `venv/Scripts/python -m pytest -q`, launch `streamlit run app.py`, then commit with TASK-1 and record its hash.

## Task 2 — TASK-2: KPI cards

Files: `sales.py`, `tests/test_sales.py`, `app.py`, `TASKS.md`.

Interface: `calculate_kpis(df) -> tuple[float, int]` returns summed amount and transaction count.

- [ ] Write a test with amounts 20, 5, and 10, expecting sales 35 and orders 3. Observe its failure.
- [ ] Implement the calculation and two formatted `st.metric` cards; currency has two decimals and counts use separators.
- [ ] Run tests and app smoke check, commit with TASK-2, update board.

## Task 3 — TASK-3: Monthly trend

Files: `sales.py`, `tests/test_sales.py`, `app.py`, `TASKS.md`.

Interface: `monthly_sales(df) -> DataFrame` with `date`, `total_amount` columns.

- [ ] Test out-of-order dates across January and February with January totaling 15 and February 20. Assert chronological dates and reconciliation to 35. Observe failure.
- [ ] Implement month-start aggregation and a Plotly line chart with date x-axis, sales y-axis, markers, and currency tooltips.
- [ ] Run tests, visually inspect the trend, commit with TASK-3, update board.

## Task 4 — TASK-4: Category and region breakdowns

Files: `sales.py`, `tests/test_sales.py`, `app.py`, `TASKS.md`.

Interface: `sales_by(df, column) -> DataFrame`, permitting only `category` or `region`, descending by amount with alphabetical tie breaking.

- [ ] Test fixture category totals A=25/B=10 and region East=30/West=5, including descending order and reconciliation. Observe failure.
- [ ] Implement grouping and side-by-side horizontal Plotly bar charts, largest at top, all labels visible.
- [ ] Run tests, inspect bars and hover values, commit with TASK-4, update board.

## Task 5 — TASK-5: Verification and deployment

Files: `tests/test_app.py`, `AGENTS.md`, `TASKS.md`, `README.md`.

- [ ] Independently calculate CSV control totals with standard-library CSV and Decimal; compare to the app and chart aggregates.
- [ ] Run Streamlit AppTest; require no exceptions, two metrics, and three charts. Run the full pytest suite.
- [ ] Open the live local app and inspect title, KPI values, chart ordering, labels, and tooltips. Record the tested browser and timing limitations.
- [ ] Write project instructions, run/redeploy directions, provenance, and lessons; preserve the upstream README as `TUTORIAL.md` before replacing the root landing page.
- [ ] Review the branch against the PRD, fix substantive findings, and record actual review limitations. Commit with TASK-5.
- [ ] Publish to Joseph's `ai-dev-workflow-tutorial` GitHub repository on main. Verify code and board arrived.
- [ ] Deploy main/app.py to Streamlit Community Cloud after account authorization, open the public URL, verify all charts, and record the URL and real completion status.

## Plan self-review and approval

Codex checked coverage against the approved design and PRD: all five functional requirements, separate calculations, tests, readable source, versioned board, and deployment are covered. Each computation has independently calculated fixture expectations. Chart presentation additionally requires a visual check. Joseph approved this saved plan and inline execution on September 22, 2026, before the build began.

