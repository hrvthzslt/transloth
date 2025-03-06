FROM python:3.11-alpine

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

CMD ["fastapi", "run", "app/main.py", "--host", "0.0.0.0.", "--port", "8000"]
