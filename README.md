# market-signals

A collection of Python notebooks for analyzing equity market valuation and macroeconomic signals. The goal is to build this out into a runnable reporting tool that surfaces key market regime indicators.

---

## Current Notebooks

### `market_play_v2.ipynb` *(primary)*
Loads the full [Shiller dataset](http://www.econ.yale.edu/~shiller/data.htm) directly and runs three analyses:

1. **CAPE Level** — Plots the Total Return CAPE ratio (1950–present) against ±1 standard deviation bands from the historical mean (~17.4).

2. **CAPE Momentum Signal** — Computes the 12-month rate of change of TR CAPE, Z-scores it against a rolling 10-year window, and smooths the signal over 3 months. Periods where the Z-score exceeds ±2 are highlighted on the CAPE chart as overheating (red) or deep value (green) regimes.

3. **Stocks vs. Bonds: Yield Gap** — Converts TR CAPE to an implied earnings yield (`1/CAPE × 100`) and compares it against the embedded 10-Year Treasury rate (GS10). The yield gap (`earnings yield − bond yield`) is Z-scored against a rolling 10-year window. A Z-score below −2 flags periods where bonds are historically expensive relative to equities.

### `market_play.ipynb` *(earlier version)*
Same analysis structure but uses two separate flat files (`stock_shiller-pe.xlsx` and `GS10.csv`) and standard CAPE rather than TR CAPE. Covers data back to 1871. Note: the GS10 series loaded from `GS10.csv` is redundant — it is already embedded in the Shiller dataset as `Rate GS10`.

---

## Data Sources

All data comes from a single source: the [Shiller Online Data (Yale)](http://www.econ.yale.edu/~shiller/data.htm) — `ie_data.xls`. This file contains CAPE, TR CAPE, GS10, price, earnings, dividends, and CPI going back to 1871.

---

## Current Signal (as of May 2026)

| Metric | Value |
|---|---|
| TR CAPE | ~42 |
| S&P 500 Earnings Yield | ~2.4% |
| 10-Year Treasury Yield | ~4.45% |
| Yield Gap | −2.08% |
| Yield Gap Z-Score (10yr rolling) | −1.65 |

Stocks are yielding roughly half what 10-year Treasuries pay on an earnings basis. The yield gap Z-score is approaching but has not yet crossed the −2 threshold that historically marks the most stretched stock-vs-bond regimes.

---

## Roadmap

- [ ] Automate data refresh via FRED API and Shiller's published XLS
- [ ] Build a Streamlit dashboard to replace notebook execution
- [ ] Add credit spread signal (HY OAS)
- [ ] Add Fed Funds rate overlay
- [ ] Equity risk premium model

---

## Requirements

```
pandas
matplotlib
openpyxl
```
