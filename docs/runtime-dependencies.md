# Runtime Dependencies — Private System Reference

The private Git snapshot included a compact `requirements.txt`:

```text
ib_async==2.1.0
python-dotenv==1.2.2
requests==2.34.2
pandas_market_calendars
```

## Notes

- `ib_async` supports asynchronous IBKR interaction.
- `python-dotenv` loads local runtime configuration.
- `requests` supports HTTP calls such as Telegram API interactions.
- `pandas_market_calendars` supports exchange calendar logic.

The public demo does not require these dependencies because it intentionally avoids live broker/API access.
