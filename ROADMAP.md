# Roadmap

| Priority | Area | Status | Notes |
| --- | --- | --- | --- |
| P0 | SQLite / SQLAlchemy migration | In progress | Replace CSV/JSON runtime logs with structured relational storage. |
| P0 | Test preservation | In progress | Preserve behavior while refactoring storage and strategy modules. |
| P0 | Technical debt cleanup | In progress | Replace custom utility code with mature Python libraries where appropriate. |
| P1 | Safe public demo | Added | Provide a toy backtest that demonstrates architecture without broker access. |
| P1 | Architecture diagrams | Added / expanding | Maintain Mermaid diagrams for system flow. |
| P1 | Redacted backtest reporting | Template added | Publish safe ranges or sanitized examples without revealing alpha. |
| P1 | Refactor case study | Added | Explain the 2,000+ line strategy refactor. |
| P2 | Demo CI workflow | Added | Run the toy demo automatically with GitHub Actions. |
| P2 | Monitoring expansion | Planned | Add latency, slippage, runtime health, and structured summaries. |
| P2 | Containerized deployment | Planned | Dockerize services after core refactor stabilizes. |
| P3 | Live trading transition | Future | Only after paper-trading validation, risk review, and compliance checks. |
| P3 | GitHub Pages documentation | Future | Turn repository docs into a browsable project site. |
