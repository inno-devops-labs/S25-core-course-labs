# Use Node.js for building
FROM node:18 AS builder

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install --only=production

COPY . .

# Use Distroless runtime
FROM gcr.io/distroless/nodejs18-debian12:nonroot

WORKDIR /app

COPY --from=builder /app .

EXPOSE 3030

CMD ["server.js"]