# Use Node.js minimal image
FROM node:18-alpine AS builder

# Set working directory
WORKDIR /app

# Copy only package.json to install dependencies first (for layer efficiency)
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install --only=production

# Copy source code
COPY . .

# Use a minimal runtime image
FROM node:18-alpine AS runtime

# Set non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

WORKDIR /app

# Copy built files from the builder stage
COPY --from=builder /app .

# Expose the port
EXPOSE 3000

# Run the application
CMD ["node", "server.js"]