#!/usr/bin/env python3
"""
Data Agent Module: Fetch and preprocess market data.
Dependencies: pandas>=1.5, yfinance>=0.2, ta>=0.10, numpy, pyarrow, pytz
"""
import argparse
import logging
from datetime import datetime
import pandas as pd
import yfinance as yf
import numpy as np
import ta  # Technical Analysis library

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s:%(message)s")

def fetch_data(symbol: str, start: str, end: str, interval: str = "1d") -> pd.DataFrame:
    """
    Fetch historical market data from Yahoo Finance.
    Returns DataFrame with datetime index (UTC) and OHLCV columns.
    """
    try:
        df = yf.download(symbol, start=start, end=end, interval=interval, progress=False)
        df.dropna(inplace=True)
        df.index = pd.to_datetime(df.index)
        if df.index.tzinfo is None:
            df.index = df.index.tz_localize('UTC')
        logging.info(f"Fetched {len(df)} rows for {symbol}")
        return df
    except Exception as e:
        logging.error(f"Error fetching data: {e}")
        raise

def add_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute technical features and append to DataFrame.
    Features: Return, LogReturn, SMA (20), EMA (20), RSI (14), ATR (14), Volatility (20).
    """
    df = df.copy()
    df['Return'] = df['Close'].pct_change()
    df['LogReturn'] = np.log(df['Close'] / df['Close'].shift(1))
    df['SMA_20'] = df['Close'].rolling(window=20).mean()
    df['EMA_20'] = df['Close'].ewm(span=20, adjust=False).mean()
    df['Volatility_20'] = df['Return'].rolling(window=20).std()
    # RSI
    df['RSI_14'] = ta.momentum.RSIIndicator(df['Close'], window=14, fillna=False).rsi()
    # ATR
    df['ATR_14'] = ta.volatility.AverageTrueRange(high=df['High'], low=df['Low'], close=df['Close'], window=14).average_true_range()
    df.dropna(inplace=True)
    logging.info("Features added")
    return df

def save_data(df: pd.DataFrame, filename: str) -> None:
    """
    Save DataFrame to CSV or Parquet based on file extension.
    """
    try:
        if filename.lower().endswith('.csv'):
            df.to_csv(filename)
        elif filename.lower().endswith('.parquet'):
            df.to_parquet(filename)
        else:
            raise ValueError("Unsupported file format. Use .csv or .parquet")
        logging.info(f"Data saved to {filename}")
    except Exception as e:
        logging.error(f"Error saving data: {e}")
        raise

def load_data(filename: str) -> pd.DataFrame:
    """
    Load data from CSV or Parquet.
    """
    try:
        if filename.lower().endswith('.csv'):
            return pd.read_csv(filename, index_col=0, parse_dates=True)
        elif filename.lower().endswith('.parquet'):
            return pd.read_parquet(filename)
        else:
            raise ValueError("Unsupported file format. Use .csv or .parquet")
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        raise

def validate_no_missing(df: pd.DataFrame) -> bool:
    """Return True if no NaN values in DataFrame."""
    missing = df.isnull().any().any()
    if missing:
        logging.warning("Missing values found in data")
    return not missing

def main():
    parser = argparse.ArgumentParser(description="Data Agent CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Fetch command
    fetch_parser = subparsers.add_parser("fetch", help="Fetch market data")
    fetch_parser.add_argument("--symbol", required=True, help="Ticker symbol")
    fetch_parser.add_argument("--start", required=True, help="Start date (YYYY-MM-DD)")
    fetch_parser.add_argument("--end", required=True, help="End date (YYYY-MM-DD)")
    fetch_parser.add_argument("--interval", default="1d", help="Data interval (e.g. 1d, 1h)")
    fetch_parser.add_argument("--out", required=True, help="Output file path (.csv/.parquet)")

    # Add-features command
    feat_parser = subparsers.add_parser("add-features", help="Add technical features")
    feat_parser.add_argument("--infile", required=True, help="Input data file (.csv/.parquet)")
    feat_parser.add_argument("--outfile", required=True, help="Output data file with features (.csv/.parquet)")

    args = parser.parse_args()
    if args.command == "fetch":
        df = fetch_data(args.symbol, args.start, args.end, args.interval)
        save_data(df, args.out)
    elif args.command == "add-features":
        df = load_data(args.infile)
        df2 = add_features(df)
        save_data(df2, args.outfile)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
