check:
	black src/ tests/ --check
	isort src/ tests/ --check-only
	pylint src/ tests/ --disable=C
	mypy src/ tests/

format:
	black src/ tests/
	isort src/ tests/

run:
	uvicorn src.main:app --host=0.0.0.0 --port 8888

test:
	pytest -s --cov=src/ --cov-report=json tests/
