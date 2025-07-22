FROM python:3.10-slim

WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app directory (adjust if needed)
COPY ./app .

# Ensure the /data directory exists (if needed)
RUN mkdir -p /data

# Command to run the pipeline
CMD ["python", "pipeline.py"]