import csv
from decimal import Decimal
from pathlib import Path

from streamlit.testing.v1 import AppTest

from sales import calculate_kpis, load_sales, monthly_sales, sales_by


ROOT = Path(__file__).resolve().parents[1]


def test_dashboard_matches_independent_csv_control_totals():
    with (ROOT / 'data/sales-data.csv').open() as source:
        rows = list(csv.DictReader(source))
    expected = sum(Decimal(row['total_amount']) for row in rows)
    assert expected == Decimal('116500.21')
    assert len(rows) == 482
    data = load_sales(ROOT / 'data/sales-data.csv')
    total, orders = calculate_kpis(data)
    assert round(total, 2) == float(expected)
    assert orders == len(rows)
    for grouped in [monthly_sales(data), sales_by(data, 'category'), sales_by(data, 'region')]:
        assert round(grouped['total_amount'].sum(), 2) == float(expected)
    assert sales_by(data, 'category').iloc[0]['category'] == 'Electronics'
    app = AppTest.from_file(str(ROOT / 'app.py')).run(timeout=30)
    assert not app.exception
    assert not app.error
    assert [(metric.label, metric.value) for metric in app.metric] == [
        ('Total Sales', '$116,500.21'), ('Total Orders', '482')]
    assert len(app.get('plotly_chart')) == 3
