FROM node:20.11-alpine3.19 AS builder

WORKDIR /app

COPY package*.json ./
RUN npm install --production

COPY app.js .

FROM gcr.io/distroless/nodejs20-debian11:nonroot

WORKDIR /app

COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/app.js .

EXPOSE 3000

CMD ["app.js"]
