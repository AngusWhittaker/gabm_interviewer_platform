# Stage 1: Base build stage
FROM python:3.11-slim

# Upgrade system packages to reduce vulnerabilities
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
        gcc \
        build-essential \
        libffi-dev \
        libssl-dev \
        libpq-dev \
        ffmpeg \
        netcat-openbsd \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

 
# Set environment variables to optimize Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 

# Create the app directory
RUN mkdir /app
 
# Set the working directory
WORKDIR /app
 
# Upgrade pip and install dependencies
RUN pip install --upgrade pip 
 
# Copy the requirements file first (better caching)
COPY requirements.txt .
 
# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh
 
ENTRYPOINT ["/app/entrypoint.sh"]
