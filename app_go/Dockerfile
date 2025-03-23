FROM golang:1.23
RUN addgroup --system users && adduser --system user -ingroup users

WORKDIR /app

COPY go.mod go.sum ./
RUN go mod download && go mod verify

COPY main.go .

EXPOSE 8000
USER user
CMD ["go", "run", "."]
