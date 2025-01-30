FROM alpine:3.21.2@sha256:56fa17d2a7e7f168a043a2712e63aed1f8543aeafdcee47c58dcffe38ed51099 AS build

WORKDIR /usr/local/app
RUN apk add build-base
COPY mongoose ./mongoose
COPY app.c ./

RUN gcc -static -I./mongoose mongoose/mongoose.c app.c -o app

FROM gcr.io/distroless/cc-debian12

WORKDIR /app

COPY --from=build /usr/local/app/app /app/app
COPY ./resources /app/resources

EXPOSE 8000

CMD ["/app/app", "0.0.0.0:8000"]
