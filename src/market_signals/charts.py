import matplotlib.pyplot as plt
import pandas as pd


def plot_cape_momentum(df: pd.DataFrame) -> plt.Figure:
    """Two-panel chart: TR CAPE level (top) with momentum Z-score signal (bottom).

    Red shading on CAPE panel where Z > 2 (overheating).
    Green shading where Z < -2 (deep value).
    """
    pass


def plot_yield_gap(df: pd.DataFrame) -> plt.Figure:
    """Two-panel chart: earnings yield vs bond yield (top), yield gap Z-score (bottom).

    Red shading on yield panel where gap Z-score < -2 (stocks expensive vs bonds).
    """
    pass
