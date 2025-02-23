FROM php:fpm-alpine3.20@sha256:5f6c116c7f4ac2cd8e23c2f94bcff487351e0591d1813e4c6d38bff2c0563c5a

WORKDIR /usr/local/app
COPY PHPtest.php ./

RUN apk update
RUN apk upgrade
RUN apk add --upgrade collectd-pinba

EXPOSE 8000

RUN addgroup -S myApp && adduser -S myApp -G myApp
USER myApp

CMD ["php", "-S", "0.0.0.0:8000", "PHPtest.php"]
