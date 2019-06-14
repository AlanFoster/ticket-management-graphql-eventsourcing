FROM python:3.7.3-alpine

ENV DOCKERIZE_VERSION v0.6.1

RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz

RUN apk add gcc build-base postgresql-dev gcc python3-dev musl-dev
RUN pip install --no-cache-dir pipenv

WORKDIR /srv/app

COPY Pipfile Pipfile.lock ./
RUN pipenv install --deploy --dev --ignore-pipfile --system

COPY . .
