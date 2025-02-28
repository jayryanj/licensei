FROM python:3.12-slim
LABEL authors="Jay"

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app /app
ENTRYPOINT ["flask", "run", "--debug", "--host=0.0.0.0", "--port=80"]