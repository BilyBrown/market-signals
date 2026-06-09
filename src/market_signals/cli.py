import sys
from pathlib import Path
import matplotlib.pyplot as plt

from .data import load_shiller_data
from .signals import compute_cape_momentum, compute_yield_gap
from .charts import plot_cape_momentum, plot_yield_gap

DATA_PATH = Path("data/ie_data.xls")
OUTPUT_PATH = Path("output")


def main():
    if not DATA_PATH.exists():
        print(f"Error: data file not found at {DATA_PATH}")
        print("Download ie_data.xls from http://www.econ.yale.edu/~shiller/data.htm")
        print("and place it in the data/ directory.")
        sys.exit(1)

    print("Loading data...")
    df = load_shiller_data(str(DATA_PATH))

    print("Computing signals...")
    df = compute_cape_momentum(df)
    df = compute_yield_gap(df)

    OUTPUT_PATH.mkdir(exist_ok=True)

    print("Generating charts...")
    fig1 = plot_cape_momentum(df)
    fig1.savefig(OUTPUT_PATH / "cape_momentum.png", dpi=150, bbox_inches="tight")

    fig2 = plot_yield_gap(df)
    fig2.savefig(OUTPUT_PATH / "yield_gap.png", dpi=150, bbox_inches="tight")

    print(f"Charts saved to {OUTPUT_PATH}/")
    plt.show()
