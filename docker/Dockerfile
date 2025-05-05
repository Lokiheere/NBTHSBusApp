FROM python:3.11-slim

# Install only essential system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc build-essential libssl-dev libffi-dev python3-dev \
    libatlas-base-dev gfortran nginx libpcre3 libpcre3-dev \
    && apt-get clean

# Set Flask environment variables
ENV FLASK_APP="app.py"
ENV FLASK_ENV="development"

USER root

# Set working directory & copy application code
WORKDIR /app
COPY .. /app

# Install Python dependencies efficiently
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Correct Gunicorn startup command
CMD ["gunicorn", "--workers=4", "--threads=2", "--bind=0.0.0.0:8080", "app:create_app()"]