FROM python:3.9

WORKDIR /app

SHELL ["/bin/bash", "-c"]

RUN apt-get update &

RUN pip install --upgrade pip

COPY requirements.txt /app

RUN pip install -r requirements.txt