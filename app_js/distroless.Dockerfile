FROM node:18.16.0-alpine3.15 as build

WORKDIR /app
COPY package.json .
RUN npm install --omit=dev

COPY server.js .

FROM gcr.io/distroless/nodejs18:nonroot

WORKDIR /app
COPY --from=build /app /app

EXPOSE 3000

CMD ["/app/server.js"]
