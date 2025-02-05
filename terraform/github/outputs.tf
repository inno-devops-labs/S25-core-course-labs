output "repository_id" {
  description = "The ID of the created GitHub repository"
  value       = github_repository.my_repo.node_id
}

output "repository_name" {
  description = "The name of the GitHub repository"
  value       = github_repository.my_repo.name
}

output "repository_url" {
  description = "The URL of the GitHub repository"
  value       = github_repository.my_repo.html_url
}
