from pathlib import Path

import pandas as pd
import pytest

import sales


@pytest.fixture
def sample():
    return pd.DataFrame({
        'date': ['2024-02-03', '2024-01-20', '2024-01-01'],
        'order_id': ['o1', 'o2', 'o3'],
        'category': ['A', 'A', 'B'],
        'region': ['East', 'West', 'East'],
        'total_amount': [20, 5, 10],
    })


def write_csv(tmp_path, data):
    path = tmp_path / 'sales.csv'
    data.to_csv(path, index=False)
    return path


def test_valid_csv(tmp_path, sample):
    result = sales.load_sales(write_csv(tmp_path, sample))
    assert len(result) == 3
    assert pd.api.types.is_datetime64_any_dtype(result['date'])
    assert result['total_amount'].sum() == 35


def test_missing_file(tmp_path):
    with pytest.raises(FileNotFoundError):
        sales.load_sales(tmp_path / 'absent.csv')


def test_empty_csv(tmp_path, sample):
    with pytest.raises(ValueError, match='empty'):
        sales.load_sales(write_csv(tmp_path, sample.iloc[:0]))


def test_missing_column(tmp_path, sample):
    with pytest.raises(ValueError, match='Missing columns'):
        sales.load_sales(write_csv(tmp_path, sample.drop(columns='region')))


@pytest.mark.parametrize('column,value', [
    ('date', 'not-a-date'), ('category', ' '), ('order_id', ''),
    ('region', None), ('total_amount', -1), ('total_amount', float('inf')),
    ('total_amount', float('nan')), ('total_amount', 'invalid'),
])
def test_invalid_values(tmp_path, sample, column, value):
    sample[column] = sample[column].astype(object)
    sample.loc[0, column] = value
    with pytest.raises(ValueError):
        sales.load_sales(write_csv(tmp_path, sample))


def test_duplicate_orders(tmp_path, sample):
    sample.loc[1, 'order_id'] = 'o1'
    with pytest.raises(ValueError, match='Duplicate'):
        sales.load_sales(write_csv(tmp_path, sample))
