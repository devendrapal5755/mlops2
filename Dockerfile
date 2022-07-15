# syntax=docker/dockerfile:1
FROM python:3.7.13
# COPY . /usr/app/
EXPOSE 5000
COPY requirements.txt requirements.txt
COPY app.py app.py
RUN pip install -r requirements.txt
CMD python app.py