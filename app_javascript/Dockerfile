FROM node:18.18.0-alpine3.18
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
WORKDIR /usr/share/app
COPY /src /usr/share/app/
RUN npm install -g http-server@14.1.1 \
    && chown -R appuser:appgroup /usr/share/app \
    && rm -rf /root/.npm
EXPOSE 8080
USER appuser
CMD ["http-server", "-p", "8080"]
