FROM python:3.8

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y gettext libgettextpo-dev \
  locales \
  locales-all \
  python3.8-dev


COPY . .
