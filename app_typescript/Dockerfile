FROM node:22-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN --mount=type=cache,target=/root/.npm npm ci

# Copy source files
COPY tsconfig.json vite.config.ts ./
COPY src/ src/

# Build the application
RUN npm run build

# Production stage
FROM caddy:2.9-alpine

# Copy the built assets from builder stage
COPY --from=builder /app/dist /usr/share/caddy

# Use non-root user
RUN adduser --system --no-create-home nonroot
USER nonroot

# Expose port 80
EXPOSE 80

# Caddy will serve static files by default