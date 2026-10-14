# Refactor Case Study: From God File to Modular Strategy System

## Background

The project started as a trading prototype. Early work covered paper trading, order placement, Telegram alerts, strategy iteration, and BTC mock trading.

As features grew, strategy logic accumulated in large files. Some multi-thousand-line strategy files became “god files” with too many responsibilities and hidden dependencies. That concentration increased maintenance risk.

## Problem

A monolithic strategy file creates several risks:

- Difficult to reason about strategy behavior
- High chance of accidental side effects during edits
- Feature edits can change unrelated sections
- Harder to test small components
- Harder for a human maintainer to review logic
- Increased chance of duplicated utilities and repeated decision logic

<a id="dual-agent-governance-model"></a>

## Refactoring goal

The refactor aimed to preserve existing behavior and improve structure. It did not replace the whole system.

Core principles:

- Keep function inputs and outputs stable where possible
- Split by responsibility, not by random file size
- Run tests after each meaningful change
- Use Git commits as restore points
- Limit each edit to a narrow task and review architecture decisions

## Before

```text
src/strategies/
├── stock_strategy.py   # large compatibility entrypoint and shared helpers
└── btc_strategy.py     # large BTC strategy facade and wrappers
```

Typical problems:

- Data access mixed with signal logic
- Strategy rules mixed with execution details
- Reporting and formatting mixed with trading decisions
- Hard-to-test functions
- Duplicated helper logic

## After

```text
src/strategies/
├── stock_strategy.py
├── stock_decision.py
├── stock_runtime.py
├── stock_score.py
├── btc_strategy.py
├── btc_decision.py
├── btc_runtime.py
├── btc_score.py
└── strategy_config.py

src/bots/
├── telegram_bot.py
├── router.py
├── ib_connection.py
└── commands/
    ├── config.py
    ├── market_data.py
    ├── orders.py
    ├── portfolio.py
    └── status.py
```

## Results

- Strategy logic became easier to navigate.
- Tests moved into focused modules.
- Telegram bot commands moved out of the core bot facade.
- BTC strategy modules became focused components.
- Future SQLite/SQLAlchemy migration became easier because data access boundaries were clearer.

## Lessons learned

1. Review architecture decisions.
2. A passing test suite is the best safety net for aggressive refactoring.
3. Separate editing from review to reduce blind spots.
4. Keep Git commits as recovery points.
5. Refactor for clear responsibilities, not only fewer lines.
