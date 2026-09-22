"""ShopSmart executive sales dashboard using the tutorial's public sample data."""

from pathlib import Path

import pandas as pd
import streamlit as st

from sales import load_sales

st.set_page_config(page_title='ShopSmart | Sales Overview', page_icon='📊', layout='wide')
st.title('ShopSmart · Sales Overview')
try:
    data = load_sales(Path(__file__).parent / 'data' / 'sales-data.csv')
except (OSError, ValueError, pd.errors.ParserError) as error:
    st.error(f'Unable to load sales data: {error}')
    st.stop()
st.caption('Public tutorial sample data · January–December 2024 · Prepared by Joseph Barragan')
