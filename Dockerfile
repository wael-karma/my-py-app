FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y unixodbc-dev freetds-dev && \
    pip install -r requirements.txt

COPY . .

EXPOSE 6000

CMD ["python", "app.py"]