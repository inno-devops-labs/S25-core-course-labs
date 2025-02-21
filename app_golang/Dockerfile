FROM golang:1.23.5-alpine3.21 AS build

WORKDIR /app_golang

COPY go.mod go.sum /app_golang/
COPY src/ /app_golang/src/

RUN go mod download && go build src/main.go


FROM alpine:3.21.2 AS run

RUN adduser --system --no-create-home gin

RUN apk add --no-cache curl=8.12.1-r0

HEALTHCHECK --interval=30s --timeout=3s \
    CMD curl -f http://localhost/ || exit 1

WORKDIR /app_golang

COPY --from=build /app_golang/main /app_golang/.
COPY --from=build /app_golang/src/templates/ /app_golang/src/templates/

USER gin

EXPOSE 80/tcp

CMD ["./main"]