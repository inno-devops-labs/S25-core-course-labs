FROM node:18.16.0-alpine3.15 as base

RUN adduser -D -u 1000 myuser

WORKDIR /app

COPY package.json .

RUN npm install --omit=dev

COPY server.js .

EXPOSE 3000

USER myuser

CMD ["node", "server.js"]