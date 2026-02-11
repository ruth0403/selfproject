import streamlit as st
from yahooquery import Ticker
import pandas as pd
import plotly.graph_objects as go

st.title("Simple Stock Analysis with yahooquery")

# Input ticker
ticker_input = st.text_input("Enter Stock Ticker:", "AAPL")

if ticker_input:
    stock = Ticker(ticker_input)

    # Current price
    quote = stock.quote_type.get(ticker_input, {})
    price = quote.get("regularMarketPrice", "N/A")
    st.subheader(f"Current Price: {price}")

    # Historical price (1 year)
    hist = stock.history(period="1y").reset_index()
    if not hist.empty:
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=hist['date'],
            y=hist['close'],
            mode='lines',
            name='Close Price'
        ))
        fig.update_layout(title=f"{ticker_input} - Last 1 Year",
                          xaxis_title="Date", yaxis_title="Price")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("No historical data found for this ticker.")
