FROM python:3.9-alpine3.13
WORKDIR /code
COPY djangoTask/requirements.txt /code/
RUN pip install -r requirements.txt