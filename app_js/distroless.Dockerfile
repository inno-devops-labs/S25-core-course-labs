FROM node:20-alpine AS builder
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install --omit=dev --no-cache

FROM gcr.io/distroless/nodejs20-debian11:nonroot
WORKDIR /app

COPY --from=builder /app/node_modules /app/node_modules
COPY src/server.js ./

EXPOSE 3000
CMD ["node", "server.js"]
