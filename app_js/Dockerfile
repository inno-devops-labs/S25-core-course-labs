# Build Stage
FROM node:22-alpine as builder
### Set the working directory
WORKDIR /app

### Install dependencies
COPY package.json .
RUN npm install --production --frozen-lockfile

### Copy the rest of the application files
COPY . .

# Preparing and Running App
FROM node:22-alpine
### Set the working directory
WORKDIR /app

### Copy the installed dependencies from the builder stage
COPY --from=builder /app/node_modules /app/node_modules

### Copy the application code
COPY --from=builder /app /app

### Add a non-root user for security purposes
RUN adduser -D nonroot
USER nonroot

### Expose the port the app runs on
EXPOSE 3000

### Command to run the application
CMD ["npm", "start"]
