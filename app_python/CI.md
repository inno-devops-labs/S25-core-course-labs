# CI Best Practices Used

1. **Use build caching**: Caches dependencies (pip) to speed up subsequent builds.
2. **Upload test and SAST results as artifacts**: Saves reports for debugging, tracking performance and applying measures.
3. **Authenticate securely**: Uses GitHub Secrets to securely pass sensitive credentials for Docker and Snyk.
4. **Define explicit job dependencies**: Uses needs: to ensure jobs run in the correct sequence, preventing unnecessary failures.
5. **Use a distroless image**: Minimizes image size and attack surface by removing unnecessary OS packages and reducing vulnerabilities.
