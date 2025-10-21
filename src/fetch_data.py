import yfinance as yf
import pandas as pd
from pathlib import Path

def fetch_aapl_data(start="2015-01-01", end="2025-10-21"):
    """Fetch Apple daily price data from Yahoo Finance."""
    df = yf.download("AAPL", start=start, end=end, auto_adjust=False, progress=False)
    Path("data").mkdir(exist_ok=True)
    df.to_csv("data/AAPL.csv")
    print(f"Saved {len(df)} rows to data/AAPL.csv")
    return df

if __name__ == "__main__":
    fetch_aapl_data()
