"""Validated sales data and dashboard calculations."""

from pathlib import Path

import numpy as np
import pandas as pd


def load_sales(path: Path) -> pd.DataFrame:
    """Load the tutorial's one-transaction-per-order CSV or raise a clear error."""
    try:
        data = pd.read_csv(path, dtype={'order_id': 'string'})
    except pd.errors.EmptyDataError as exc:
        raise ValueError('Sales file is empty.') from exc
    required = {'date', 'order_id', 'category', 'region', 'total_amount'}
    missing = required - set(data.columns)
    if missing:
        raise ValueError(f'Missing columns: {", ".join(sorted(missing))}')
    if data.empty:
        raise ValueError('Sales file is empty.')
    for column in ['order_id', 'category', 'region']:
        data[column] = data[column].astype('string').str.strip()
        if data[column].isna().any() or data[column].eq('').any():
            raise ValueError(f'{column} contains blank values.')
    if data['order_id'].duplicated().any():
        raise ValueError('Duplicate order IDs: expected one row per order.')
    data['date'] = pd.to_datetime(data['date'], format='%Y-%m-%d', errors='coerce')
    if data['date'].isna().any():
        raise ValueError('Dates must be valid YYYY-MM-DD values.')
    data['total_amount'] = pd.to_numeric(data['total_amount'], errors='coerce')
    if not np.isfinite(data['total_amount']).all() or data['total_amount'].lt(0).any():
        raise ValueError('Sales amounts must be finite, nonnegative numbers.')
    return data


def calculate_kpis(data: pd.DataFrame) -> tuple[float, int]:
    """Sum sales and count the validated one-row-per-order transactions."""
    return float(data['total_amount'].sum()), len(data)


def monthly_sales(data: pd.DataFrame) -> pd.DataFrame:
    """Aggregate calendar months in chronological order."""
    return (data.set_index('date')['total_amount']
            .resample('MS').sum().reset_index())


def sales_by(data: pd.DataFrame, column: str) -> pd.DataFrame:
    """Rank category or region totals, using names to break ties."""
    if column not in {'category', 'region'}:
        raise ValueError('Group must be category or region.')
    return (data.groupby(column, as_index=False)['total_amount'].sum()
            .sort_values(['total_amount', column], ascending=[False, True])
            .reset_index(drop=True))
