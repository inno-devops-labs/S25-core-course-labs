FROM golang:1.23.5-alpine3.20@sha256:def59a601e724ddac5139d447e8e9f7d0aeec25db287a9ee1615134bcda266e2 AS build

LABEL description="This is a simple Go app" maintainer="s.asekrea@innopolis.university"

WORKDIR /build

COPY app.go app_service.go go.mod /build/

# # Build the Go application
RUN go build -o app

# final base image
FROM alpine:3.20.5@sha256:31687a2fdd021f85955bf2d0c2682e9c0949827560e1db546358ea094f740f12 AS release

RUN addgroup -S app_group && adduser -S app_user -G app_group

# installs the tzdata package into the Alpine Linux-based image
RUN apk add --no-cache tzdata

WORKDIR /app

# transfers the compiled application (app) from the build image to the release image.
COPY --from=build /build/app ./

RUN chown -R app_user:app_group /app

# Change the user to the non-root user
USER app_user

EXPOSE 8002

CMD ["./app"]