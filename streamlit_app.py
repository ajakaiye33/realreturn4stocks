import streamlit as st
from calculate_real_return.stock_calculator import StockCalculator
from datetime import datetime

# Custom CSS
st.markdown(
    """
    <style>
        .stButton > button:first-child {
            background-color: #4CAF50;
            color: white;
            padding: 12px 24px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("📈 Stock Profitability Calculator 📊")

# Sidebar
st.sidebar.header("About")
st.sidebar.markdown(
    """
This application serves as an advanced tool for investors aiming to optimize their stock trading strategies. It performs a sophisticated financial analysis to calculate the ideal minimum and maximum selling prices per share for a stock, ensuring a real, inflation-adjusted profit. 

The app takes into account multiple factors including the stock's initial purchase price, the date of purchase, your targeted rate of return, the current rate of inflation (CPI), the total number of shares you've purchased, and any additional fees or charges you've incurred during the transaction. 

The algorithm behind the calculations assumes a minimum holding period of 6 months for the stock, but can also accommodate longer or shorter holding periods as specified by the user.

"""
)

# Main Content
st.header("Input Parameters")
with st.container():
    initial_price = st.number_input(
        "Initial price per share ($)", min_value=0.0, max_value=100000.0, step=0.01
    )
    purchase_date = st.date_input("Purchase date")
    target_rate = st.number_input(
        "Target rate of return (%)", min_value=0.0, max_value=100.0, step=0.01
    )
    current_cpi = st.number_input(
        "Current CPI or inflation rate (%)", min_value=0.0, max_value=100.0, step=0.01
    )
    num_shares = st.number_input(
        "Number of shares bought", min_value=1, max_value=100000, step=1
    )
    fees = st.number_input(
        "Total fees/charges incurred ($)", min_value=0.0, max_value=10000.0, step=0.01
    )

if st.button("Calculate"):
    try:
        purchase_date_str = purchase_date.strftime("%d/%m/%Y")
        calculator = StockCalculator(
            initial_price, purchase_date_str, target_rate, current_cpi, num_shares, fees
        )
        min_price_per_share, max_price_per_share = calculator.calculate_sell_price()
        st.success(
            f"The ideal minimum price per share to sell the stock for real profit is: ${min_price_per_share:.2f}"
        )
        st.success(
            f"The suggested target maximum price per share to consider for selling is: ${max_price_per_share:.2f}"

        )

        with st.expander("What does 'Suggested Target Maximum' mean?", expanded=False):
            st.write("The 'Suggested Target Maximum' is calculated based on the inputs you've provided and current market conditions. It serves as a high-probability target for selling your shares. However, selling above this price could result in exceptionally high returns.")

    except Exception as e:
        st.error(f"An error occurred: {e}")
