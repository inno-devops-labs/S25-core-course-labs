# Stage 1: Build Stage
# Use a specific version of the Node.js image to ensure consistency and install dependencies
FROM node:16-alpine AS build

WORKDIR /app

# Copy package.json and package-lock.json first to take advantage of Docker cache
COPY package*.json ./ 

# Install production dependencies (we don't want to install devDependencies in the final image)
RUN npm install --production

# Copy the rest of the application files
COPY public/ ./public
COPY server.js .

# Stage 2: Production Stage with Distroless Image
# Use Distroless image with the nonroot tag (contains only the app and its dependencies, no package manager)
FROM gcr.io/distroless/nodejs16:nonroot

# Set the working directory
WORKDIR /app

# Copy the app files from the build stage to the production stage
COPY --from=build /app /app

# Expose the port the app will run on (default 3000 for Node.js apps)
EXPOSE 3000

# Start the application
CMD ["server.js"]
