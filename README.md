# Customer360 AI Analyst

An AI-powered analytics application that allows users to query a Customer 360 database using natural language.

The application converts user questions into safe SQL queries using a Large Language Model (LLM), executes the queries against a read-only SQLite database, and returns both structured results and a natural-language business summary.

---

## Design Goals

This project was built to explore modern AI-assisted backend development while following software engineering best practices.

Key design goals include:

- Clear separation of responsibilities (Single Responsibility Principle)
- Safe SQL generation and validation
- Read-only database access
- Modular and maintainable architecture
- Testable components
- Natural-language business analytics

---

## Features

Current features include:

- Natural-language questions powered by OpenAI
- Automatic SQL generation
- SQL safety validation
- Read-only SQLite execution
- Dynamic database schema discovery
- AI-generated business summaries
- Streamlit user interface
- Structured logging
- Performance timing
- Custom application exceptions
- Unit tests with pytest

---

## Architecture

                Streamlit UI
                      │
                      ▼
              ask_database()
                      │
                pipeline.py
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
 sql_generator   database   analyzer
        │             │
        └──────┬──────┘
               ▼
             llm.py
               │
               ▼
          OpenAI API

---

## Tech Stack

- Python
- OpenAI API
- SQLite
- Pandas
- Streamlit
- Pytest

---

## Project Structure

```
customer360-ai-analyst/
│
├── data/
├── src/
├── tests/
├── README.md
├── requirements.txt
└── .env.example
```

---

## Installation

Clone the repository.

```bash
git clone <repository-url>
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate it.

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Create a `.env` file.

```text
OPENAI_API_KEY=your_api_key_here
```

---

## Running the application

Terminal version:

```bash
python src/app.py
```

Streamlit version:

```bash
streamlit run src/streamlit_app.py
```

---

## Running tests

```bash
pytest -v
```

---

## Current Status

The project is under active development.

Upcoming features include:

- Dependency Injection
- Conversation memory
- Azure SQL support
- Docker
- FastAPI REST API
- GitHub Actions CI

## Software Engineering Principles

This project is intentionally designed to practice modern backend engineering principles, including:

- Single Responsibility Principle (SRP)
- Modular architecture
- Layered application design
- Safe AI integration
- Defensive programming
- Separation of concerns
- Readable and maintainable code