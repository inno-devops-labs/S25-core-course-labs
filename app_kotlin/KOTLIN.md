# Coding description

## Frameworks used

Ktor is used for its lightweight nature. It is efficient enough for small apps (similar frameworks like Spring would be too heavy for this use case).

Timezone is handled with use of `java.time` package, it doesn't depend on server location.

## Code style

- Separation of logic and template (`Application.kt` and `index.html`)
- Readable code, following Kotlin conventions
- Manual testing
- Dependencies in `build.gradle.kts`
- Unnecessary files are indicated in `.gitignore`
