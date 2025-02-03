# CI Pipeline

## Best Practices

1. Structured Workflow Organization

   Each job is independent and runs only if the previous stage succeeds, ensuring early failure detection.

2. Workflow Trigger Optimization

   The pipeline triggers only when changes occur in the app_nodejs/ directory or CI workflow files.
 
3. Efficient Dependency Management

   The workflow uses Node.js caching (cache: "npm") to store dependencies, reducing installation time.

4. Automated Deployment to Docker Hub

   The pipeline builds and pushes the latest Docker image only after successful tests.

