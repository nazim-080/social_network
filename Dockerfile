FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /ylab_cv_constructor

# install dependencies
COPY ./requirements.txt .
RUN python -m pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir

# copy project
COPY . .