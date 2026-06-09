import sys
import tempfile
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

sys.path.insert(0, str(Path(__file__).parent.parent))

from market_signals.data import download_shiller_data, load_shiller_data
from market_signals.signals import compute_cape_momentum, compute_yield_gap
from market_signals.charts import plot_cape_momentum, plot_yield_gap

st.set_page_config(page_title="Market Signals", layout="wide")

_DATA_DIR = Path(tempfile.gettempdir()) / "market_signals"


@st.cache_data(ttl=3600, show_spinner=False)
def get_data() -> pd.DataFrame:
    _DATA_DIR.mkdir(exist_ok=True)
    path = _DATA_DIR / "ie_data.xls"
    download_shiller_data(str(path))
    df = load_shiller_data(str(path))
    df = compute_cape_momentum(df)
    df = compute_yield_gap(df)
    return df


def main():
    st.title("Market Signals")
    st.caption("S&P 500 valuation analysis — data refreshes automatically every hour")

    with st.spinner("Loading latest Shiller data..."):
        df = get_data()

    # Latest non-null values for each metric
    latest_cape = df["tr_cape"].dropna().iloc[-1]
    latest_gs10 = df["gs10"].dropna().iloc[-1]
    latest_ey = df["earnings_yield"].dropna().iloc[-1]
    latest_gap = df["yield_gap"].dropna().iloc[-1]
    latest_gap_z = df["gap_zscore"].dropna().iloc[-1]

    # Prior-year values for deltas (closest available date ~12 months back)
    latest_date = df["tr_cape"].dropna().index[-1]
    prior_date = latest_date - pd.DateOffset(years=1)
    prior_cape = df["tr_cape"].asof(prior_date)
    prior_gs10 = df["gs10"].asof(prior_date)

    # --- Metrics row ---
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("TR CAPE", f"{latest_cape:.1f}", f"{latest_cape - prior_cape:+.1f} vs. 1yr ago")
    c2.metric("Earnings Yield", f"{latest_ey:.2f}%")
    c3.metric("10-Yr Treasury", f"{latest_gs10:.2f}%", f"{latest_gs10 - prior_gs10:+.2f}% vs. 1yr ago")
    c4.metric("Yield Gap", f"{latest_gap:.2f}%")
    c5.metric("Gap Z-Score (10yr)", f"{latest_gap_z:.2f}")

    st.divider()

    # --- Charts ---
    fig1 = plot_cape_momentum(df)
    st.pyplot(fig1)
    plt.close(fig1)

    fig2 = plot_yield_gap(df)
    st.pyplot(fig2)
    plt.close(fig2)

    st.divider()

    if st.button("Refresh Data"):
        st.cache_data.clear()
        st.rerun()

    st.caption(
        "Data: Robert J. Shiller, *Irrational Exuberance*, Princeton University Press. "
        "[econ.yale.edu/~shiller/data.htm](http://www.econ.yale.edu/~shiller/data.htm)"
    )


main()
