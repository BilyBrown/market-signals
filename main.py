"""Development entrypoint. Run from the repo root: python main.py

For the installed CLI command after `pip install .`, use: market-signals
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

from market_signals.cli import main

if __name__ == "__main__":
    main()
