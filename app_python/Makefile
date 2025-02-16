check:
	black src/ --check
	isort src/ --check-only
	pylint src/ --disable=C
	mypy src/

format:
	black src/
	isort src/

run:
	uvicorn src.main:app --host=0.0.0.0 --port 8888
