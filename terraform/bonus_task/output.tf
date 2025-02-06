output "admin_team_id" {
  value = github_team.admins.id
}

output "developers_team_id" {
  value = github_team.developers.id
}

output "viewers_team_id" {
  value = github_team.viewers.id
}

output "admin_team_name" {
  value = github_team.admins.name
}

output "developers_team_name" {
  value = github_team.developers.name
}

output "viewers_team_name" {
  value = github_team.viewers.name
}
