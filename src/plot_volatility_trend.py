import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.linear_model import LinearRegression
import numpy as np

def plot_volatility_trend():
    df = pd.read_csv("data/extreme_analysis.csv", parse_dates=["Date"], index_col="Date")

    vol = df["Volatility"].dropna()
    X = np.arange(len(vol)).reshape(-1, 1)
    y = vol.values

    # Fit line
    model = LinearRegression()
    model.fit(X, y)
    trend = model.predict(X)

    plt.figure(figsize=(12, 5))
    plt.plot(vol.index, vol, alpha=0.5, label="Volatility")
    plt.plot(vol.index, trend, color="red", linewidth=2.0, label="Linear Trend")

    plt.title("Trend in 30-Day Rolling Volatility")
    plt.xlabel("Date")
    plt.ylabel("Volatility")
    plt.legend()
    plt.tight_layout()

    Path("figures").mkdir(exist_ok=True)
    plt.savefig("figures/figure6_volatility_trend.png", dpi=300)
    print("Saved figures/figure6_volatility_trend.png")

if __name__ == "__main__":
    plot_volatility_trend()
