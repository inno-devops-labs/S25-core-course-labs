# Continuous Integration (CI) Best Practices

This document outlines the best practices implemented in the GitHub Actions CI workflow for the C# application.

## **CI Workflow Overview**

The CI workflow (`csharp_app_ci.yml`) is triggered on `pull_request` events that modify files in `app_csharp/` or the workflow itself. It consists of three sequential jobs:

1. **Build, Lint, and Test**  
2. **Security Check**  
3. **Docker Build & Push**  

---

## **Best Practices Implemented**

### ✅ **1. Optimized Dependency Management**

- **NuGet package caching**  
  Uses GitHub Actions Cache with granular paths (excludes `bin`/`obj` directories) and project-specific cache keys based on `MoscowTimeApp.csproj`.  
- **`.NET 8.0.x` version pinning**  
  Ensures consistent environment setup using `actions/setup-dotnet@v3`.  
- **Incremental builds**  
  Uses `--no-restore` and `--no-build` flags to optimize build/test execution speed.  

### ✅ **2. Code Quality Assurance**

- **`dotnet format` for linting**  
  Enforces code style consistency via `--verify-no-changes` to fail on formatting issues.  
- **Strict build configuration**  
  Uses `--configuration Release` for both build and test steps to ensure production-grade checks.  
- **Test isolation**  
  Runs tests separately after building to ensure clean execution.  

### ✅ **3. Security Checks**

- **Snyk dependency scanning**  
  Scans `.sln` file for vulnerabilities using the official `snyk/actions/dotnet` integration.  
- **Secret protection**  
  Uses `SNYK_TOKEN` stored in GitHub Secrets for secure authentication.  

### ✅ **4. Safe CI Execution**

- **Job dependencies via `needs`**  
  - Security checks only run after successful build/test.  
  - Docker builds require both build/test and security checks to pass.  
- **Failure isolation**  
  Errors in linting, building, or testing block subsequent security/docker steps.  

### ✅ **5. Production-Ready Docker Images**

- **Multi-architecture support**  
  Uses `docker/setup-buildx-action@v2` for cross-platform builds.  
- **Distroless image variant**  
  Provides minimal attack surface with `distroless.Dockerfile`.  
- **Secure credential handling**  
  Uses GitHub Secrets (`DOCKER_USERNAME`, `DOCKER_PASSWORD`) for registry auth.  
- **GH Actions cache optimization**  
  Leverages `cache-to`/`cache-from` for efficient Docker layer caching.  
  