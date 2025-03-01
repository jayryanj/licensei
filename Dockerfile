FROM python:3.12-slim
LABEL authors="Jay"

WORKDIR /backend

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY backend /backend
ENTRYPOINT ["flask", "run", "--debug", "--host=0.0.0.0", "--port=80"]