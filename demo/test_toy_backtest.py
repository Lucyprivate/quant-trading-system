import unittest
from pathlib import Path

from toy_backtest import load_rows, run_backtest


class ToyBacktestTest(unittest.TestCase):
    def test_toy_backtest_runs(self):
        rows = load_rows(Path(__file__).with_name("sample_market_data.csv"))
        trades, equity, final_equity = run_backtest(rows)
        self.assertTrue(rows)
        self.assertTrue(trades)
        self.assertTrue(equity)
        self.assertGreater(final_equity, 0)


if __name__ == "__main__":
    unittest.main()
