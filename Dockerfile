# Dockerfile
FROM python:3.11-slim

WORKDIR /code

# Install system packages required to build some Python packages
RUN apt-get update && \
    apt-get install -y gcc build-essential libpq-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]