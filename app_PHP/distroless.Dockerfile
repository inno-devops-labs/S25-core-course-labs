FROM ghcr.io/s6n-labs/distroless-php:8.3.0-bookworm

WORKDIR /usr/local/app
COPY PHPtest.php ./

EXPOSE 8000

CMD ["php", "-S", "0.0.0.0:8000", "PHPtest.php"]
