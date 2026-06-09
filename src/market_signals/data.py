import urllib.request
from pathlib import Path

import pandas as pd

SHILLER_URL = (
    "https://img1.wsimg.com/blobby/go/e5e77e0b-59d1-44d9-ab25-4763ac982e53"
    "/downloads/c9b8cf0f-f01a-49f5-9ea5-d19443390ab2/ie_data.xls?ver=1780495520681"
)


def download_shiller_data(dest: str = "data/ie_data.xls", url: str = SHILLER_URL) -> None:
    """Download the latest Shiller ie_data.xls to dest.

    Args:
        dest: Local path to save the file. Parent directory is created if needed.
        url: Direct download URL. Defaults to the current Shiller data host.
    """
    Path(dest).parent.mkdir(parents=True, exist_ok=True)
    urllib.request.urlretrieve(url, dest)


def load_shiller_data(path: str, start_year: str = "1950") -> pd.DataFrame:
    """Load and parse the Shiller ie_data.xls file into a clean monthly DataFrame.

    The raw file encodes dates as floats (e.g. 1871.01 = Jan 1871). This function
    parses that format, sets a proper DatetimeIndex, and returns only the columns
    used downstream.

    Args:
        path: Path to ie_data.xls, available from http://www.econ.yale.edu/~shiller/data.htm
        start_year: Exclude rows before this year. Defaults to "1950" (post-war era).

    Returns:
        DataFrame indexed by date with columns:
            tr_cape, gs10, price, earnings, dividends, cpi
    """
    raw = pd.read_excel(path, sheet_name="Data", header=7)
    raw = raw[~raw["Date"].isna()].copy()

    year = raw["Date"].astype(int)
    # Multiply by 100 and take modulo to extract month, rounding to handle
    # floating-point imprecision (e.g. 1871.1 * 100 = 187110.00000000003)
    month = (raw["Date"] * 100 % 100).round().astype(int).clip(lower=1)
    raw.index = pd.to_datetime(year.astype(str) + "-" + month.astype(str) + "-01")
    raw.index.name = "date"

    raw = raw[raw.index >= start_year].sort_index()

    return pd.DataFrame(
        {
            "tr_cape": pd.to_numeric(raw["TR CAPE"], errors="coerce"),
            "gs10": pd.to_numeric(raw["Rate GS10"], errors="coerce"),
            "price": pd.to_numeric(raw["P"], errors="coerce"),
            "earnings": pd.to_numeric(raw["E"], errors="coerce"),
            "dividends": pd.to_numeric(raw["D"], errors="coerce"),
            "cpi": pd.to_numeric(raw["CPI"], errors="coerce"),
        },
        index=raw.index,
    )
