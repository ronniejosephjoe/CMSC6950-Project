import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from pathlib import Path

def plot_decomposition():
    df = pd.read_csv("data/extreme_analysis.csv", parse_dates=["Date"], index_col="Date")
    vol = df["Volatility"].dropna()

    decomposition = seasonal_decompose(vol, model="additive", period=252)

    fig = decomposition.plot()
    fig.set_size_inches(12, 8)

    Path("figures").mkdir(exist_ok=True)
    plt.savefig("figures/figure8_decomposition.png", dpi=300)
    print("Saved decomposition plot.")

if __name__ == "__main__":
    plot_decomposition()
