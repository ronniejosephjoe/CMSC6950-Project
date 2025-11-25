# CMSC6950 Final Project – Apple Stock Volatility and Extreme Returns

**Student:** Ronie Joe
**Course:** CMSC 6950 – Fall 2025  
**Instructor:** Dr. Scott MacLachlan 

---

## 🔍 Project Overview
This project analyzes **Apple Inc. (AAPL)** daily stock prices from **2015–2025**, obtained from the official [Yahoo Finance](https://finance.yahoo.com/quote/AAPL) API.  
The goal is to study **volatility and extreme-value behavior** in stock returns.

---

## 📈 Planned Analysis
1. Compute daily returns and 30-day rolling volatility.  
2. Identify **extreme returns** (|r| > 3σ or >95th percentile).  
3. Compute statistics on frequency and magnitude of extremes.  
4. Evaluate volatility and extreme-event trends over time.  
5. Sensitivity analysis for different thresholds (2σ vs. 3σ vs. percentile).

---

## Repository Structure
cmsc6950-final-apple-volatility/
│
├── README.md
├── requirements.txt
│
├── data/
│   ├── AAPL.csv
│   └── extreme_analysis.csv
│
├── figures/
│   ├── figure1_price_and_volatility.png
│   ├── figure2_daily_returns.png
│   ├── figure3_rolling_volatility.png
│   └── figure4_extreme_returns.png
│
├── src/
│   ├── fetch_data.py
│   ├── compute_metrics.py
│   ├── plot_daily_returns.py
│   ├── plot_rolling_volatility.py
│   ├── analyze_extremes.py
│   └── plot_extremes.py
│
└── tests/
    └── test_compute_metrics.py

---

## ⚙️ Installation & Reproducibility

# Install required Python packages:
pip install -r requirements.txt

# 🔽 1. Fetch the Data
Downloads AAPL daily data and writes data/AAPL.csv:
``` python -m src.fetch_data```
# 📉 2. Generate Figure 1 — Price + Rolling Volatility
```python -m src.plot_rolling_volatility```
Creates:
figures/figure1_price_and_volatility.png
# 📉 3. Generate Figure 2 — Daily Returns
```python -m src.plot_daily_returns```
Creates:
figures/figure2_daily_returns.png
# 📈 4. Generate Figure 3 — Rolling Volatility Only
```python -m src.plot_rolling_volatility```
Creates:
figures/figure3_rolling_volatility.png
# 🚨 5. Extreme Value Analysis (2σ, 3σ, 95th percentile)
Compute extreme values
```python -m src.analyze_extremes```
Generates:
data/extreme_analysis.csv
Plot extreme return events
```python -m src.plot_extremes```
Creates:
figures/figure4_extreme_returns.png





## 🧾 References
- Yahoo Finance API (via `yfinance`)
- Pandas Documentation
- Matplotlib Library



