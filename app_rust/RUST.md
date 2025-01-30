# Rust Web Application - Random Quote Display

## Framework Choice: Actix-web

Actix-web was chosen for this project for several reasons:

1. **Performance**: One of the fastest web frameworks available, consistently ranking high in benchmarks.

2. **Safety**: Leverages Rust's safety guarantees and ownership system.

3. **Modern Features**: Built with async/await support and modern Rust practices.

4. **Scalability**: Excellent support for concurrent connections and high-performance requirements.

5. **Active Community**: Well-maintained with regular updates and strong community support.

## Best Practices Applied

1. **Clean Code**: Following Rust idioms and style guidelines.
2. **Separation of Concerns**: HTML templates separated from Rust logic.
3. **Static Data**: Efficient use of static data for quotes.
4. **Code Quality Tools**:
   - Using `cargo fix` to automatically fix common code issues and apply suggested improvements
   - Leveraging `clippy` (via `cargo clippy`) for additional linting and catching common mistakes
   - Following clippy suggestions to write more idiomatic Rust code
   - Regular runs of these tools ensure consistent code quality
