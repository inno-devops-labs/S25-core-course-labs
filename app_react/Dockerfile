FROM node:18.19-alpine3.18

# create non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

WORKDIR /app

COPY package*.json ./

# dependencies installation
RUN npm ci

RUN npm install serve

COPY . .

RUN npm run build

# change owner of the app directory
RUN chown -R appuser:appgroup /app

# switch to non-root user
USER appuser

EXPOSE 3000

CMD ["./node_modules/.bin/serve", "-s", "dist", "-l", "3000"]