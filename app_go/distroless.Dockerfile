FROM golang:1.23.5-alpine3.21 AS build

WORKDIR /app

# install dependencies
COPY go.mod go.sum ./
RUN go mod download

# copy app
COPY cmd/ cmd/
COPY internal/ internal/

# build app
RUN go build -o build/main cmd/main.go

FROM gcr.io/distroless/static-debian12:nonroot

WORKDIR /app

# copy built files
COPY --from=build /app/build/main .
COPY internal/templates/ internal/templates/
COPY static/ static/

EXPOSE 8080

ENV GIN_MODE=release

# command to run application
CMD ["./main"]
