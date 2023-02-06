FROM python:3.10-alpine

COPY ./requirements.txt /tmp/

RUN python3 -m pip install --upgrade pip setuptools wheel && \
    python3 -m pip install -r /tmp/requirements.txt

WORKDIR /srv