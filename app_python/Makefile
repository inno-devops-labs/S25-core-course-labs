APP_PORT ?= 8000
APP_HOST ?= localhost

install:
	pip install -r requirements.dev.txt

run:
	uvicorn main:app --host ${APP_HOST} --port ${APP_PORT}

format:
	ruff check --fix main.py

check:
	mypy main.py

check-dockerfile:
	docker run --rm -i hadolint/hadolint < Dockerfile


test:
	pytest