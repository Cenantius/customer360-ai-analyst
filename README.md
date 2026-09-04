# Customer360 AI Analyst

[![CI](https://github.com/cenantius/customer360-ai-analyst/actions/workflows/ci.yml/badge.svg)](https://github.com/cenantius/customer360-ai-analyst/actions/workflows/ci.yml)

A Python backend and data analytics project that allows users to query a Customer 360 database using natural language.

The application uses an LLM to translate business questions into SQL, validates the generated query, executes it against a read-only SQLite database, and produces both structured results and a natural-language summary.

The project was built as a hands-on software engineering project combining Python, SQL, REST APIs, automated testing, Docker, and continuous integration. AI is used as one component of the application rather than being the sole focus of the project.

---

## Key Features

- Natural-language database queries using the OpenAI API
- Automatic SQL generation
- SQL validation before execution
- Read-only SQLite database access
- Dynamic database schema discovery
- Natural-language summaries of query results
- Conversational context for follow-up questions
- FastAPI REST API
- Streamlit chat interface
- Dependency injection for testability
- Structured logging and custom exception handling
- Performance timing
- Automated tests with pytest
- Docker containerization
- GitHub Actions continuous integration

---

## How It Works

A user can ask a business question such as:

> Which city generated the second-most revenue?

The application processes the question through a multi-step pipeline:

```text
Natural-language question
          │
          ▼
     SQL generation
          │
          ▼
     SQL validation
          │
          ▼
 Read-only database
          │
          ▼
    Query results
          │
          ▼
Natural-language summary
```

The generated SQL and structured query results can also be inspected by the user.

Recent completed conversation turns can be included as context when generating SQL, allowing the application to understand follow-up questions that depend on the previous conversation.

---

## Architecture

```text
                  User
                   │
          ┌────────┴────────┐
          ▼                 ▼
    Streamlit UI        FastAPI API
          │                 │
          └────────┬────────┘
                   ▼
              ask_database()
                   │
               pipeline.py
                   │
       ┌───────────┼───────────┐
       ▼           ▼           ▼
 SQL Generator  Validator   Database
       │                       │
       │                       ▼
       │                     SQLite
       │
       └────────────┐
                    ▼
                 Analyzer
                    │
                    ▼
                OpenAI API
```

The pipeline coordinates SQL generation, validation, database execution, and result analysis.

Dependencies can be passed into the pipeline instead of being permanently coupled to their production implementations. This makes it possible to replace external dependencies with test implementations and test the application without making real OpenAI API calls.

---

## SQL Safety

LLM-generated SQL is not executed without validation.

The application uses multiple safeguards:

- Generated SQL is validated before execution
- Unsafe SQL operations are rejected
- Multiple SQL statements are rejected
- Database access is read-only
- Application failures are handled through custom exceptions

This provides separate application-level and database-level safeguards before and during query execution.

---

## Tech Stack

- Python 3.12
- SQL
- SQLite
- Pandas
- OpenAI API
- FastAPI
- Uvicorn
- Streamlit
- Pytest
- Docker
- Git & GitHub
- GitHub Actions

---

## Project Structure

```text
customer360-ai-analyst/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── data/
├── src/
│   ├── analyzer.py
│   ├── api.py
│   ├── app.py
│   ├── config.py
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
git clone https://github.com/Cenantius/customer360-ai-analyst.git
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

Create a local `.env` file based on `.env.example` and provide the required environment variables:

```text
OPENAI_API_KEY=your_api_key_here
```

The `.env` file is excluded from version control.

---

## Running the Application

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
- API documentation: `http://localhost:8000/docs`
- Health check: `http://localhost:8000/health`

### Terminal

```bash
python src/app.py
```

---

## Testing

Run the test suite with:

```bash
pytest -v
```

The tests cover core application behavior including SQL validation, pipeline behavior, conversational context, and API endpoints.

Dependency injection and test doubles allow the application to be tested without making real OpenAI API calls.

---

## Continuous Integration

GitHub Actions automatically runs the test suite when changes are pushed to the `main` branch.

The CI workflow:

1. Creates a clean Ubuntu environment
2. Checks out the repository
3. Sets up Python 3.12
4. Installs project dependencies
5. Runs the pytest test suite

This helps verify that the application works outside the local development environment and catches problems before further development.

---

## Docker

The FastAPI application can also be run inside a Docker container.

Build the image:

```bash
docker build -t customer360-ai-analyst .
```

Run the container:

```bash
docker run --env-file .env -p 8000:8000 customer360-ai-analyst
```

The containerized API is then available at:

- `http://localhost:8000`
- `http://localhost:8000/docs`
- `http://localhost:8000/health`

---

## Project Status

The core application is complete and functional.

The project demonstrates a complete development workflow from application design and database access to automated testing, REST API development, containerization, and continuous integration.

Possible future extensions include cloud deployment, additional database backends, and further integration testing.

---

## What I Learned

This project was built to develop practical software engineering skills beyond basic application functionality.

Key areas of learning included:

- Designing a modular Python application
- Separating responsibilities between application components
- Working with SQL and relational data from Python
- Designing and consuming REST APIs
- Safely integrating an LLM into an application
- Using dependency injection to improve testability
- Writing automated tests and test doubles
- Debugging differences between local and CI environments
- Containerizing a backend application with Docker
- Automating testing with GitHub Actions
- Using Git and GitHub throughout an iterative development workflow