# CI: Flutter app

## Workflow overview
This Flutter app uses **GitHub Actions** to automate:
1. **Building & Testing**  
2. **Security Scanning (Snyk)**  
3. **Docker Image Build & Push**  

## Steps in CI pipeline
1. **Code Checkout**  
2. **Setup Flutter & Dependencies**  
3. **Linting (`flutter analyze`)**  
4. **Unit Testing (`flutter test`)**  
5. **Security Scan (Snyk)**
6. **Docker Build & Push** (if on `push` event)

## Snyk integration
- The workflow includes a **Snyk security scan** to detect vulnerabilities in dependencies.
- The scan is triggered **after tests pass**.
- Snyk requires an API token (`SNYK_TOKEN`) stored in **GitHub Secrets**.