# Dockerfile Comparison: Original vs Distroless

## 1. Differences Between Images
### Original Image:
- Base Image: `python:3.11-slim-bookworm `
- Size: Larger (e.g., ~43.5MB)
- Features: Includes a shell, package manager, and debugging tools.
- Security: Slightly more exposed due to unnecessary components (e.g., Bash, apt).

### Distroless Image:
- Base Image: `gcr.io/distroless/python3-debian11:nonroot`
- Size: Smaller (e.g., ~26.7MB)
- Features: Minimal runtime environment with no shell or package manager.
- Security: Reduced attack surface due to lack of unnecessary tools.

## 2. Why These Differences Exist
- The Distroless image removes unnecessary components (e.g., Bash, apt, libraries).
- Only includes essential runtime files, which decreases the chance of vulnerabilities.
- Distroless ensures better security by running as a non-root user.

