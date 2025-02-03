# Use a minimal Node.js base image
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy only package.json first for better caching
COPY package.json .

# Install dependencies (no additional dependencies in this case)
RUN npm install --omit=dev

# Copy application code
COPY server.js .

# Expose port
EXPOSE 3000

# Set non-root user for security
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

# Run the application
CMD ["npm", "start"]