FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy shared library
COPY shared /app/shared

# Copy service code
COPY services/auth_service /app/services/auth_service

# Run Uvicorn directly from within the module path
CMD ["uvicorn", "services.auth_service.main:app", "--host", "0.0.0.0", "--port", "8000"]
