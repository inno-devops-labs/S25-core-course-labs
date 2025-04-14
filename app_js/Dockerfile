FROM node:20-slim AS base

WORKDIR /app

COPY package*.json ./
RUN npm i

COPY src src
COPY public public
COPY ./*.json ./*.js ./*.ts index.html ./
RUN npm run build

COPY entrypoint.sh ./
RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
