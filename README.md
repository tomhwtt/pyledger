# pyLedger 🧾  
A frameworkless Python ledger application designed around clean architecture and Domain-Driven Design principles.

## 🧭 Overview

`pyLedger` is a personal exploration of writing a well-structured Python application without relying on Django, Flask, or other web frameworks. It focuses on re-engaging with foundational Python concepts: class design, abstraction, service orchestration, and explicit architecture boundaries.

## 🧠 Motivation

As someone who works primarily with Django and serverless architecture (e.g., Lambdas), I wanted to build something from scratch that emphasizes:

- Plain Python class design
- Domain logic isolated from infrastructure
- Clear boundaries between services, repositories, and orchestration layers

The code is organized around clear responsibilities and well-defined layers, following Domain-Driven Design patterns like services, entities, and repositories — while keeping the overall structure lightweight and easy to understand.

### 🧱 Architecture

- `pyledger/domain/` — Core business entities and logic
- `pyledger/services/` — Application-level service logic
- `pyledger/repository/` — Abstract and SQLAlchemy repositories for each domain entity
- `pyledger/adapters/` — SQLAlchemy ORM mappings
- `pyledger/db.py` — Database engine and session setup
- `pyledger/orchestrator.py` — Coordinates high-level workflows
- `pyledger/repl.py` — REPL for local experimentation
- `create_tables.py` — Initializes database schema
- `tests/` — Unit and integration tests (in progress)

## 🧩 Key Features

- Account creation and transaction posting (credit/debit)
- Balance calculation with both in-memory and SQLAlchemy repositories
- Domain validation (e.g. amounts must be positive)
- Flexible architecture for plugging in CLI, web, or API layers in the future

## 🧪 Testing

The app is being developed with `pytest`, with a focus on testability at both the unit and service levels. Tests will expand as features are added.

## 🧰 Tech Stack

- Python 3.10+
- SQLAlchemy
- PostgreSQL (via Docker, optional)
- Pytest (in progress)

## 🔭 Roadmap

- Redis-based concurrency locking to demonstrate in-memory coordination
- Pending transactions support
- CLI interface or minimal web adapter
- PostgreSQL migrations
- More robust testing and edge-case handling

## 🚀 Running Locally (with Docker)

```
# Start the Postgres database
docker-compose up -d

# Create the tables
python create_tables.py

# Open an interactive Python REPL
python -m -i pyledger.repl
```
### Once inside the REPL
You can run commands like:
```
from pyledger.domain.transaction import TransactionType

user = user_service.create_user("user", "user@example.com")
session.commit()

account = account_service.create_account(user.id)
session.commit()

tx1 = transaction_service.create_transaction(account.id, TransactionType.CREDIT, 50.00)
tx2 = transaction_service.create_transaction(account.id, TransactionType.DEBIT, $25.00)
session.commit()
```

## 💬 Notes

This is a work in progress. I'm building it iteratively with an eye toward learning, clarity, and extensibility. If you're reviewing the repo and curious about anything specific, feel free to reach out.

