FROM python:3.11.1-bullseye

# RUN adduser basicuser
# USER basicuser

WORKDIR /app

RUN apt-get update
RUN apt install pipenv -y

RUN mkdir -p output

RUN pip install langchain