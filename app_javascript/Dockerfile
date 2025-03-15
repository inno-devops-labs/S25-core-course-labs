FROM node:18.18.0-alpine3.18
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
WORKDIR /usr/share/app
COPY /src /usr/share/app/
COPY package.json /usr/share/app/package.json
COPY package-lock.json /usr/share/app/package-lock.json
RUN npm install \
    && chown -R appuser:appgroup /usr/share/app \
    && rm -rf /root/.npm
EXPOSE 8080
USER appuser
CMD ["sh", "-c", "node /usr/share/app/server.js"]
