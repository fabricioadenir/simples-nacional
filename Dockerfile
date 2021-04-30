FROM python:3.7-alpine3.10

RUN apk add --update alpine-sdk libxml2-dev libxslt-dev linux-headers python3-dev libffi-dev musl-dev
RUN apk add --update openssl-dev python-dev

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY Pipfile /usr/src/app/

RUN pipenv install --system --deploy --ignore-pipfile

COPY . /usr/src/app

EXPOSE 8000

CMD uvicorn asgi:app --host 0.0.0.0 --port 8000
