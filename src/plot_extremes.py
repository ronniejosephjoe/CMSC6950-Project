import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def plot_extremes():
    df = pd.read_csv("data/extreme_analysis.csv", parse_dates=["Date"], index_col="Date")

    # Subset for clarity
    returns = df["Returns"]
    extremes = df["Extreme_3sigma"]

    plt.figure(figsize=(12, 5))
    plt.plot(returns.index, returns, alpha=0.4, label="Daily Returns")
    plt.scatter(
        returns.index[extremes],
        returns[extremes],
        color="red",
        s=10,
        label="Extreme Returns (>3σ)"
    )

    plt.axhline(0, color="black", linewidth=0.8)
    plt.title("Extreme Daily Returns (>|3σ|)")
    plt.xlabel("Date")
    plt.ylabel("Daily Return")
    plt.legend()
    plt.tight_layout()

    Path("figures").mkdir(exist_ok=True)
    plt.savefig("figures/figure4_extreme_returns.png", dpi=300)
    print("Saved figures/figure4_extreme_returns.png")

if __name__ == "__main__":
    plot_extremes()
