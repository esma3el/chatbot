FROM python:3.10.14-alpine3.20

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY server.py .
COPY green_api.py .

ENTRYPOINT [ "python3","server.py" ]