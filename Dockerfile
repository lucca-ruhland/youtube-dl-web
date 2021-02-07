FROM python:alpine3.7

COPY . /app
WORKDIR /app

RUN pip install virtualenv

RUN python -m venv /opt/venv

RUN /opt/venv/bin/pip install .
RUN /opt/venv/bin/pip install gunicorn

