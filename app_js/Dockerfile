FROM node:20-alpine AS builder
WORKDIR /app

COPY package*.json ./
RUN npm ci --omit=dev

COPY . .

RUN npm i

FROM gcr.io/distroless/nodejs20:nonroot
WORKDIR /app

# Copy built files and dependencies
COPY --from=builder /app /app

EXPOSE 3000

# Run the application
CMD ["app.js"]
