# Use the Python 3.13 slim image (Debian-based)
FROM python:3.13-slim

# Set the working directory inside the container
WORKDIR /app

# Update and install necessary system packages, replacing 'nss' with 'libnss3'
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    bash \
    curl \
    wget \
    unzip \
    xvfb \
    libx11-6 \
    xauth \
    libxcomposite1 \
    libxdamage1 \
    libxi6 \
    libxtst6 \
    libnss3 \
    fonts-dejavu \
    gcc \
    libffi-dev \
    musl-dev \
    && apt-get clean

# Copy the requirements.txt into the container
COPY requirements.txt /app/

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright after the dependencies
RUN pip install playwright && python -m playwright install --with-deps

# Copy the application code into the container
COPY . /app

# Set the command to run your Playwright tests
CMD ["pytest", "tests"]
