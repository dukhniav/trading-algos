import requests
import os
from utils import Utils

utils = Utils()

utils.setup()

API_KEY = utils.alpha_vantage_api_key


def get_stock_data(symbol):
    alpha_interval = "5min"
    alpha_function = "TIME_SERIES_INTRADAY"

    url = f"https://www.alphavantage.co/query?function={alpha_function}&symbol={symbol}&interval={alpha_interval}&apikey={API_KEY}"

    response = requests.get(url)
    data = response.json()

    # Extract the daily stock prices
    time_series = data["Time Series (5min)"]
    stock_data = []
    for date, values in time_series.items():
        stock_data.append(
            {
                "date": date,
                "open": float(values["1. open"]),
                "high": float(values["2. high"]),
                "low": float(values["3. low"]),
                "close": float(values["4. close"]),
                "volume": int(values["5. volume"]),
            }
        )

    return stock_data


# Example usage
symbol = "AAPL"
stock_data = get_stock_data(symbol)
for data in stock_data:
    print(data)
