FROM node:alpine3.20

# Install Python 3.10
RUN apk add --no-cache python3=3.10.12-r0 python3-dev=3.10.12-r0 py3-pip


RUN npx -y playwright@1.50.1 install --with-deps


# Set working directory
WORKDIR /app

# Copy application files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt