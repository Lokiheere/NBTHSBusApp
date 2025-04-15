FROM python:3.11-slim

ENV FLASK_APP=app.py

WORKDIR /home/nbthsbusapp

COPY requirements requirements

RUN python -m venv venv

RUN venv/bin/pip install --upgrade pip

RUN venv/bin/pip install -r requirements/docker.txt

COPY app app

COPY app.py boot.sh ./

EXPOSE 5000

ENTRYPOINT ["./boot.sh"]