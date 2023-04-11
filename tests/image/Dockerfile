FROM python:3.10-alpine AS unit_tests
WORKDIR /srv
COPY ./requirements.txt /tmp/
RUN python3 -m pip install --upgrade pip setuptools wheel && \
   python3 -m pip install -r /tmp/requirements.txt
RUN apk update && \
   apk add chromium-chromedriver