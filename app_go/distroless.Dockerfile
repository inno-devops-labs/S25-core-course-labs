FROM golang:1.23 AS build

WORKDIR /usr/src/app

ARG config_path

COPY go.mod .
COPY go.sum .
RUN go mod download

COPY cmd/ ./cmd
COPY internal/ ./internal
COPY templates/ ./templates  
COPY config/ ./config

RUN go build -o ./url-shortener ./cmd/url-shortener

FROM gcr.io/distroless/base-debian12:nonroot

WORKDIR /app

COPY --from=build /usr/src/app/url-shortener /app/url-shortener
COPY --from=build /usr/src/app/config /app/config
COPY --from=build /usr/src/app/templates/ /app/templates


ARG config_path
ENV CONFIG_PATH=$config_path

EXPOSE 8080

ENTRYPOINT ["/app/url-shortener"]