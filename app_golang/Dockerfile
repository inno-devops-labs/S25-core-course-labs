# use a specific version of golang 
FROM golang:1.23-alpine AS builder

# working directorate
WORKDIR /app_go

# copy go.mod and install dependencies 
COPY go.mod ./
RUN go mod download

# building web app
COPY main.go .
RUN go build -o main .

FROM alpine:latest

# working directorate
WORKDIR /app_go

# create a regular user and give it permissions
RUN adduser -D user
COPY --chown=user:user --from=builder /app_go/main .
COPY --chown=user:user static/ static/
COPY --chown=user:user templates/ templates/

# switch to the created user
USER user

# open a port to access the application
EXPOSE 8000

# run the web application
CMD ["./main"]