output "team_ids" {
  description = "List of GitHub Teams created"
  value       = { for team in github_team.teams : team.name => team.id }
}

output "repository_access" {
  description = "Teams and their access levels to the repository"
  value       = { for team in github_team_repository.team_access : team.team_id => team.permission }
}
