FROM node:22-alpine3.18 AS base
LABEL authors="dmhd6219"

RUN adduser app_typescript_user --system --shell=/bin/false
USER app_typescript_user
WORKDIR /app_typescript

COPY --chown=app_typescript_user:app_typescript_user package.json ./
RUN npm install

COPY --chown=app_typescript_user:app_typescript_user index.html tsconfig.app.json tsconfig.json tsconfig.node.json vite.config.ts ./
COPY --chown=app_typescript_user:app_typescript_user public/ ./public/
COPY --chown=app_typescript_user:app_typescript_user src/ ./src/

RUN npm run build

ENV NODE_ENV="production"
EXPOSE 8080
CMD [ "npm", "run", "preview" ]