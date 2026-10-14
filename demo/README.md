# Demo

This directory contains a self-contained toy backtest. It does not connect to a broker or live market data service.

## Run

```bash
python3 demo/toy_backtest.py --input demo/sample_market_data.csv
```

## Optional outputs

```bash
python3 demo/toy_backtest.py   --input demo/sample_market_data.csv   --trades-out demo/trades_out.csv   --equity-out demo/equity_out.csv
```

## Purpose

The demo mirrors the shape of the private system:

1. Load market-like rows from CSV.
2. Apply a score-first gate.
3. Pass the trade through a simple risk guard.
4. Execute a mock order.
5. Track equity and trades.

This simple toy shows the workflow. It is not a real trading strategy.
