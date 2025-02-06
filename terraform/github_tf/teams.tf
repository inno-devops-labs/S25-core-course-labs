resource "github_team" "developers" {
  name        = "developers"
  description = "Team for developers with write access"
}

resource "github_team" "admins" {
  name        = "admins"
  description = "Team for administrators with admin access"
}

resource "github_team" "readers" {
  name        = "readers"
  description = "Team for users with read-only access"
}

resource "github_team_repository" "developers_access" {
  team_id    = github_team.developers.id
  repository = github_repository.core_course_labs.name
  permission = "push"
}

resource "github_team_repository" "admins_access" {
  team_id    = github_team.admins.id
  repository = github_repository.core_course_labs.name
  permission = "admin"
}

resource "github_team_repository" "readers_access" {
  team_id    = github_team.readers.id
  repository = github_repository.core_course_labs.name
  permission = "pull"
}

output "developers_team_id" {
  value = github_team.developers.id
}

output "admins_team_id" {
  value = github_team.admins.id
}

output "readers_team_id" {
  value = github_team.readers.id
}