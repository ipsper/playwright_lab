FROM node:20-bookworm

# Install Python 3.10

RUN apt-get update && apt-get install -y python3.10 python3-pip
RUN npx -y playwright@1.50.1 install --with-deps

# Set working directory
WORKDIR /app

# Copy application files
COPY app /app

# Install Python dependencies

RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the rest of the application
COPY app /app

# Set default environment variables for Uvicorn
ENV UVICORN_HOST=0.0.0.0
ENV UVICORN_PORT=8000

# Run FastAPI
CMD ["sh", "-c", "uvicorn main:app --host $UVICORN_HOST --port $UVICORN_PORT"]