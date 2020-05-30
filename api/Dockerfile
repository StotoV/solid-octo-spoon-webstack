FROM python:3.8.3-buster

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["uwsgi", "app.ini"]
