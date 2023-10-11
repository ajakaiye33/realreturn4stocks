from datetime import datetime
from dateutil.relativedelta import relativedelta


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
        return delta.years + delta.months / 12 + delta.days / 365.25

    def calculate_real_rate(self):
        return self.target_rate - self.current_cpi

    def calculate_sell_price(self):
        years = self.time_since_purchase()
        real_rate = self.calculate_real_rate()
        max_price_per_share = (
            self.initial_price * (1 + self.target_rate) ** years + self.fees_per_share
        )
        min_price_per_share = (
            self.initial_price * (1 + real_rate) ** years + self.fees_per_share
        )
        return min_price_per_share, max_price_per_share
