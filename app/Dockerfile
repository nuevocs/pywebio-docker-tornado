FROM python:3.6

ENV PYTHONUNBUFFERED 1
ENV DOCKER true

RUN apt-get update && apt-get install -y vim python3-dev
RUN apt-get clean
RUN apt-get autoremove

ADD ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN /sbin/init