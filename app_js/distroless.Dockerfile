FROM node:18-alpine AS builder

WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .

FROM gcr.io/distroless/nodejs:18

WORKDIR /app
COPY --from=builder /app .

USER nonroot

EXPOSE 3000

CMD ["server.js"]
