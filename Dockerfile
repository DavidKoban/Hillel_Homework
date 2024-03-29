FROM python:3.8-alpine
ENV PYTHONUNBUFFERED=1
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
WORKDIR /django
EXPOSE 80:8080
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . /django/
CMD python bot.py