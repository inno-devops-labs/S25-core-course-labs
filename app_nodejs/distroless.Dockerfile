FROM gcr.io/distroless/nodejs18:nonroot

WORKDIR /app

# Copy application files
COPY . /app/

EXPOSE 8000

# Corrected CMD statement
CMD ["server.js"]
