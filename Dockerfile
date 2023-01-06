# syntax=docker/dockerfile:1

FROM python:latest


EXPOSE 8000

WORKDIR /fastapi

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

CMD ["python3","-m","uvicorn","main:app","--host=0.0.0.0"]

