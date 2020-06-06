FROM python:3.8.3-buster

RUN apt-get update && apt-get install -y --no-install-recommends netcat

COPY . /api
WORKDIR /api

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

ENTRYPOINT ["/bin/sh", "/api/entrypoint.sh"]
