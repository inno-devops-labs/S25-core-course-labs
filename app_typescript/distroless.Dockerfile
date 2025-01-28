ARG BUILD_IMAGE=node:20.1.0
ARG RUN_IMAGE=gcr.io/distroless/nodejs20-debian11

# Build stage
FROM $BUILD_IMAGE AS build-env
COPY package.json index.html tsconfig.app.json tsconfig.json tsconfig.node.json vite.config.ts /app/
COPY public/ /app/public/
COPY src/ /app/src/
WORKDIR /app
RUN npm install && npm run build

# Prepare production dependencies
FROM $BUILD_IMAGE AS deps-env
COPY package.json ./
RUN npm install

FROM $RUN_IMAGE AS run-env
WORKDIR /usr/app
COPY --from=build-env /app/dist ./dist
COPY --from=deps-env /node_modules ./node_modules
COPY package.json ./package.json

EXPOSE 8080
CMD ["node_modules/vite/dist/node/cli.js", "preview", "--host", "0.0.0.0", "--port", "8080"]