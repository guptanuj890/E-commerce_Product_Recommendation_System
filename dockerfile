FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements first for caching purposes
COPY requirements.txt .

# Install Python dependencies explicitly
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the rest of the code
COPY . .

# Expose port
EXPOSE 5000

# Start the app
CMD ["python", "app.py"]
