# 1. Python base image
FROM python:3.11-slim

# 2. Environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Working directory
WORKDIR /app

# 4. Install dependencies
# Pehle requirements.txt copy karein
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 5. Baaki code copy karein
COPY . /app/

# 6. Command to run
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]