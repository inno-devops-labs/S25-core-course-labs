# Continuous Integration

## Jobs

1) Validate with Python app installing, linting and testing.
2) Build with docker building and publishing to registry.

## Best practices

1) Job dependencies
2) Triggers only on changes to `main`
3) Triggers only when changes in `app_python` directory
4) Docker build caching