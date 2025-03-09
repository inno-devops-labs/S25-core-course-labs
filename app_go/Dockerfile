FROM golang:1.23 AS builder

RUN useradd --create-home builder
WORKDIR /home/builder

USER builder

COPY go.mod .
COPY go.sum .

COPY main.go .

RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -buildvcs=false -o go-binary


FROM alpine:3.14

# Add the executor user with a specified home directory
RUN adduser -D -h /home/executor executor && \
    mkdir -p /home/executor && \
    chown executor:executor /home/executor

WORKDIR /home/executor

USER executor

# Copy the binary from the builder stage
COPY --from=builder /home/builder/go-binary .
COPY ./templates ./templates

# Ensure the binary is executable
RUN chmod +x ./go-binary

EXPOSE 8080

RUN mkdir -p "data"

CMD [ "./go-binary" ]