# Dockerfile for custom Python environment (if needed outside Databricks)
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/

CMD ["python", "src/ingestion/data_generator.py"]