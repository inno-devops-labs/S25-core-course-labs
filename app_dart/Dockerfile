FROM ghcr.io/cirruslabs/flutter:3.27.3 AS builder

WORKDIR /app

COPY lib/ lib/
COPY web web/
COPY pubspec.yaml .

RUN flutter clean
RUN flutter build web --release

RUN addgroup --system appuser && \
  adduser --system --group appuser && \
  chown -R appuser:appuser /app

USER appuser

FROM nginx:1.27.3-alpine
COPY --from=builder /app/build/web /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]