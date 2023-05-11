FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /events-app

WORKDIR /events-app

ADD . /events-app/

RUN apt-get update && apt-get upgrade -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000