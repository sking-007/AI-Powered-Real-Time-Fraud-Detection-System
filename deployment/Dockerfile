# Use Python as the base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy all project files
COPY . /app

# Install dependencies
RUN pip install fastapi uvicorn xgboost numpy pandas

# Expose API port
EXPOSE 8000

# Run FastAPI app
CMD ["uvicorn", "deploy_model:app", "--host", "0.0.0.0", "--port", "8000"]
