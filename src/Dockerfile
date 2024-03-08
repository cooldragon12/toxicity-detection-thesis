FROM python:3.11.5-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

RUN mkdir /src
WORKDIR /src

COPY requirements.txt /src/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /src/