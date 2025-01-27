FROM golang:1.23-alpine AS builder

# Set the working directory 
WORKDIR /app_golang

# Copy the file with dependencies and install them
COPY go.mod ./
RUN go mod download

# Copy the main file, build it under the name "server" and grant execution permissions
COPY main.go .
RUN go build -o server main.go \  
    && chmod +x server

# Use a distroless image without root privileges 
FROM gcr.io/distroless/base-debian12:nonroot

# Change to the working directory 
WORKDIR /app_golang

# Copy data from the intermediate image and other necessary components 
COPY --from=builder /app_golang/server /app_golang/  
COPY static/ static/
COPY templates/ templates/

# Open a port to access the application
EXPOSE 8000

# Command to run our server (web app)
CMD ["/app_golang/server"]  