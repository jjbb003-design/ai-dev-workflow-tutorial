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

- [x] Create a five-milestone board from the PRD and mark TASK-1 in progress.
- [x] Create `venv/`, install pandas/Streamlit/Plotly and pytest, and record tested dependency versions.
- [x] Write fixture tests for a three-row valid CSV and missing file, missing column, empty input, invalid date, blank categories, negative/nonfinite amounts, and duplicate order IDs. Expect explicit `ValueError` or `FileNotFoundError`; observe failure before implementation.
- [x] Implement validation with explicit messages and add a title-only app that catches load errors and stops.
- [x] Run `venv/Scripts/python -m pytest -q`, launch `streamlit run app.py`, then commit with TASK-1 and record its hash.

## Task 2 — TASK-2: KPI cards

Files: `sales.py`, `tests/test_sales.py`, `app.py`, `TASKS.md`.

Interface: `calculate_kpis(df) -> tuple[float, int]` returns summed amount and transaction count.

- [x] Write a test with amounts 20, 5, and 10, expecting sales 35 and orders 3. Observe its failure.
- [x] Implement the calculation and two formatted `st.metric` cards; currency has two decimals and counts use separators.
- [x] Run tests and app smoke check, commit with TASK-2, update board.

## Task 3 — TASK-3: Monthly trend

Files: `sales.py`, `tests/test_sales.py`, `app.py`, `TASKS.md`.

Interface: `monthly_sales(df) -> DataFrame` with `date`, `total_amount` columns.

- [x] Test out-of-order dates across January and February with January totaling 15 and February 20. Assert chronological dates and reconciliation to 35. Observe failure.
- [x] Implement month-start aggregation and a Plotly line chart with date x-axis, sales y-axis, markers, and currency tooltips.
- [x] Run tests, visually inspect the trend, commit with TASK-3, update board.

## Task 4 — TASK-4: Category and region breakdowns

Files: `sales.py`, `tests/test_sales.py`, `app.py`, `TASKS.md`.

Interface: `sales_by(df, column) -> DataFrame`, permitting only `category` or `region`, descending by amount with alphabetical tie breaking.

- [x] Test fixture category totals A=25/B=10 and region East=30/West=5, including descending order and reconciliation. Observe failure.
- [x] Implement grouping and side-by-side horizontal Plotly bar charts, largest at top, all labels visible.
- [x] Run tests, inspect bars and hover values, commit with TASK-4, update board.

## Task 5 — TASK-5: Verification and deployment

Files: `tests/test_app.py`, `AGENTS.md`, `TASKS.md`, `README.md`.

- [x] Independently calculate CSV control totals with standard-library CSV and Decimal; compare to the app and chart aggregates.
- [x] Run Streamlit AppTest; require no exceptions, two metrics, and three charts. Run the full pytest suite.
- [x] Open the live local app and inspect title, KPI values, chart ordering, labels, and tooltips. Record the tested browser and timing limitations.
- [x] Write project instructions, run/redeploy directions, provenance, and lessons; preserve the upstream README as `TUTORIAL.md` before replacing the root landing page.
- [x] Review the branch against the PRD, fix substantive findings, and record actual review limitations. Commit with TASK-5.
- [x] Publish to Joseph's `ai-dev-workflow-tutorial` GitHub repository on main. Verify code and board arrived.
- [x] Deploy main/app.py to Streamlit Community Cloud after account authorization, open the public URL, verify all charts, and record the URL and real completion status.

## Plan self-review and approval

Codex checked coverage against the approved design and PRD: all five functional requirements, separate calculations, tests, readable source, versioned board, and deployment are covered. Each computation has independently calculated fixture expectations. Chart presentation additionally requires a visual check. Joseph approved this saved plan and inline execution on September 22, 2026, before the build began.


## Execution and review evidence

- TASK-1: 13 tests failed for missing load_sales, then all 13 passed after validation implementation. Commit ebcffbd.
- TASK-2–4: five new calculation tests failed for missing functions, then all 18 tests passed. Shared code commit 29d1715; separate board commits record each milestone. Combined calculation work is an explicit deviation from separate per-milestone code commits, chosen because the small module shares one fixture and validation contract.
- TASK-5: independent Decimal total equals 116500.21 for 482 rows; 19 tests pass, including AppTest with two metrics, three charts, and no app errors. Code/docs commit e783bf5.
- Visual review: in-app Chromium showed readable KPI cards, Jan–Dec trend, all five categories and four regions, largest bars at top. Browser tooltip check displayed Electronics $42,683.67; cross-browser coverage remains unverified.
- Review performed inline by Codex against the PRD and diff; no independent reviewer or student review is claimed. Retained tutorial instructions. No private data or credentials staged. Cold-cloud startup timing targets remain unmeasured.


Published main commit 358f218; anonymous HTTP retrieval of app.py, requirements.txt, and TASKS.md returned 200 and matched local contents.


Deployment completed September 22, 2026: https://shopsmart-joseph-barragan.streamlit.app/. Codex verified the live KPI values ($116,500.21 and 482), monthly chart, all five categories and four regions with descending bars. Anonymous HTTP access returned 200. Google Docs work and Joseph’s personal assignment reviews are separate from dashboard completion.
