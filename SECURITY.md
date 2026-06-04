# Security Policy

This repository documents a personal trading system and does **not** contain live trading source code, production credentials, or proprietary strategy parameters.

## Redaction policy

The following information is intentionally excluded:

- API keys and access tokens
- IBKR account identifiers
- Real account balances or positions
- Proprietary trading thresholds
- Live execution parameters
- Raw Telegram screenshots containing personal data
- Exact strategy rules that could expose trading edge
- Broker session configuration
- Private `.env` files

## Safe publication rules

- Never commit `.env` files.
- Never commit screenshots unless account data and tokens are fully redacted.
- Never publish private keys, webhook URLs, chat IDs, or broker session information.
- Keep trading strategy parameters and production execution logic private.
- Treat all logs as sensitive until reviewed and redacted.

## Disclaimer

Nothing in this repository constitutes financial advice, investment advice, or a recommendation to trade any asset. Any trading system must be tested carefully and used at the operator's own risk.

## Reporting issues

If you find a security issue in the public documentation, please open an issue or contact the repository owner.
