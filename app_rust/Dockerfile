FROM rust:1-slim-bullseye AS builder

WORKDIR /build

RUN addgroup --gid 42000 app && \
    useradd --create-home --uid 42000 --gid app app && \
    chown -R app:app /build && \
    chmod 755 /build

USER app

# Copy dependency files first to utilize cache
COPY ./Cargo.lock .
COPY ./Cargo.toml .

# Build dependencies only to create a cached layer
RUN mkdir src && \
    echo "fn main() {}" > src/main.rs && \
    cargo build --release && \
    rm -rf src

# Copy source code and templates
COPY ./src ./src
COPY ./templates ./templates

# Build the application
RUN cargo build --release


FROM debian:bookworm-slim AS runtime

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    ca-certificates nano curl libc6 libstdc++6 && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN useradd appuser -u 10000
USER appuser

COPY --from=builder /build/target/release/quote_app .
COPY --from=builder /build/templates ./templates

EXPOSE 8080

CMD ["./quote_app"]
