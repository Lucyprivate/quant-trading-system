# Backtest Results — Redacted Template

This document is a safe template for publishing performance evidence without exposing proprietary trading logic.

## Publication policy

Do not publish:

- exact strategy thresholds
- exact position sizes
- live account balances
- raw trade logs
- unredacted timestamps that reveal execution patterns
- brokerage account identifiers

## Safe metric template

| Metric | Value |
| --- | --- |
| Asset universe | Redacted / examples only |
| Test mode | Paper trading / backtest |
| Period | YYYY-MM-DD to YYYY-MM-DD |
| Benchmark | QQQ / SPY / NASDAQ-style benchmark |
| Total return | Range or redacted |
| Max drawdown | Range or redacted |
| Sharpe ratio | Range or redacted |
| Win rate | Range or redacted |
| Number of trades | Range or redacted |
| Notes | Explain limitations and assumptions |

## Example wording

> The strategy was evaluated in paper-trading/backtesting mode using a private dataset and broker-compatible execution assumptions. Exact thresholds and trade logs are intentionally omitted. The main engineering result is not a public alpha claim, but a tested pipeline covering market data ingestion, signal gating, risk checks, mock/live-compatible execution paths, and reporting.

## Private backtest features documented in the source snapshot

The private backtesting documentation includes support for:

- slippage modeling
- fixed and bps commissions
- partial fills
- order timeout
- bracket exits
- daily max-loss kill switch
- market-data-source gates
- technical filters
- walk-forward parameter stability checks

These are more important for public credibility than publishing a single overfit return number.
