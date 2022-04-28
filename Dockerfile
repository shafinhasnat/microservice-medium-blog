FROM python:3.9.5-slim-buster
WORKDIR /usr/src/app

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

COPY ./entrypoint.sh .
RUN chmod +x /usr/src/app/entrypoint.sh
