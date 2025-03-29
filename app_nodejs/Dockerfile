# Stage 1: Build stage
FROM node:18-alpine AS builder

WORKDIR /app

# Copy package.json and install dependencies first (for caching)
COPY package.json package-lock.json* ./

RUN npm ci --only=production

# Copy source code
COPY . .

# Stage 2: Final runtime stage
FROM node:18-alpine

WORKDIR /app

# Copy only built files from builder stage
COPY --from=builder /app .

# Create visits directory and set permissions
RUN mkdir -p /app && touch /app/visits && chmod 777 /app/visits

# Run as non-root user
USER node

EXPOSE 8000

CMD ["node", "server.js"]
