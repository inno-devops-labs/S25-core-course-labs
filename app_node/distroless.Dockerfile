# Stage 1: Build the application
FROM node:14 AS builder

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the application code
COPY . .

# Stage 2: Create a Distroless image
FROM gcr.io/distroless/nodejs14

# Set the working directory
WORKDIR /app

# Copy the built application from the builder stage
COPY --from=builder /app .

# Expose the port
EXPOSE 3001

# Command to run the application
CMD ["app.js"]
