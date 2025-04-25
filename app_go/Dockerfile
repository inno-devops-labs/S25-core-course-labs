FROM golang:1.23.5-alpine3.21

# Environment variables
ENV ADMIN_USER="admin"

# Copy static file directory
COPY static ./static
# Copy python app file
COPY main.go ./

# Setup an app user so the container doesn't run as the root user
RUN adduser --system $ADMIN_USER
USER $ADMIN_USER

# Compile go application
RUN go build -o randomizer main.go

# Explicitly specify port
EXPOSE 5500

CMD ["./randomizer"]
