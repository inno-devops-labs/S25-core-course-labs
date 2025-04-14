output "repository_url" {
  description = "URL of the created repository"
  value       = github_repository.S25-core-course-labs.html_url
}

output "repository_id" {
  description = "ID of the created repository"
  value       = github_repository.S25-core-course-labs.node_id
} 