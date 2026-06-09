import pandas as pd


def compute_cape_momentum(
    df: pd.DataFrame, window: int = 120, smoothing: int = 3
) -> pd.DataFrame:
    """Compute 12-month rate of change of TR CAPE, rolling Z-score, and smoothed signal.

    Args:
        df: DataFrame from load_shiller_data, must contain tr_cape column.
        window: Rolling window in months for Z-score normalization. Default 120 (10 years).
        smoothing: Window in months to smooth the rolling Z-score. Default 3.

    Returns:
        DataFrame with added columns:
            roc_12m, rolling_mu, rolling_sigma, rolling_zscore, smoothed_z
    """
    df = df.copy()
    df["roc_12m"] = df["tr_cape"].pct_change(periods=12)
    df["rolling_mu"] = df["roc_12m"].rolling(window=window).mean()
    df["rolling_sigma"] = df["roc_12m"].rolling(window=window).std()
    df["rolling_zscore"] = (df["roc_12m"] - df["rolling_mu"]) / df["rolling_sigma"]
    df["smoothed_z"] = df["rolling_zscore"].rolling(window=smoothing).mean()
    return df


def compute_yield_gap(df: pd.DataFrame, window: int = 120) -> pd.DataFrame:
    """Compute the earnings yield vs GS10 yield gap and its rolling Z-score.

    Earnings yield = (1 / TR CAPE) * 100. A negative gap means bonds are paying
    more than the implied equity earnings yield.

    Args:
        df: DataFrame from load_shiller_data, must contain tr_cape and gs10 columns.
        window: Rolling window in months for Z-score normalization. Default 120 (10 years).

    Returns:
        DataFrame with added columns:
            earnings_yield, yield_gap, gap_mu, gap_sigma, gap_zscore
    """
    df = df.copy()
    df["earnings_yield"] = (1 / df["tr_cape"]) * 100
    df["yield_gap"] = df["earnings_yield"] - df["gs10"]
    df["gap_mu"] = df["yield_gap"].rolling(window=window).mean()
    df["gap_sigma"] = df["yield_gap"].rolling(window=window).std()
    df["gap_zscore"] = (df["yield_gap"] - df["gap_mu"]) / df["gap_sigma"]
    return df
