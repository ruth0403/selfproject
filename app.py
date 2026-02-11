import streamlit as st
import pandas as pd
import numpy as np
from yahooquery import Ticker
import plotly.graph_objects as go

st.set_page_config(page_title="Stock Analysis App", layout="wide")
st.title("📈 Stock Analysis Dashboard")

# User input
ticker_input = st.text_input("Enter Stock Ticker (e.g., AAPL, TSLA, MSFT):", "AAPL")

if ticker_input:

    stock = Ticker(ticker_input)

    # Company info
    info = stock.asset_profile[ticker_input]

    st.subheader("Company Overview")
    col1, col2 = st.columns(2)

    with col1:
        st.write("**Company Name:**", info.get("longBusinessSummary", "N/A")[:100] + "...")
        st.write("**Sector:**", info.get("sector", "N/A"))
        st.write("**Industry:**", info.get("industry", "N/A"))

    with col2:
        quote = stock.quote_type[ticker_input]
        st.write("**Current Price:**", quote.get("regularMarketPrice", "N/A"))
        st.write("**Market Cap:**", q
