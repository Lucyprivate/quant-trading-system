#!/usr/bin/env python3
"""
Safe toy backtest for the public case-study repository.

This script intentionally avoids broker APIs, live market data, account state,
Telegram credentials, and proprietary trading logic. It demonstrates the
engineering shape of the private system:

CSV data -> score-first filter -> risk guard -> mock order -> summary.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class MarketRow:
    date: str
    symbol: str
    asset_class: str
    price: float
    reference_close: float
    ml_score: float
    spread_pct: float


@dataclass
class Position:
    symbol: str
    quantity: float
    entry_price: float
    asset_class: str


def load_rows(path: Path) -> list[MarketRow]:
    rows: list[MarketRow] = []
    with path.open(newline="", encoding="utf-8") as f:
        for raw in csv.DictReader(f):
            rows.append(
                MarketRow(
                    date=raw["date"],
                    symbol=raw["symbol"].upper(),
                    asset_class=raw["asset_class"].upper(),
                    price=float(raw["price"]),
                    reference_close=float(raw["reference_close"]),
                    ml_score=float(raw["ml_score"]),
                    spread_pct=float(raw["spread_pct"]),
                )
            )
    return rows


def score_first_gate(row: MarketRow, min_score: float = 0.65) -> tuple[bool, str]:
    if row.ml_score < min_score:
        return False, f"score {row.ml_score:.2f} below threshold {min_score:.2f}"
    if row.price > row.reference_close * 0.995:
        return False, "price is not at a sufficient pullback"
    if row.spread_pct > 0.20:
        return False, "spread too wide"
    return True, "score, pullback, and spread checks passed"


def risk_guard(cash: float, row: MarketRow, max_notional: float = 1_000.0) -> tuple[float, str]:
    notional = min(cash, max_notional)
    if row.asset_class == "CRYPTO":
        notional = min(notional, 200.0)
        quantity = round(notional / row.price, 6)
    else:
        quantity = int(notional // row.price)

    if quantity <= 0:
        return 0.0, "insufficient cash or position size below minimum"

    return float(quantity), f"approved quantity={quantity}"


def mark_to_market(cash: float, positions: dict[str, Position], latest_prices: dict[str, float]) -> float:
    equity = cash
    for position in positions.values():
        price = latest_prices.get(position.symbol, position.entry_price)
        equity += position.quantity * price
    return equity


def run_backtest(rows: list[MarketRow]) -> tuple[list[dict], list[dict], float]:
    initial_cash = 10_000.0
    cash = initial_cash
    positions: dict[str, Position] = {}
    latest_prices: dict[str, float] = {}
    trades: list[dict] = []
    equity_curve: list[dict] = []

    for row in rows:
        latest_prices[row.symbol] = row.price

        position = positions.get(row.symbol)
        if position:
            take_profit = row.price >= position.entry_price * 1.02
            stop_loss = row.price <= position.entry_price * 0.97
            if take_profit or stop_loss:
                proceeds = position.quantity * row.price
                cash += proceeds
                reason = "take_profit" if take_profit else "stop_loss"
                trades.append({
                    "date": row.date,
                    "symbol": row.symbol,
                    "action": "SELL",
                    "quantity": position.quantity,
                    "price": row.price,
                    "reason": reason,
                })
                del positions[row.symbol]

        if row.symbol not in positions:
            allowed, gate_reason = score_first_gate(row)
            if allowed:
                qty, risk_reason = risk_guard(cash, row)
                if qty > 0:
                    notional = qty * row.price
                    cash -= notional
                    positions[row.symbol] = Position(
                        symbol=row.symbol,
                        quantity=qty,
                        entry_price=row.price,
                        asset_class=row.asset_class,
                    )
                    trades.append({
                        "date": row.date,
                        "symbol": row.symbol,
                        "action": "BUY",
                        "quantity": qty,
                        "price": row.price,
                        "reason": f"{gate_reason}; {risk_reason}",
                    })

        equity_curve.append({
            "date": row.date,
            "equity": round(mark_to_market(cash, positions, latest_prices), 2),
            "cash": round(cash, 2),
            "open_positions": len(positions),
        })

    final_equity = mark_to_market(cash, positions, latest_prices)
    return trades, equity_curve, final_equity


def write_csv(path: Path, rows: list[dict]) -> None:
    if not rows:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a safe toy score-first backtest.")
    parser.add_argument("--input", type=Path, required=True, help="CSV input path")
    parser.add_argument("--trades-out", type=Path, help="Optional trades CSV output path")
    parser.add_argument("--equity-out", type=Path, help="Optional equity CSV output path")
    args = parser.parse_args()

    rows = load_rows(args.input)
    trades, equity_curve, final_equity = run_backtest(rows)

    if args.trades_out:
        write_csv(args.trades_out, trades)
    if args.equity_out:
        write_csv(args.equity_out, equity_curve)

    print("Toy backtest summary")
    print(f"initial_cash: {10000.00:.2f}")
    print(f"final_equity: {final_equity:.2f}")
    print(f"trades: {len(trades)}")
    print(f"open_positions: {equity_curve[-1]['open_positions'] if equity_curve else 0}")


if __name__ == "__main__":
    main()
