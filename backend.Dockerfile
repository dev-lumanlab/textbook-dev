FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./iacapap_textbook_backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./iacapap_textbook_backend .

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]
