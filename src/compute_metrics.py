import pandas as pd

def rolling_volatility(prices: pd.Series, window: int = 30) -> pd.Series:
    """Compute rolling standard deviation of daily returns."""
    returns = prices.pct_change()
    return returns.rolling(window, min_periods=window).std()
