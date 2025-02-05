FROM node:18-alpine AS build

WORKDIR /app_nodejs

COPY package*.json ./

COPY app.js ./

COPY public/ ./public/

RUN npm install --omit=dev

FROM gcr.io/distroless/nodejs18-debian12:nonroot AS final

COPY --from=build /app_nodejs /app_nodejs

WORKDIR /app_nodejs

EXPOSE 3000

CMD ["app.js"]

