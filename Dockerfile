# Use official Python image
FROM python:3.11-slim

ENV PYTHONPATH=/app
# Set working directory
WORKDIR /app

# Copy all files
COPY . .

# Upgrade pip and install dependencies for all packages
RUN python -m pip install --upgrade pip
RUN python -m pip install -r package1/requirements.txt \
                       -r package2/requirements.txt \
                       -r package3/requirements.txt \
                       pytest

# Default command to run all tests
CMD ["pytest", "package1/tests", "package2/tests", "package3/tests"]

