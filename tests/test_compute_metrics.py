import pandas as pd
import numpy as np
from src.compute_metrics import rolling_volatility

def test_rolling_volatility_basic():
    prices = pd.Series([100, 102, 101, 103, 104, 106, 107])
    result = rolling_volatility(prices, window=3)
    returns = prices.pct_change()
    expected = returns.rolling(3, min_periods=3).std()
    assert np.allclose(result.dropna(), expected.dropna(), equal_nan=True)

def test_handles_short_series():
    prices = pd.Series([100, 101])
    result = rolling_volatility(prices, window=5)
    assert result.isna().all(), "Should return NaN when window > length"

def test_no_nan_after_window():
    prices = pd.Series(np.linspace(100, 200, 50))
    result = rolling_volatility(prices, window=10)
    assert result.iloc[10:].notna().all()
