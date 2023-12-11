FROM python:3.9-alpine3.13
WORKDIR /tofi
COPY requirements.txt /tofi/
RUN pip install -r requirements.txt