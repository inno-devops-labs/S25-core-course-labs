FROM golang:1.23-alpine3.20

ARG USERUID=10001
ARG USERGID=10001

# Create user and group
RUN addgroup -g "${USERGID}" user && \
    adduser -D -u "${USERUID}" -G user user

WORKDIR /app

COPY . .

RUN go mod download && \
    go build -o /app/service

# Create /data directory and set correct ownership
RUN mkdir -p /data && chown -R user:user /app && chown -R user:user /data

USER user

EXPOSE 8080

CMD ["/app/service"]