FROM node:20-alpine AS builder
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install --omit=dev --no-cache

FROM node:20-alpine
WORKDIR /app

COPY --from=builder /app/node_modules /app/node_modules
COPY src/server.js ./

RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

EXPOSE 3000
CMD ["node", "server.js"]
