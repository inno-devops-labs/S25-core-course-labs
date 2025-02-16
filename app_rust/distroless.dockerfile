# Stage 1: Build the application
FROM rust:1.84-slim-bullseye AS builder

# Rootless user
RUN useradd -m appuser
WORKDIR /home/appuser/app

# Copy sources
COPY Rocket.toml ./
COPY Cargo.toml Cargo.lock ./
COPY src ./src

# Build application
RUN cargo build --release

# Stage 2: Create a minimal image with the application
FROM gcr.io/distroless/cc:nonroot

# Copy application binary with Rocket.toml config
WORKDIR /app
COPY --from=builder /home/appuser/app/target/release/app_rust ./app
COPY --from=builder /home/appuser/app/Rocket.toml ./Rocket.toml

EXPOSE 8000

CMD ["./app"]
