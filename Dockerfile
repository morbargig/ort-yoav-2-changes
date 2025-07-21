# Use Python 3.11 slim image
FROM python:3.11-slim

# Install system dependencies for tkinter and GUI support
RUN apt-get update && apt-get install -y \
    python3-tk \
    x11-apps \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy the calculator script
COPY scripts/calculator.py .

# Set environment variables for GUI
ENV DISPLAY=:0
ENV PYTHONUNBUFFERED=1

# Create a non-root user
RUN useradd -m -u 1000 calculator
USER calculator

# Command to run the calculator
CMD ["python", "calculator.py"]
