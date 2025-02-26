FROM node:18-slim AS build

RUN adduser nonrootuser

USER nonrootuser

WORKDIR /app_nodejs

COPY --chown=nonrootuser:nonrootuser package*.json app.js ./

RUN npm install --only=production

COPY --chown=nonrootuser:nonrootuser public/ ./public/

EXPOSE 3000

CMD ["node", "app.js"]

