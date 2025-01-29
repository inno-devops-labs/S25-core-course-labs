FROM golang:1.23.5-alpine3.20@sha256:def59a601e724ddac5139d447e8e9f7d0aeec25db287a9ee1615134bcda266e2 AS build

LABEL description="Distroless Go app" maintainer="s.asekrea@innopolis.university"

WORKDIR /build

COPY app.go app_service.go go.mod /build/

# Build the Go application
RUN go build -o app

# from console.cloud.google
FROM gcr.io/distroless/static-debian12:nonroot@sha256:6ec5aa99dc335666e79dc64e4a6c8b89c33a543a1967f20d360922a80dd21f02

WORKDIR /app

# transfers the compiled application (app) from the build image.
COPY --from=build /build/app ./

EXPOSE 8002

CMD ["./app"]