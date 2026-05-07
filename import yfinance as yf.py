import yfinance as yf
import pandas as pd

def fetch_data(symbol="AAPL", start="2023-01-01", end="2024-01-01"):
    # Download data from Yahoo Finance
    data = yf.download(symbol, start=start, end=end)

    # Clean data (remove missing values)
    data = data.dropna()

    return data


def main():
    data = fetch_data()

    # Show first few rows
    print(data.head())

    # Save to CSV (important for later modules)
    data.to_csv("market_data.csv")

    print("\nData saved to market_data.csv")


if __name__ == "__main__":
    main()