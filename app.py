import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

import yfinance as yf
print(yf.__version__)


st.set_page_config(page_title="Stock Analysis App", layout="wide")

st.title("📈 Stock Analysis Dashboard")

# User input
ticker_input = st.text_input("Enter Stock Ticker (e.g., AAPL, TSLA, MSFT):", "AAPL")

if ticker_input:

    stock = yf.Ticker(ticker_input)

    # Get stock info
    info = stock.info

    st.subheader("Company Overview")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Company Name:**", info.get("longName", "N/A"))
        st.write("**Sector:**", info.get("sector", "N/A"))
        st.write("**Industry:**", info.get("industry", "N/A"))
        st.write("**Market Cap:**", info.get("marketCap", "N/A"))

    with col2:
        st.write("**Current Price:**", info.get("currentPrice", "N/A"))
        st.write("**52 Week High:**", info.get("fiftyTwoWeekHigh", "N/A"))
        st.write("**52 Week Low:**", info.get("fiftyTwoWeekLow", "N/A"))
        st.write("**Dividend Yield:**", info.get("dividendYield", "N/A"))

    # Historical Data
    st.subheader("📊 Price Chart (1 Year)")

    hist = stock.history(period="1y")

    # Moving averages
    hist["MA50"] = hist["Close"].rolling(window=50).mean()
    hist["MA200"] = hist["Close"].rolling(window=200).mean()

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=hist.index,
        y=hist["Close"],
        mode="lines",
        name="Closing Price"
    ))

    fig.add_trace(go.Scatter(
        x=hist.index,
        y=hist["MA50"],
        mode="lines",
        name="50-Day MA"
    ))

    fig.add_trace(go.Scatter(
        x=hist.index,
        y=hist["MA200"],
        mode="lines",
        name="200-Day MA"
    ))

    fig.update_layout(
        title=f"{ticker_input} Price Chart",
        xaxis_title="Date",
        yaxis_title="Price",
        template="plotly_dark"
    )

    st.plotly_chart(fig, use_container_width=True)

    # Financial Metrics
    st.subheader("📑 Key Financial Metrics")

    col3, col4, col5 = st.columns(3)

    with col3:
        st.metric("P/E Ratio", info.get("trailingPE", "N/A"))
        st.metric("Forward P/E", info.get("forwardPE", "N/A"))

    with col4:
        st.metric("EPS (TTM)", info.get("trailingEps", "N/A"))
        st.metric("Revenue", info.get("totalRevenue", "N/A"))

    with col5:
        st.metric("ROE", info.get("returnOnEquity", "N/A"))
        st.metric("Debt to Equity", info.get("debtToEquity", "N/A"))

    # Financial Statements
    st.subheader("📄 Financial Statements")

    if st.checkbox("Show Income Statement"):
        st.write(stock.financials)

    if st.checkbox("Show Balance Sheet"):
        st.write(stock.balance_sheet)

    if st.checkbox("Show Cash Flow"):
        st.write(stock.cashflow)
