# market-signals: Progress & Roadmap

## What This Is

A Python package that downloads the latest Shiller dataset and produces two market valuation signals:
1. **TR CAPE Momentum** — how fast the S&P 500's valuation is rising relative to its own history
2. **Stocks vs. Bonds Yield Gap** — whether equities are cheap or expensive relative to the 10-year Treasury

Runnable as a Streamlit dashboard or a command-line tool.

---

## Steps Completed

### 1. Exploratory Analysis (notebooks)
- Built two Jupyter notebooks (`market_play.ipynb`, `market_play_v2.ipynb`) exploring Shiller CAPE data
- `v2` is the primary version — uses TR CAPE and pulls GS10 directly from the Shiller file (no separate CSV needed)
- Both notebooks remain in `notebooks/` as reference

### 2. GitHub Repo
- Created public repo: `https://github.com/BilyBrown/market-signals`
- Pushed notebooks as initial commit

### 3. Package Structure
Scaffolded as an installable Python package:
```
market-signals/
├── notebooks/
├── src/market_signals/
│   ├── data.py             # download + parse Shiller data
│   ├── signals.py          # CAPE momentum, yield gap calculations
│   ├── charts.py           # matplotlib chart functions
│   ├── cli.py              # market-signals command
│   ├── app.py              # Streamlit dashboard
│   └── dashboard_runner.py # market-signals-dashboard command
├── output/                 # generated charts land here (gitignored)
├── data/                   # data files land here (gitignored)
├── main.py                 # dev entrypoint (python main.py)
└── pyproject.toml
```

### 4. Refactor
Extracted all logic from `market_play_v2.ipynb` into the package:
- `data.py` — parses Shiller's decimal date format (e.g. `1871.01`), returns clean DataFrame
- `signals.py` — 12m rate of change, 10yr rolling Z-score, 3-month smoothing, yield gap
- `charts.py` — two-panel matplotlib figures returned as objects (caller handles display/save)

### 5. Automated Data Download
- `download_shiller_data()` in `data.py` fetches the latest XLS from the Shiller host URL
- CLI and dashboard both call this automatically — no manual data steps for the user

### 6. Streamlit Dashboard
- Metrics row: TR CAPE, earnings yield, 10-yr treasury, yield gap, gap Z-score (with YoY deltas)
- Both charts displayed full-width
- Data cached for 1 hour; "Refresh Data" button clears cache
- Runs via: `python -m streamlit run src/market_signals/app.py --server.headless true`

### 7. Bugs Fixed Along the Way
- Relative imports in `app.py` broke when Streamlit ran it directly → fixed with `sys.path.insert`
- `main()` not called at module level → Streamlit rendered blank page → added `main()` call at bottom of `app.py`
- Missing `xlrd` dependency for `.xls` parsing → added to `pyproject.toml`
- Windows PATH issue: entry point `.exe` files install to an unlisted Scripts folder → workaround is `python -m streamlit run ...` directly

---

## How to Run

```bash
# Install
git clone https://github.com/BilyBrown/market-signals.git
cd market-signals
pip install .

# Dashboard
python -m streamlit run src/market_signals/app.py --server.headless true
# then open http://localhost:8501

# CLI (saves charts to output/)
python main.py
```

**Note on Windows PATH:** The `market-signals` and `market-signals-dashboard` commands are registered but may not be on PATH depending on your Python install. The commands above always work.

---

## Roadmap

- [x] CAPE momentum signal with rolling Z-score
- [x] Stocks vs. bonds yield gap with rolling Z-score
- [x] Automated data refresh from Shiller's published XLS
- [x] Streamlit dashboard with metrics and charts
- [ ] Fix Windows PATH issue so `market-signals-dashboard` works without the workaround
- [ ] Credit spread signal (HY OAS) — needs a FRED API data source
- [ ] Fed Funds rate overlay — available in the Shiller dataset (`Rate GS10` column has it, or FRED)
- [ ] Equity risk premium model
- [ ] Multi-page Streamlit app (one page per signal)

---

## Data

All data from Robert J. Shiller, *Irrational Exuberance*, Princeton University Press.
[econ.yale.edu/~shiller/data.htm](http://www.econ.yale.edu/~shiller/data.htm)
