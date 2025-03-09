# Stage 1: Build Stage
# Use a specific Node.js version and a slim base image (Alpine) to minimize size.
FROM node:16-alpine AS build

# Set the working directory inside the container
WORKDIR /app

# Copy only the package.json and package-lock.json to utilize Docker cache for dependencies
COPY package*.json ./

# Install dependencies
RUN npm install 

# Copy the rest of the application files
COPY public/ ./public
COPY data/ data/
COPY server.js .

# Stage 2: Production Stage
# Use a minimal Node.js image with Alpine to reduce image size
FROM node:16-alpine

# Set the working directory inside the container
WORKDIR /app

# Create a non-root user for security
# RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Change ownership of the application folder to the new user
# RUN chown -R appuser:appgroup /app

# Switch to the non-root user
# USER appuser

# Copy the installed dependencies and application code from the build stage
COPY --from=build /app /app

# Expose the application port (adjust if necessary)
EXPOSE 3000

# Command to run the application (in pacage.json the "start" command starts the app using "node server.js")
CMD ["npm", "start"]
