import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def plot_yearly_extremes():
    df = pd.read_csv("data/extreme_analysis.csv", parse_dates=["Date"], index_col="Date")

    df["Year"] = df.index.year

    counts = df.groupby("Year")["Extreme_3sigma"].sum()

    plt.figure(figsize=(10, 5))
    plt.bar(counts.index, counts.values)

    plt.title("Count of Extreme Daily Returns (>3σ) Per Year")
    plt.xlabel("Year")
    plt.ylabel("Number of Extreme Days")
    plt.tight_layout()

    Path("figures").mkdir(exist_ok=True)
    plt.savefig("figures/figure7_yearly_extremes.png", dpi=300)

    counts.to_csv("data/yearly_extreme_counts.csv")
    print("Saved yearly extreme count table and figure.")

if __name__ == "__main__":
    plot_yearly_extremes()
