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

FROM gcr.io/distroless/cc-debian11:nonroot AS runtime

WORKDIR /app
COPY --from=builder /build/target/release/quote_app /app/
COPY --from=builder /build/templates templates/

EXPOSE 8080

CMD ["./quote_app"] 