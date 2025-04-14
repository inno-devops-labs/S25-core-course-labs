FROM rust:1.84-slim-bullseye AS builder

RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser
WORKDIR /app

COPY Cargo.toml Cargo.lock ./
COPY src ./src

RUN cargo build --release

FROM debian:bullseye-slim

RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser
WORKDIR /app
COPY --from=builder /app/target/release/app_rust /app/app_rust
USER appuser

EXPOSE 8080

CMD ["./app_rust"]
