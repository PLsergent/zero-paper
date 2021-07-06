# syntax=docker/dockerfile:1
FROM python:3.7
ENV PYTHONUNBUFFERED=1
WORKDIR /zero_paper
COPY . /zero_paper
RUN pip install pipenv
RUN pipenv install


CMD [ "pipenv", "run", "gunicorn", "-b", "0.0.0.0:8000", "config.wsgi:application" ]
