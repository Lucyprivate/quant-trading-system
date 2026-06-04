# Quick Start

This guide shows how to run the **safe public demo**. It does not connect to IBKR, Longbridge, Telegram, Azure, or any live trading service.

## Prerequisites

* Python 3.10+
* Git
* No brokerage credentials required
* No API keys required
* No external Python dependencies required

## 1. Clone the repository

```bash
git clone https://github.com/Lucyprivate/quant-trading-system.git
cd quant-trading-system
```

## 2. Run the safe demo

```bash
python3 demo/toy_backtest.py --input demo/sample_market_data.csv
```

The demo uses a small CSV file and a simplified score-first trading flow:

```text
sample market data
    ↓
score-first filter
    ↓
risk guard
    ↓
mock order
    ↓
toy backtest summary
```

## 3. Optional: write outputs to CSV

```bash
python3 demo/toy_backtest.py \
  --input demo/sample_market_data.csv \
  --trades-out demo/trades_out.csv \
  --equity-out demo/equity_out.csv
```

## 4. Expected output

The exact numbers may change if you edit the sample data, but the current sample data should produce:

```text
Toy backtest summary
initial_cash: 10000.00
final_equity: 10081.25
trades: 8
open_positions: 0
```

## 5. What this demo proves

The demo is intentionally simple. It demonstrates the engineering shape of the private system without exposing proprietary strategy logic:

* CSV ingestion
* score-first trade filtering
* risk budget sizing
* mock order execution
* equity tracking
* trade log output

## 6. What this demo does not include

* Real IBKR connection
* Real market data
* Real order placement
* Real account state
* Proprietary alpha logic
* Telegram credentials
* Production risk parameters

## 7. Private system reference

The private project includes a fuller backtesting engine with options for:

* bid/ask gating
* slippage
* commissions
* partial fills
* order timeouts
* bracket exits
* daily kill switch
* market-data-source gates
* technical filters
* walk-forward parameter stability checks

Those features are documented here as an engineering case study, not published as a trading product.
