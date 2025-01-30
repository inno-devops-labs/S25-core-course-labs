# build stage
FROM node:18-slim as builder

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build
RUN npm install -g http-server

# Production stage
FROM gcr.io/distroless/nodejs:18

WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /usr/local/lib/node_modules/http-server /app/http-server

EXPOSE 3000

CMD ["/app/http-server/bin/http-server", "dist", "-p", "3000"]