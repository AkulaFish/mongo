run-local:
	uvicorn core.main:app --host localhost --port 8000 --reload