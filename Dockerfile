FROM python:alpine3.7

COPY . /app
WORKDIR /app

RUN pip install virtualenv

RUN python -m venv /opt/venv

# copy youtube_dl_web static/templates folder
COPY ./src/youtube_dl_web/templates/ /opt/venv/lib/python3.7/site-packages/youtube_dl_web/templates/
COPY ./src/youtube_dl_web/static/ /opt/venv/lib/python3.7/site-packages/youtube_dl_web/static/

RUN /opt/venv/bin/pip install .
RUN /opt/venv/bin/pip install gunicorn
RUN pip install python-dotenv