# Changed from 3.9 to 3.10
FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files
COPY . .

EXPOSE 5000

# Added timeout to handle your 10 million rows
CMD ["gunicorn", "--timeout", "600", "--bind", "0.0.0.0:5000", "app:app"]