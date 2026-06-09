import matplotlib.pyplot as plt
import pandas as pd


def plot_cape_momentum(df: pd.DataFrame, smoothing: int = 3) -> plt.Figure:
    """Two-panel chart: TR CAPE level (top) with momentum Z-score signal (bottom).

    Shades the CAPE panel red where smoothed Z > 2 (overheating) and
    green where smoothed Z < -2 (deep value).

    Args:
        df: DataFrame after compute_cape_momentum, must contain tr_cape,
            rolling_zscore, and smoothed_z columns.
        smoothing: Smoothing period used, shown in the legend label.

    Returns:
        matplotlib Figure.
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 9), sharex=True)

    ax1.plot(df.index, df["tr_cape"], color="black", alpha=0.7, label="TR CAPE")
    ax1.set_title("S&P 500 TR CAPE: Smoothed Rolling Z-Score Analysis", fontsize=14)
    ax1.set_ylabel("TR CAPE")
    ax1.grid(alpha=0.2)

    ax2.plot(df.index, df["rolling_zscore"], color="blue", alpha=0.2, label="Raw Z-Score")
    ax2.plot(df.index, df["smoothed_z"], color="blue", lw=2, label=f"{smoothing}-Mo Smoothed Z")
    ax2.axhline(0, color="black", lw=1)
    ax2.axhline(2, color="red", linestyle="--")
    ax2.axhline(-2, color="green", linestyle="--")
    ax2.fill_between(df.index, 2, 4, color="red", alpha=0.1)
    ax2.fill_between(df.index, -2, -4, color="green", alpha=0.1)
    ax2.set_ylabel("Z-Score (12m RoC)")
    ax2.legend(loc="upper left")

    for i in range(1, len(df)):
        z = df["smoothed_z"].iloc[i]
        if pd.isna(z):
            continue
        if z > 2:
            ax1.axvspan(df.index[i - 1], df.index[i], color="red", alpha=0.3)
        elif z < -2:
            ax1.axvspan(df.index[i - 1], df.index[i], color="green", alpha=0.3)

    plt.tight_layout()
    return fig


def plot_yield_gap(df: pd.DataFrame) -> plt.Figure:
    """Two-panel chart: earnings yield vs bond yield (top), yield gap Z-score (bottom).

    Shades the yield panel red where gap Z-score < -2, marking periods where stocks
    are historically expensive relative to bonds.

    Args:
        df: DataFrame after compute_yield_gap, must contain earnings_yield,
            gs10, and gap_zscore columns.

    Returns:
        matplotlib Figure.
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    ax1.plot(df.index, df["earnings_yield"], label="S&P 500 Earnings Yield", color="blue", lw=1.5)
    ax1.plot(df.index, df["gs10"], label="10-Year Treasury Yield", color="orange", lw=1.5, linestyle="--")
    ax1.set_title("Stocks vs. Bonds: The Battle for Yield", fontsize=14)
    ax1.set_ylabel("Yield (%)")
    ax1.legend()
    ax1.grid(alpha=0.2)

    ax2.plot(df.index, df["gap_zscore"], color="purple", label="Yield Gap Z-Score")
    ax2.axhline(0, color="black", lw=1)
    ax2.axhline(2, color="green", linestyle="--", label='Stocks "Cheap" vs Bonds')
    ax2.axhline(-2, color="red", linestyle="--", label='Stocks "Expensive" vs Bonds')
    ax2.fill_between(df.index, -2, -4, color="red", alpha=0.1)
    ax2.set_ylabel("Z-Score (10yr rolling)")
    ax2.legend(loc="lower left")

    for i in range(1, len(df)):
        z = df["gap_zscore"].iloc[i]
        if pd.isna(z):
            continue
        if z < -2:
            ax1.axvspan(df.index[i - 1], df.index[i], color="red", alpha=0.2)

    plt.tight_layout()
    return fig
