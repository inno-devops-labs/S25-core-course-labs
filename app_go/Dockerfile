FROM golang:1.23

WORKDIR /usr/src/app
RUN addgroup --system appgroup 
RUN useradd --system appuser --groups appgroup
RUN chown -R appuser:appgroup /usr/src/app

ARG config_path

COPY go.mod .
COPY go.sum .
RUN go mod download

COPY cmd/ ./cmd
COPY internal/ ./internal
COPY templates/ ./templates  
COPY config/ ./config

RUN mkdir bin

ENV CONFIG_PATH=$config_path

RUN go build -o ./bin/url-shortener ./cmd/url-shortener

EXPOSE 8080

# USER appuser

CMD ["./bin/url-shortener"]