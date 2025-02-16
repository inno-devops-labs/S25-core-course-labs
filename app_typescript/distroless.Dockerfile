# Build stage
FROM node:20.1.0 AS build-env
COPY package.json index.html tsconfig.app.json tsconfig.json tsconfig.node.json vite.config.ts /app/
COPY public/ /app/public/
COPY src/ /app/src/
WORKDIR /app
RUN npm install && npm run build

# Prepare production dependencies
FROM node:20.1.0 AS deps-env
WORKDIR /app
COPY package.json ./
RUN npm install

# Create final production stage
FROM gcr.io/distroless/nodejs20-debian11:nonroot AS run-env
WORKDIR /usr/app
COPY --from=build-env /app/dist ./dist
COPY --from=deps-env /app/node_modules ./node_modules

ENV NODE_ENV="production"
EXPOSE 8080
CMD ["node_modules/vite/dist/node/cli.js", "preview", "--host", "0.0.0.0", "--port", "8080"]