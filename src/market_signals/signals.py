import pandas as pd


def compute_cape_momentum(df: pd.DataFrame, window: int = 120, smoothing: int = 3) -> pd.DataFrame:
    """Compute 12-month rate of change of TR CAPE, rolling Z-score, and smoothed signal.

    Adds columns: roc_12m, rolling_mu, rolling_sigma, rolling_zscore, smoothed_z
    """
    pass


def compute_yield_gap(df: pd.DataFrame, window: int = 120) -> pd.DataFrame:
    """Compute earnings yield vs GS10 yield gap and its rolling Z-score.

    Adds columns: earnings_yield, yield_gap, gap_mu, gap_sigma, gap_zscore
    """
    pass
