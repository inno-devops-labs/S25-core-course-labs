FROM node:16-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

# Проверяем содержимое директории для отладки
RUN ls -la

EXPOSE 3000

# Используем server.js
CMD ["node", "./server.js"]
