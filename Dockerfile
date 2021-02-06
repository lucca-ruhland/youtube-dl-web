FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN pip install .
EXPOSE 5000
CMD youtube-dl-web --host 127.0.0.1 --port 5000 --environment production