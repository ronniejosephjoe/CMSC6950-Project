import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def plot_sensitivity():
    df = pd.read_csv("data/extreme_analysis.csv", parse_dates=["Date"], index_col="Date")

    returns = df["Returns"]
    e2 = df["Extreme_2sigma"]
    e3 = df["Extreme_3sigma"]
    ep = df["Extreme_p95"]

    plt.figure(figsize=(12, 6))
    plt.plot(returns.index, returns, alpha=0.3, label="Daily Returns")

    plt.scatter(returns.index[e2], returns[e2], s=8, color="blue", label="> 2σ", alpha=0.6)
    plt.scatter(returns.index[e3], returns[e3], s=10, color="red", label="> 3σ", alpha=0.8)
    plt.scatter(returns.index[ep], returns[ep], s=12, color="green", label="> 95th percentile", alpha=0.5)

    plt.title("Sensitivity Analysis of Extreme Value Definitions")
    plt.xlabel("Date")
    plt.ylabel("Daily Return")
    plt.legend()
    plt.tight_layout()

    Path("figures").mkdir(exist_ok=True)
    plt.savefig("figures/figure5_sensitivity.png", dpi=300)
    print("Saved figures/figure5_sensitivity.png")

if __name__ == "__main__":
    plot_sensitivity()
