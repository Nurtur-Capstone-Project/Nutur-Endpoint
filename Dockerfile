FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update

RUN pip install --no-cache-dir -r requirements.txt


COPY . .

ENV PYTHONUNBUFFERED True

ENV HOST 0.0.0.0

EXPOSE 8001

CMD [ "python", "main.py" ]