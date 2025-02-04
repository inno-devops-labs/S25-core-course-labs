# app_rust

This web application generates a random unsigned 64-bit integer

## Running

- Install latest [rust toolchain](https://www.rust-lang.org/)

- Build the project

```console
cargo build --release
```

- Run the project

```console
./target/release/app_rust
```

## Enabling logging

To set the logging level, `RUST_LOG` environment variable is used.

List of possible values for `RUST_LOG`:

- `error`
- `warn`
- `info`
- `debug`
- `trace`
- `off`

Example that sets logging level to info:

```console
RUST_LOG=info ./target/release/app_rust
```

## Installation

```console
cargo install --root <installation root>
```

This installs the binary into `<installation root>/bin/app_rust`

Note: _the command may require root priveledges_

## Docker

### Building The Image

```console
docker build -t 2imt/app_rust:1.0 .
```

### Pulling The Image

```console
docker pull 2imt/app_rust:1.0
```

### Running The Image

```console
docker run --rm -p 8080:8080 2imt/app_rust:1.0
```

## Unit Tests

```console
cargo test
```

## CI Workflow

- **Dependencies**: Installs the required Rust dependencies.
- **Linting**: Runs `rustfmt` and `cargo-clippy` to check the code style and potential issues.
- **Testing**: Runs tests using `cargo-nextest` to ensure the project is functioning correctly.
- **Docker**: Builds and pushes a Docker image to Docker Hub.
- **Security**: Checks for vulnerabilities using `cargo-audit`.
