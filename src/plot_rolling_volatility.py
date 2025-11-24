import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from src.compute_metrics import rolling_volatility

def plot_rolling_volatility():
    # Load dataset
    df = pd.read_csv("data/AAPL.csv", parse_dates=["Date"], index_col="Date")

    # Use Adj Close if available
    if "Adj Close" in df.columns:
        prices = df["Adj Close"]
    else:
        prices = df["Close"]

    # Compute rolling volatility
    vol = rolling_volatility(prices, window=30)

    # Plot
    plt.figure(figsize=(10, 5))
    plt.plot(vol.index, vol, label="30-Day Rolling Volatility", color="orange")
    
    plt.xlabel("Date")
    plt.ylabel("Volatility (std of returns)")
    plt.title("AAPL 30-Day Rolling Volatility (2015–2025)")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    # Save output
    Path("figures").mkdir(exist_ok=True)
    plt.savefig("figures/figure3_rolling_volatility.png", dpi=300)
    print("Saved figures/figure3_rolling_volatility.png")

if __name__ == "__main__":
    plot_rolling_volatility()
