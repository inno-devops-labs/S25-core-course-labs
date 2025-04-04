
### Best Practices

1. __Path-Based Triggers__ - The workflow is executed only when any file within app_python/ directory was changed

2. __Password and Username Secrets__ - For security enhancement the `Secrets` variables allow hiding personal access tokens

3. __Variables__ - Make script more maintainable by reducing duplicated code framgents

4. __Explicit Version__ - The same as with `Dockerfile`, explicit tool versioning allows better code debugging and understanding its limits.

5. __Docker Caching__ - `cache-from` and `cache-to` attributes of building and pushing Docker image accelerate the process 

6. __Snyk vulnerabilities check__ - Another Security enhancement
