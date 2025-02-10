# FROM golang:1.23.5 as build

# # Environment variables
# ENV ADMIN_USER="admin"

# WORKDIR /go/src/app
# COPY . .

# RUN go mod download
# RUN CGO_ENABLED=0 go build -o /go/bin/app

# # The program will be compiled through this
# FROM gcr.io/distroless/static:nonroot
# COPY --from=build /go/bin/app .

# # Explicitly specify port
# EXPOSE 3000

# CMD ["/app"]

# In this image we build the binary
FROM golang:1.23 AS build

WORKDIR /go/src/app
COPY . .

RUN go mod download
RUN CGO_ENABLED=1 go build -o /go/bin/app

# Now copy it into our base image. 
# We run code in it.
FROM gcr.io/distroless/base-nossl:nonroot
COPY --from=build /go/bin/app /

EXPOSE 8080

CMD ["/app"]
