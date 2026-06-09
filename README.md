# market-signals

A Python package for analyzing equity market valuation and macroeconomic signals. Run it from the command line to generate charts on the current state of the market — data is downloaded automatically on each run.

---

## Installation

```bash
git clone https://github.com/BilyBrown/market-signals.git
cd market-signals
pip install .
```

## Usage

```bash
market-signals
```

That's it. The tool fetches the latest Shiller dataset, computes signals, saves two charts to `output/`, and displays them.

To run without installing (from the repo root):

```bash
python main.py
```

---

## What It Produces

### Chart 1 — TR CAPE Momentum
Tracks the S&P 500 Total Return CAPE ratio (1950–present) alongside a rolling Z-score of its 12-month rate of change, smoothed over 3 months.

- **Red shading** on the CAPE panel: momentum Z-score > +2 — valuation is rising at a historically abnormal pace
- **Green shading**: Z-score < −2 — CAPE is falling sharply relative to its recent history

### Chart 2 — Stocks vs. Bonds: The Battle for Yield
Compares the S&P 500 implied earnings yield (`1 / TR CAPE × 100`) against the 10-Year Treasury yield (GS10), with a rolling Z-score of the gap between them.

- A **negative yield gap** means bonds are paying more than the equity earnings yield
- **Red shading** on the yield panel: gap Z-score < −2 — stocks are historically expensive relative to bonds

---

## Data

All data is sourced from the [Shiller Online Data (Yale)](http://www.econ.yale.edu/~shiller/data.htm) — a single XLS file containing CAPE, TR CAPE, GS10, price, earnings, dividends, and CPI going back to 1871. It is downloaded fresh on each run.

---

## Project Structure

```
market-signals/
├── notebooks/              # original exploratory notebooks
├── src/market_signals/
│   ├── data.py             # download and parse Shiller data
│   ├── signals.py          # CAPE momentum and yield gap calculations
│   ├── charts.py           # chart generation
│   └── cli.py              # command-line entrypoint
├── output/                 # generated charts (gitignored)
└── main.py                 # dev entrypoint (python main.py)
```

---

## Roadmap

- [x] CAPE momentum signal with rolling Z-score
- [x] Stocks vs. bonds yield gap with rolling Z-score
- [x] Automated data refresh from Shiller's published XLS
- [ ] Streamlit dashboard
- [ ] Credit spread signal (HY OAS)
- [ ] Fed Funds rate overlay
- [ ] Equity risk premium model

---

## Requirements

Python 3.9+, pandas, matplotlib, openpyxl
