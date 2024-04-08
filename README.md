## Simple FastAPI app for autotests

### Description

Simple planning app for autotesting. User can perform the following operations:

- create event /new
- delete event /{id}
- get all events /
- get specific event /{id}
- sign up user /signup
- sign in user /signin

The application implements JWT authorization.

- FastAPI
- Pydantic
- MongoDB

### Requirements

- Python => 3.10

### Quick start

```bash
python -m venv venv
pip install -r requirements.txt
pytest -vv
```

Swagger documentation is available along the way http://localhost:8082

### Start from Docker

```bash
docker docker build -t event-planner-api .
docker-compose up -d
```