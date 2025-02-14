FROM node:18-alpine as build

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

WORKDIR /app

COPY package.json .

RUN npm install --omit=dev

COPY server.js .

RUN chown -R appuser:appgroup /app
USER appuser

EXPOSE 3001
CMD ["node", "server.js"]