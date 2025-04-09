mkdir -p data
chmod 777 data
uvicorn main:app --host localhost --port 8000 --reload