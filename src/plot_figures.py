# firstplot.py
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

TICKER = "AAPL"
START = "2015-01-01"
END   = "2025-10-21"

# Force classic columns and keep 'Adj Close' present
df = yf.download(
    TICKER,
    start=START,
    end=END,
    auto_adjust=False,        # keep 'Adj Close'
    group_by="column",        # avoid MultiIndex
    progress=False
)

# Robustly pick the price series (works even if your env still returns MultiIndex)
if isinstance(df.columns, pd.MultiIndex):
    # pick level-0 name 'Adj Close' or fall back to 'Close'
    cols0 = df.columns.get_level_values(0)
    if "Adj Close" in cols0:
        price = df.xs("Adj Close", axis=1, level=0).squeeze()
    else:
        price = df.xs("Close", axis=1, level=0).squeeze()
else:
    price = df["Adj Close"] if "Adj Close" in df.columns else df["Close"]

# Compute returns + 30-day rolling volatility
ret = price.pct_change()
rolling_vol = ret.rolling(30, min_periods=30).std()

# Plot
fig, ax1 = plt.subplots(figsize=(10, 5))
ax1.plot(price.index, price, label=f"{TICKER} Adj Close ($)")
ax1.set_xlabel("Date")
ax1.set_ylabel("Price ($)")

ax2 = ax1.twinx()
ax2.plot(rolling_vol.index, rolling_vol, label="30-day Rolling Volatility")
ax2.set_ylabel("Volatility")

plt.title(f"{TICKER} Price and 30-day Rolling Volatility ({START}–{END})")
fig.tight_layout()
plt.savefig("/Users/ronniejoe/Library/Mobile Documents/com~apple~CloudDocs/CMSC 6950 Project/figures", dpi=300)
print("Saved figures/figure1.png")
