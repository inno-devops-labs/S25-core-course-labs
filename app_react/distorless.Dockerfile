# Stage 1: Base
FROM node:22-alpine3.21 AS base
WORKDIR /app_react

# Stage 2: Production Dependencies
FROM base AS prod-deps
COPY package.json vite.config.js index.html eslint.config.js .prettierrc ./
COPY src/ ./src/
COPY public/ ./public/

# Install PRODUCTION dependencies
RUN --mount=type=cache,id=npm,target=/root/.npm \
    npm i

# Stage 3: Build
FROM base AS build
COPY --from=prod-deps /app_react ./

# Install ALL dependencies (including devDependencies)
RUN --mount=type=cache,id=npm,target=/root/.npm \
    npm i

# Build steps
RUN npm run lint && \
    npm run format && \
    npm run build

# Stage 4: Final Image
FROM gcr.io/distroless/nodejs22:nonroot
WORKDIR /app_react

# Copy production dependencies and build artifacts
COPY --from=prod-deps /app_react/node_modules /app_react/node_modules
COPY --from=build /app_react/dist /app_react/dist

# Use Node.js directly to run your application
# (distroless doesn't include npm)
CMD [ "npm", "run" , "preview" ]  

EXPOSE 8000