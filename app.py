"""ShopSmart executive sales dashboard using the tutorial's public sample data."""

from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

from sales import calculate_kpis, load_sales, monthly_sales, sales_by

st.set_page_config(page_title='ShopSmart | Sales Overview', page_icon='📊', layout='wide')
st.title('ShopSmart · Sales Overview')
try:
    data = load_sales(Path(__file__).parent / 'data' / 'sales-data.csv')
except (OSError, ValueError, pd.errors.ParserError) as error:
    st.error(f'Unable to load sales data: {error}')
    st.stop()
st.caption('Public tutorial sample data · January–December 2024 · Prepared by Joseph Barragan')

total_sales, total_orders = calculate_kpis(data)
sales_card, orders_card = st.columns(2)
sales_card.metric('Total Sales', f'${total_sales:,.2f}', border=True)
orders_card.metric('Total Orders', f'{total_orders:,}', border=True)

st.subheader('Sales over time')
st.caption('Monthly revenue · hover for exact values')
trend = px.line(monthly_sales(data), x='date', y='total_amount', markers=True,
                labels={'date': 'Month', 'total_amount': 'Sales (USD)'},
                color_discrete_sequence=['#147d92'])
trend.update_traces(hovertemplate='%{x|%B %Y}<br>$%{y:,.2f}<extra></extra>',
                    line={'width': 3}, marker={'size': 7})
trend.update_layout(height=340, margin={'l': 10, 'r': 10, 't': 10, 'b': 10},
                    xaxis={'tickformat': '%b', 'dtick': 'M1'},
                    yaxis={'tickprefix': '$'}, showlegend=False)
st.plotly_chart(trend, width='stretch', config={'displayModeBar': False})

left, right = st.columns(2)
for panel, column, title, color in [
    (left, 'category', 'Sales by category', '#147d92'),
    (right, 'region', 'Sales by region', '#465bb5'),
]:
    with panel:
        st.subheader(title)
        grouped = sales_by(data, column)
        chart = px.bar(grouped, x='total_amount', y=column, orientation='h',
                       text='total_amount',
                       labels={'total_amount': 'Sales (USD)', column: ''},
                       color_discrete_sequence=[color])
        chart.update_traces(texttemplate='$%{x:,.0f}', textposition='outside',
                            cliponaxis=False,
                            hovertemplate='%{y}<br>$%{x:,.2f}<extra></extra>')
        chart.update_layout(height=340, showlegend=False,
                            margin={'l': 0, 'r': 65, 't': 10, 'b': 10},
                            yaxis={'categoryorder': 'array',
                                   'categoryarray': grouped[column].tolist(),
                                   'autorange': 'reversed'},
                            xaxis={'tickprefix': '$'})
        st.plotly_chart(chart, width='stretch', config={'displayModeBar': False})

st.divider()
st.caption('Source: LMU AI Dev Workflow Tutorial · Static sample data, not live sales. '
           'Sales = sum of transaction amounts; orders = validated transaction rows.')
