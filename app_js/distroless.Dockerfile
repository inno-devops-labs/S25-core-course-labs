# Stage 1: Build stage
FROM node:16-slim AS build

WORKDIR /app

# copying only package.json and package-lock.json
COPY package*.json ./

# install
RUN npm install --only=production

COPY server.js .
COPY public/ ./public/
COPY .env .


# Stage 2: Running stage
FROM gcr.io/distroless/nodejs:16

WORKDIR /app
COPY --from=build /app /app

# Create a non-root user
USER 1000

EXPOSE 3000
CMD ["server.js"]