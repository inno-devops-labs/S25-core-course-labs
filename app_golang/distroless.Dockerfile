FROM golang:1.23.5-alpine3.21 AS build

WORKDIR /app_golang

COPY go.mod go.sum /app_golang/
COPY src/ /app_golang/src/

RUN go mod download && go build src/main.go


FROM gcr.io/distroless/static-debian12:nonroot AS run

WORKDIR /app_golang

COPY --from=build /app_golang/main /app_golang/.
COPY --from=build /app_golang/src/templates/ /app_golang/src/templates/

EXPOSE 80/tcp

CMD ["./main"]