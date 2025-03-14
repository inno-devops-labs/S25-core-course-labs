FROM node:20.11-alpine3.19

RUN adduser -D appuser

WORKDIR /app

# Create data directory and set permissions
RUN mkdir -p /data && chown -R appuser:appuser /data && chmod 755 /data

COPY --chown=appuser:appuser package*.json ./

RUN npm install --production

COPY --chown=appuser:appuser app.js .

USER appuser

EXPOSE 3000

CMD ["node", "app.js"]
