import pytest
from calculate_real_return.stock_calculator import (
    StockCalculator,
)  # replace with your actual import


def test_correct_calculations():
    calc = StockCalculator(100, "01/01/2021", 10, 2, 100, 5)  # sample input
    min_price, max_price = calc.calculate_sell_price()
    assert min_price == 125.54102508804239
    assert max_price == 133.5923154713842


def test_edge_cases():
    calc = StockCalculator(100, "01/07/2023", 0, 0, 100, 0)  # sample edge case input
    min_price, max_price = calc.calculate_sell_price()
    assert min_price == 100.00
    assert max_price == 100.00
    # ... more edge cases


# ... more tests for different scenarios and input types
