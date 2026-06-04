# Refactor Case Study: From God File to Modular Strategy System

## Background

The project began as an AI-assisted trading prototype. Early development prioritized getting the system to run: paper trading, order placement, Telegram alerts, strategy iteration, and BTC mock trading.

As features accumulated, the strategy logic became concentrated in large strategy files. At one point, the system contained multi-thousand-line strategy files that behaved like “god files”: too many responsibilities, too many hidden dependencies, and too much risk for future maintenance.

## Problem

A monolithic strategy file creates several risks:

- Difficult to reason about strategy behavior
- High chance of accidental side effects during edits
- AI agents may modify unrelated sections while trying to implement a feature
- Harder to test small components
- Harder for a human maintainer to review logic
- Increased chance of duplicated utilities and repeated decision logic

## Refactoring goal

The goal was not to rewrite everything from scratch. The goal was to preserve existing behavior while improving structure.

Core principles:

- Keep function inputs and outputs stable where possible
- Split by responsibility, not by random file size
- Run tests after each meaningful change
- Use Git commits as restore points
- Let AI execute narrow tasks, but keep architecture decisions human-reviewed

## Dual-agent governance model

```mermaid
flowchart LR
    A[Advisor Agent] --> B[Architecture Plan]
    B --> C[Human Review]
    C --> D[Executor Agent]
    D --> E[Code Changes]
    E --> F[Tests / Git Commit]
    F --> C
```

- **Advisor Agent:** proposes refactoring plans, module boundaries, risks, and review questions.
- **Executor Agent:** performs approved edits in the codebase.
- **Human operator:** confirms the plan, checks output, requests tests, and controls Git commits.

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
- Tests were split into more focused modules.
- Telegram bot commands were separated from the core bot facade.
- BTC strategy modules were split into focused components.
- Future SQLite/SQLAlchemy migration became easier because data access boundaries were clearer.

## Lessons learned

1. AI can write code quickly, but architecture still needs human supervision.
2. A passing test suite is the best safety net for aggressive refactoring.
3. “One agent writes, another agent reviews” reduces blind spots.
4. Git commits are not optional; they are the recovery system.
5. Refactoring is not just about fewer lines; it is about clearer responsibility boundaries.
