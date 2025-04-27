output "repository_id" {
  description = "The ID of the GitHub repository"
  value       = github_repository.core-course-labs.id
}

output "repository_url" {
  description = "The URL of the GitHub repository"
  value       = github_repository.core-course-labs.html_url
}

output "admins_team_id" {
  description = "The ID of the admins team"
  value       = github_team.admins.id
}

output "maintainers_team_id" {
  description = "The ID of the maintainers team"
  value       = github_team.maintainers.id
}

output "contributors_team_id" {
  description = "The ID of the contributors team"
  value       = github_team.contributors.id
}
