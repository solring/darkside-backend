# syntax=docker/dockerfile:1

FROM python:3
ARG certdir=./ssh
RUN echo "certdir: $certdir"

RUN mkdir /backend
COPY ./app /backend/app
COPY ./requirements.txt  /backend/.

COPY $certdir /backend/ssh

WORKDIR /backend
RUN pip install --no-cache-dir -r requirements.txt

ENV GUNICORN_CMD_ARGS="--certfile /backend/ssh/server.crt --keyfile /backend/ssh/server.key"
CMD ["gunicorn", "-b 0.0.0.0:5000", "app:app"]

EXPOSE 5000
