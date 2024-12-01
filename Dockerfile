FROM python:3.12.5-slim-bookworm


WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc \
  && apt-get clean

# I also don't know what this does, but it's in the tutorial
CMD ["python", "main.py"]