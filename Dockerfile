FROM python:3.12-slim

WORKDIR /usr/src/app

# Install system dependencies required for building Python packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    libc6-dev && \
    rm -rf /var/lib/apt/lists/*


# Install necessary libraries
COPY requirements.txt .

RUN pip install -r requirements.txt

# Copy the entire src directory to the container and token
COPY src/ .

COPY .env .env

# Command to run the main Python script (assuming main.py is your main script)
CMD ["python", "./main.py"]