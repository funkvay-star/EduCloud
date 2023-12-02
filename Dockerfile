# Use Python 3.12 slim image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Install system dependencies required for building Python packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    libc6-dev && \
    rm -rf /var/lib/apt/lists/*

# Copy the entire src directory to the container and token
COPY src/ .
COPY token.txt ./

# Create an entrypoint script
RUN echo '#!/bin/bash\nexport TELEGRAM_TOKEN=$(cat token.txt)\nexec "$@"' > /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set the entrypoint
ENTRYPOINT ["/entrypoint.sh"]

# Install necessary libraries
RUN pip install aiogram \
    loguru \
    pytest \
    python-dotenv

# Command to run the main Python script (assuming main.py is your main script)
CMD ["python", "./main.py"]

