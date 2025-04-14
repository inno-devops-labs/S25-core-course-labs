FROM node:16-slim

# working directory is app
WORKDIR /app

COPY package*.json ./

# special tool that I've added to handle properly SIGINT (Ctrl + C) signal
RUN apt-get update && apt-get install -y tini && apt-get clean && rm -rf /var/lib/apt/lists/*
ENTRYPOINT ["/usr/bin/tini", "--"]

RUN npm install --only=production

# creating non-root user and give him ownership of the /app dir
RUN addgroup --system appuser && \
    adduser --system --group appuser && \
    chown -R appuser:appuser /app
USER appuser

COPY server.js .
COPY public/ ./public/

COPY .env .

EXPOSE 3000
CMD ["node", "server.js"]