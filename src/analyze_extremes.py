import pandas as pd
import numpy as np
from pathlib import Path
from src.compute_metrics import rolling_volatility

def compute_extremes():
    # Load data
    df = pd.read_csv("data/AAPL.csv", parse_dates=["Date"], index_col="Date")

    # Use adjusted close if present
    prices = df["Adj Close"] if "Adj Close" in df.columns else df["Close"]

    # Daily returns
    returns = prices.pct_change()

    # Rolling volatility
    vol = rolling_volatility(prices, window=30)

    # Extreme thresholds
    threshold_3sigma = 3 * vol
    threshold_2sigma = 2 * vol
    threshold_p95 = returns.abs().quantile(0.95)

    # Boolean masks
    extreme_3sigma = returns.abs() > threshold_3sigma
    extreme_2sigma = returns.abs() > threshold_2sigma
    extreme_p95 = returns.abs() > threshold_p95

    result = pd.DataFrame({
        "Returns": returns,
        "Volatility": vol,
        "Extreme_3sigma": extreme_3sigma,
        "Extreme_2sigma": extreme_2sigma,
        "Extreme_p95": extreme_p95
    })

    Path("data").mkdir(exist_ok=True)
    result.to_csv("data/extreme_analysis.csv")
    print("Saved extreme analysis to data/extreme_analysis.csv")

    return result

if __name__ == "__main__":
    compute_extremes()
