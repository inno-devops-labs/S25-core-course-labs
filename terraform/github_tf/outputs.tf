output "repository_url" {
  value       = "https://github.com/RwKaLs/${github_repository.devops_labs.name}"
  description = "The URL of the created GitHub repository"
}

output "default_branch" {
  value       = github_branch_default.default_branch.branch
  description = "The default branch of the repository"
}
