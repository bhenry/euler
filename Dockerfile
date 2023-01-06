# syntax=docker/dockerfile:1

FROM python:3.11-slim-bullseye

WORKDIR /opt/app

COPY . .

CMD ["python"]
