# Terraform for GitHub

## Used Resources

- `github_repository.my_repo` — GitHub repository
- `github_branch_protection.main_protection` — Branch protection

## Best Terraform Practices

- Use environment variables for sensitive data (e.g., $env:GITHUB_TOKEN).
- Initialize repository with a README (auto_init = true).
