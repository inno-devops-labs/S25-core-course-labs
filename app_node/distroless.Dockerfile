# Stage 1: Build dependencies
FROM node:18-alpine AS builder

# Set working directory
WORKDIR /app_node

# Copy package files
COPY app_node/package.json .
COPY app_node/package-lock.json .

# Install dependencies
RUN npm install --omit=dev

# Copy application files
COPY app_node/ .

# Stage 2: Use Distroless for Production
FROM gcr.io/distroless/nodejs18:nonroot

# Set working directory
WORKDIR /app_node

# Copy only necessary built files from builder stage
COPY --from=builder /app_node/node_modules /app_node/node_modules
COPY --from=builder /app_node/server.js /app_node/server.js
COPY --from=builder /app_node/package.json /app_node/package.json
COPY --from=builder /app_node/package-lock.json /app_node/package-lock.json

# Expose port 7000
EXPOSE 7000

# Set environment variable for port
ENV PORT=7000

# Run the application using Node.js (correct binary path)
CMD ["node", "/app_node/server.js"]
