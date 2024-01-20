FROM python:3-slim-buster

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app/ .

CMD ["gunicorn", "main:app", "-w 5", "-k uvicorn.workers.UvicornWorker", "-b 0.0.0.0:8000"]