# Stage 1: Build
FROM node:18-alpine AS builder

# Set working directory
WORKDIR /app_node

# Copy package.json and install dependencies
COPY package.json .
RUN npm install --omit=dev

# Copy application source code
COPY . .

# Stage 2: Production with Distroless
FROM gcr.io/distroless/nodejs18:nonroot

# Set working directory
WORKDIR /app_node

# Copy built application from builder stage
COPY --from=builder /app_node /app_node

# Expose port 7000
EXPOSE 7000

# Run the application
CMD ["node", "server.js"]
