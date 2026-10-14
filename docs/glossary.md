<a id="ai-native-development"></a>

# Glossary

## Backtesting

A test of a trading strategy on historical data to evaluate its simulated behavior.

## Score-first gating

A trade-entry design where candidate trades must pass a scoring/filtering layer before entering execution logic.

## ML signal filter

A model-like scoring layer that filters low-quality trade signals before they reach the strategy engine.

## Risk guard

A safety layer that blocks or limits trades based on position size, exposure, cooldowns, or other constraints.

## God file

A large file with too many responsibilities. It is hard to maintain, review, and test.

## Paper trading

Simulated trading with market-like execution and no real capital at risk.

## SQLite

A lightweight relational database suitable for local storage and structured logs.

## SQLAlchemy

A Python ORM/library for structured database access. It reduces the need for raw SQL.

## Telegram bot

A bot used to send trading, runtime, and health-check notifications to a Telegram chat.
