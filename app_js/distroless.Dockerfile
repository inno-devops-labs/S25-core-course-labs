# Build Stage
FROM node:22-alpine AS builder
### Set the working directory
WORKDIR /app

### Install dependencies
COPY package.json . 
RUN npm install --production --frozen-lockfile

### Copy the rest of the application files
COPY . .

# Preparing and Running App
FROM gcr.io/distroless/nodejs22-debian12:nonroot
### Set the working directory
WORKDIR /app

### Copy the installed dependencies from the builder stage
COPY --from=builder /app/node_modules /app/node_modules

### Copy the application code
COPY --from=builder /app /app

### Non-root user
USER nonroot

### Expose the port the app runs on
EXPOSE 3000

### Command to run the application
CMD ["server.js"]
