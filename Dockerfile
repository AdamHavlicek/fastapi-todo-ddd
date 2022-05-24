FROM python:3-alpine as build

RUN apk --update add postgresql-dev python3-dev musl-dev libffi-dev make && \
    apk --update add --no-cache --virtual .build-deps gcc g++ && \
    pip install --upgrade pip --no-cache-dir

WORKDIR /opt/project

COPY ./entrypoint.sh /

COPY ./requirements.txt /tmp/requirements.txt

COPY ./Makefile /opt/project/

COPY ./pyproject.toml /opt/project/

RUN pip install --upgrade --no-cache-dir -r /tmp/requirements.txt &&  \
    poetry config virtualenvs.create false && \
    make install

RUN apk --purge del .build-deps
