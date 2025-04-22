FROM python:3.11-slim

# Install system-level dependencies required for uWSGI
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    && apt-get clean

# Set environment variables
ENV FLASK_APP="app:create_app"
ENV FLASK_ENV="production"

WORKDIR /app
ADD . /app/

COPY config/app.ini /config/app.ini

# Install Python dependencies, including uWSGI
RUN pip install --upgrade pip
RUN pip install uwsgi
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y libpcre3 libpcre3-dev
RUN pip install uwsgi

ENTRYPOINT ["./boot.sh"]