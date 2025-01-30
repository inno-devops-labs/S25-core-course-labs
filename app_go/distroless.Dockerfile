FROM golang:1.21-alpine AS builder

WORKDIR /app
COPY main.go .
RUN go mod init app && go mod tidy
RUN go build -o myapp main.go

FROM gcr.io/distroless/static:nonroot

WORKDIR /app
COPY --from=builder /app/myapp .

USER nonroot
CMD ["/app/myapp"]
