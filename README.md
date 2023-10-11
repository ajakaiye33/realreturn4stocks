# Stock Profit Optimizer
> Realize Your Investment Goals with Data-Driven Insights

![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)
[![Python CI using Makefile's all target](https://github.com/ajakaiye33/realreturn4stocks/actions/workflows/main.yaml/badge.svg)](https://github.com/ajakaiye33/realreturn4stocks/actions/workflows/main.yaml)

## About

Stock Profit Optimizer calculates the ideal minimum and maximum price per share to sell a stock, considering various financial metrics and real-world conditions like inflation. The application assists investors in maximizing their returns through a robust, data-backed approach. 

The application operates under the assumption that you will hold the stock for a minimum of 6 months, although you can specify a different holding period.

## Features

- **User-Friendly Interface:** Utilizes Streamlit for a clean, intuitive user experience.
- **Customizable Parameters:** Tailor your target rate of return, inflation rate, number of shares, and more.
- **Data-Driven:** Built with precision and efficiency at its core.

## Installation

Clone this repository and navigate into the project directory. Run the following commands:

```bash
git clone https://github.com/ajakaiye33/realreturn4stocks.git
cd real_stock_calculator
python -m venv venv
source venv/bin/activate python
make all
```


## Usage

To start the Streamlit app:

```bash
streamlit run streamlit_app.py
```

Navigate to `http://localhost:8501` in your web browser.

## Testing

Run all unit tests to ensure the application behaves as expected.

```bash
make test
```


