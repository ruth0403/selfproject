import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

st.set_page_config(page_title="Simple Stock App")

st.title("📈 Simple Stock Analysis")

ticker = st.text_input("Enter Stock Ticker:", "AAPL")

if ticker:
    stock = yf.Ticker(ticker)

    # Current price
    info = stock.info
    price = info.get("currentPrice", "N/A")

    st.subheader(f"Current Price: {price}")

    # Historical data
    hist = stock.history(period="1y")

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=hist.index,
        y=hist["Close"],
        mode="lines",
        name="Close Price"
    ))

    fig.update_layout(
        title=f"{ticker} - Last 1 Year",
        xaxis_title="Date",
        yaxis_title="Price"
    )

    st.plotly_chart(fig, use_container_width=True)
