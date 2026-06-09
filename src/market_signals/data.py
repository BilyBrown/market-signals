import pandas as pd


def load_shiller_data(path: str) -> pd.DataFrame:
    """Load and parse the Shiller ie_data.xls file into a clean monthly DataFrame.

    Returns a DataFrame indexed by datetime with columns:
        Value (TR CAPE), Rate GS10, P, D, E, CPI
    """
    pass
