# Terraform Best Practices for GitHub Infrastructure

1. **Use Environment Variables**

   - The token and owner are not hardcoded in `.tf` files.

2. **State Management**

   - Storing sensitive state in public repos was avoided.

3. **Version Locking**
   - The `version = "~> 5.0"` is specified for `github` provider.
