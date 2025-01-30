# Stage 1: Build dependencies
FROM node:18-alpine AS builder

# Set working directory
WORKDIR /app_node

# Copy package.json explicitly from app_node/
COPY app_node/package.json .  

# Install dependencies
RUN npm install --omit=dev

# Copy the rest of the application files
COPY app_node/ .

# Expose port 3000
EXPOSE 3000

# Run the application
CMD ["node", "server.js"]
