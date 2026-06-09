from src.market_signals.data import load_shiller_data
from src.market_signals.signals import compute_cape_momentum, compute_yield_gap
from src.market_signals.charts import plot_cape_momentum, plot_yield_gap
import matplotlib.pyplot as plt

DATA_PATH = "data/ie_data.xls"


def main():
    df = load_shiller_data(DATA_PATH)
    df = compute_cape_momentum(df)
    df = compute_yield_gap(df)

    plot_cape_momentum(df)
    plot_yield_gap(df)
    plt.show()


if __name__ == "__main__":
    main()
