FROM node:18-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm install --only=production

COPY . .

FROM gcr.io/distroless/nodejs:18

WORKDIR /app
COPY --from=builder /app /app

EXPOSE 3000

CMD ["server.js"]

