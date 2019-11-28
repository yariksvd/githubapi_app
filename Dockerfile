FROM python:3.7-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/