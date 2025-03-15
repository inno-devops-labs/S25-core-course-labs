# Builder base image
FROM node:20-alpine AS builder

# Set working directory
WORKDIR /app

COPY package*.json ./

# Install dependencies
RUN npm install --production

# Copy application code
COPY . .

# Create folder and allow rw permission
RUN mkdir -p /app/data && chmod -R 777 /app/data

# Base distroless-nonroot image
FROM gcr.io/distroless/nodejs20-debian12:nonroot AS result

# Set working directory
WORKDIR /app

# Copy application code from builder stage, включая data
COPY --from=builder /app /app

EXPOSE 3000

CMD ["server.js"]
