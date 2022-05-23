FROM python:3-alpine as build

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

WORKDIR /opt/project

COPY ./entrypoint.sh /

COPY ./requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /tmp/requirements.txt

