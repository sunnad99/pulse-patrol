# FastAPI Server

This is the backend server for the customer management system built with FastAPI and SQLAlchemy.

## Setup

### Prerequisites

- Python 3.11+
- pip (Python package manager)
- PostgreSQL

### Installation

1. Create a virtual environment:

```bash
python -m venv venv
```

2. Activate the virtual environment:

```bash
source venv/bin/activate
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Run the migrations:

```bash
alembic init alembic
alembic migrate
```

5. Run the server:

```bash
uvicorn app:app --reload
```
