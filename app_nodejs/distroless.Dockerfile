# app_nodejs/distroless.Dockerfile

# Stage 1: Builder
FROM node:14-alpine as builder
WORKDIR /build
COPY package.json .
RUN npm install --production
COPY server.js .

# Stage 2: Distroless Runtime
# Use Distroless Node image from:
# https://github.com/GoogleContainerTools/distroless/tree/main/nodejs
FROM gcr.io/distroless/nodejs14:nonroot

WORKDIR /usr/src/app

# Copy the built artifacts from the builder stage
COPY --from=builder /build/node_modules ./node_modules
COPY --from=builder /build/server.js .

EXPOSE 3000
# Distroless image is already set to nonroot user
CMD ["server.js"]
