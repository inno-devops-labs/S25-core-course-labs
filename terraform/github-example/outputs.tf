output "repository_id" {
  description = "The ID of the GitHub repository"
  value       = github_repository.core-course-labs.id
}

output "repository_url" {
  description = "The URL of the GitHub repository"
  value       = github_repository.core-course-labs.html_url
}

output "branch_protection_id" {
  description = "The ID of the branch protection rule"
  value       = github_branch_protection.main.id
}
