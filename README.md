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

### Requirements

- Python => 3.10

### Prerequisite

To run successfully, there must be a config file in project root.

```bash
DATABASE_URL=mongodb://database:27017/planner
SECRET_KEY=<HASH_FOR_DB>
```

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