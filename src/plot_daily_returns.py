import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def plot_daily_returns():
    # Load dataset
    df = pd.read_csv("data/AAPL.csv", parse_dates=["Date"], index_col="Date")

    # Use Adj Close if available, otherwise Close
    prices = df["Adj Close"] if "Adj Close" in df.columns else df["Close"]

    # Compute daily returns
    returns = prices.pct_change()

    # Plot
    plt.figure(figsize=(10, 5))
    plt.plot(returns.index, returns, label="Daily Returns")
    plt.axhline(0, color="black", linewidth=0.8)

    plt.xlabel("Date")
    plt.ylabel("Daily Return")
    plt.title("AAPL Daily Returns (2015–2025)")
    plt.tight_layout()

    # Save output
    Path("figures").mkdir(exist_ok=True)
    plt.savefig("figures/figure2_daily_returns.png", dpi=300)
    print("Saved figures/figure2_daily_returns.png")

if __name__ == "__main__":
    plot_daily_returns()
