FROM node:18-alpine AS builder
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install --only=production

FROM gcr.io/distroless/nodejs18:nonroot
WORKDIR /app
COPY --from=builder /app/node_modules /app/node_modules
COPY . .
CMD ["app.js"]
