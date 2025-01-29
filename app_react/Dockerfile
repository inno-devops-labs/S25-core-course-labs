# Stage 1: Base
# Use a specific version of the Node.js Alpine image for reproducibility
FROM node:23-alpine3.21@sha256:15b885c5e195296ba49bab32681b478e92eb0f255078a84ad29020b87b0bdcc6 AS base

# Set environment variables for pnpm
ENV PNPM_HOME="/pnpm" \
    PATH="$PNPM_HOME:$PATH"

# Install pnpm globally using npm
# Note: Using `corepack` is recommended for managing package managers like pnpm
RUN npm install -g pnpm

# Create a non-root user and group for security
RUN addgroup -g 1001 app && \
    adduser -u 1001 -G app -D app

# Set the working directory
WORKDIR /app_react

# Set permissions for the working directory
RUN chown -R app:app /app_react

# Switch to the non-root user
USER app

# Stage 2: Production Dependencies
FROM base AS prod-deps

# Copy only the files required for installing dependencies
# This reduces the build context size and improves cache efficiency
COPY --chown=app:app package.json pnpm-lock.yaml vite.config.js index.html eslint.config.js .prettierrc ./
COPY --chown=app:app src/ ./src/
COPY --chown=app:app public/ ./public/

# Install dependencies using pnpm
# Use a cache mount to speed up subsequent builds
RUN --mount=type=cache,id=pnpm,target=/pnpm/store pnpm install --frozen-lockfile

# Stage 3: Build
FROM base AS build

# Copy the application files from the prod-deps stage
COPY --chown=app:app --from=prod-deps /app_react /app_react

# Set the working directory
WORKDIR /app_react

# Run linting, formatting, and build steps
RUN pnpm run lint && \
    pnpm run format && \
    pnpm run format:fix && \
    pnpm run build

# Stage 4: Final Image
FROM base

# Copy only the necessary files from the build stage
# This minimizes the final image size and improves security
COPY --chown=app:app --from=build /app_react/dist /app_react/dist
COPY --chown=app:app --from=build /app_react/node_modules /app_react/node_modules
COPY --chown=app:app --from=build /app_react/package.json /app_react/package.json
COPY --chown=app:app --from=build /app_react/vite.config.js /app_react/vite.config.js

# Expose the port the application will run on
EXPOSE 4173

# Set the entrypoint to run the application
ENTRYPOINT [ "pnpm", "run", "preview", "--", "--host", "0.0.0.0", "--port", "4173" ]