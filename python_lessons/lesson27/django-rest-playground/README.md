# Django REST Framework Playground

This repository contains examples and exercises created while learning Django REST Framework during the Python Developer Pro course.

The project demonstrates selected Django REST Framework concepts, including:

- serializers,
- function-based API views,
- JWT authentication with SimpleJWT,
- middleware,
- request and response handling,
- testing,
- cookies and `JsonResponse`,
- example HTTP requests.

The repository is intended for learning purposes and contains independent examples presented during the course rather than a single production-ready application.

## Technologies

- Python 3.13+
- Django
- Django REST Framework
- SimpleJWT
- uv

## Project structure

```text
.
├── core/                 # Django project configuration
├── drf_playground/       # DRF examples used throughout the lesson
├── tests/                # Additional test examples
├── manage.py
├── requests.http         # Example HTTP requests
├── pyproject.toml
├── uv.lock
└── README.md
```

## Getting started

Install the dependencies:

```bash
uv sync
```

Run the development server:

```bash
uv run python manage.py runserver
```

Apply migrations if necessary:

```bash
uv run python manage.py migrate
```

## Notes

This repository demonstrates concepts presented during the course. Some files intentionally show alternative approaches (for example, different ways of organizing tests or implementing API endpoints) and are included for educational purposes.