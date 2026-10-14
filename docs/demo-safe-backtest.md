# Safe Demo Backtest

The public demo runs without exposing private trading logic.

## Why a toy demo?

The private project contains broker integrations, Telegram monitoring, strategy logic, and runtime state. Publishing those details would create security and strategy-leak risks.

The demo therefore focuses on the **engineering pattern**:

```mermaid
flowchart LR
    A[CSV Rows] --> B[Score-first Gate]
    B --> C[Risk Guard]
    C --> D[Mock Order]
    D --> E[Trade Log]
    D --> F[Equity Curve]
```

<a id="what-it-demonstrates"></a>

## What the demo shows

- Load a market row
- Gate a trade with an ML-like score threshold
- Limit order size with a simple risk budget
- Produce trade/equity outputs from mock orders
- Keep real strategy logic private while giving readers a runnable example

## What it intentionally omits

- IBKR connection
- Longbridge API calls
- Telegram bot credentials
- Live orders
- Real strategy parameters
- Real account balances or positions

## Run command

```bash
python3 demo/toy_backtest.py --input demo/sample_market_data.csv
```

## Optional outputs

```bash
python3 demo/toy_backtest.py   --input demo/sample_market_data.csv   --trades-out demo/trades_out.csv   --equity-out demo/equity_out.csv
```

## Next improvement

A future public demo could add:

- SQLite output
- parameter configuration
- chart generation
- sample unit tests
- GitHub Actions workflow validation
