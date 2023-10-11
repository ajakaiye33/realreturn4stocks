from datetime import datetime
from dateutil.relativedelta import relativedelta
import streamlit as st


class StockCalculator:
    MIN_HOLDING_PERIOD_MONTHS = 6  # Minimum holding period in months

    def __init__(
        self, initial_price, purchase_date, target_rate, current_cpi, num_shares, fees
    ):
        self.initial_price = float(initial_price)
        self.purchase_date = datetime.strptime(purchase_date, "%d/%m/%Y")
        self.target_rate = float(target_rate) / 100
        self.current_cpi = float(current_cpi) / 100
        self.num_shares = int(num_shares)
        self.fees = float(fees)
        self.fees_per_share = self.fees / self.num_shares

    def time_since_purchase(self):
        current_date = datetime.now()
        delta = relativedelta(current_date, self.purchase_date)
        months_held = delta.years * 12 + delta.months
        if months_held < self.MIN_HOLDING_PERIOD_MONTHS:
            st.write(f"Note: Your holding period of {months_held} months is less than the recommended minimum of {self.MIN_HOLDING_PERIOD_MONTHS} months.")
        return delta.years + delta.months / 12 + delta.days / 365.25

    def calculate_real_rate(self):
        #return self.target_rate - self.current_cpi
        #return ((1 + self.target_rate) / (1 + self.current_cpi)) - 1
        real_rate = ((1 + self.target_rate) / (1 + self.current_cpi)) - 1
        st.write(f"Your target nominal rate of return is {self.target_rate * 100}%. Considering an inflation rate of {self.current_cpi * 100}%, your real rate of return is {real_rate * 100:.2f}%.")  # Informing the user about the real rate
        return real_rate


    def calculate_sell_price(self, n=12):  # n=12 for monthly compounding
        years = self.time_since_purchase()
        real_rate = self.calculate_real_rate()
        max_price_per_share = (
            self.initial_price * (1 + self.target_rate / n) ** (n * years) + self.fees_per_share
        )
        min_price_per_share = (
            self.initial_price * (1 + real_rate / n) ** (n * years) + self.fees_per_share
        )
        return min_price_per_share, max_price_per_share
