# Customer360 AI Analyst

An AI-powered analytics application that allows users to query a Customer 360 database using natural language.

The application converts user questions into safe SQL queries using a Large Language Model (LLM), validates and executes the queries against a read-only SQLite database, and returns both structured results and a natural-language business summary.

---

## Design Goals

This project was built to explore modern AI-assisted backend development while following software engineering best practices.

Key design goals include:

- Clear separation of responsibilities (Single Responsibility Principle)
- Safe SQL generation and validation
- Read-only database access
- Modular and maintainable architecture
- Testable components through dependency injection
- Conversational analytics
- Clear error handling and structured logging
- Containerized deployment

---

## Features

Current features include:

- Natural-language analytics powered by OpenAI
- Automatic SQL generation
- SQL safety validation
- Read-only SQLite execution
- Dynamic database schema discovery
- AI-generated business summaries
- Conversational context for follow-up questions
- Streamlit chat interface
- FastAPI REST API
- Dependency injection for testability
- Structured logging
- Performance timing
- Custom application exceptions
- Unit and API tests with pytest
- Docker support

---

## Architecture

```text
                 User
                  │
          ┌───────┴───────┐
          ▼               ▼
     Streamlit UI      FastAPI API
          │               │
          └───────┬───────┘
                  ▼
             ask_database()
                  │
              pipeline.py
                  │
       ┌──────────┼──────────┐
       ▼          ▼          ▼
 sql_generator  database  analyzer
       │                     │
       └──────────┬──────────┘
                  ▼
                llm.py
                  │
                  ▼
             OpenAI API
```

The pipeline coordinates SQL generation, validation, database execution, and result analysis. Dependencies can be replaced with test implementations, allowing the pipeline and API to be tested without making real OpenAI API calls.

---

## Tech Stack

- Python 3.12+
- OpenAI API
- SQLite
- Pandas
- Streamlit
- FastAPI
- Uvicorn
- Pytest
- Docker

---

## Project Structure

```text
customer360-ai-analyst/
│
├── data/
│
├── src/
│   ├── analyzer.py
│   ├── api.py
│   ├── app.py
│   ├── conversation.py
│   ├── database.py
│   ├── exceptions.py
│   ├── llm.py
│   ├── logging_config.py
│   ├── pipeline.py
│   ├── sql_generator.py
│   ├── sql_validator.py
│   └── streamlit_app.py
│
├── tests/
│
├── .dockerignore
├── .env.example
├── .gitignore
├── Dockerfile
├── pytest.ini
├── README.md
└── requirements.txt
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd customer360-ai-analyst
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a local `.env` file based on `.env.example` and provide your OpenAI API key:

```text
OPENAI_API_KEY=your_api_key_here
```

The `.env` file should never be committed to version control.

---

## Running the Application

### Terminal

```bash
python src/app.py
```

### Streamlit

```bash
streamlit run src/streamlit_app.py
```

### FastAPI

```bash
uvicorn api:app --app-dir src --reload
```

The API is then available at:

- `http://localhost:8000`
- Interactive API documentation: `http://localhost:8000/docs`
- Health check: `http://localhost:8000/health`

---

## Running Tests

Run the test suite with:

```bash
pytest -v
```

The application uses dependency injection and test doubles so that core pipeline and API behavior can be tested without making real OpenAI API calls.

---

## Running with Docker

The FastAPI application can also be built and run inside a Docker container.

Docker Desktop is required for containerized execution.

### Build the Docker Image

Make sure Docker Desktop is running.

From the project root:

```bash
docker build -t customer360-ai-analyst .
```

### Run the Docker Container

Make sure your local `.env` file contains the required environment variables.

Then run:

```bash
docker run --env-file .env -p 8000:8000 customer360-ai-analyst
```

The containerized FastAPI application is then available at:

- `http://localhost:8000`
- Interactive API documentation: `http://localhost:8000/docs`
- Health check: `http://localhost:8000/health`

The `.env` file is excluded from the Docker image and should never be committed to version control.

To stop a container running in the foreground, press `Ctrl+C`.

---

## Current Status

The project is under active development.

Implemented engineering features include:

- Dependency injection
- Conversational context
- FastAPI REST API
- Docker containerization
- Automated tests
- Structured logging and error handling

Potential next steps include:

- GitHub Actions CI
- Azure SQL integration
- Additional API and integration tests
- Deployment to a cloud environment

---

## Software Engineering Principles

This project is intentionally designed to practice modern backend engineering principles, including:

- Single Responsibility Principle (SRP)
- Dependency injection
- Modular architecture
- Layered application design
- Safe AI integration
- Defensive programming
- Separation of concerns
- Automated testing
- Readable and maintainable code