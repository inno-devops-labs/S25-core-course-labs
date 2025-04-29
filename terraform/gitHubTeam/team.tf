provider "github" {
  token = var.github_token
  owner = var.github_owner
}

resource "github_team" "admin_team" {
  name        = "admins"
  description = "Team with admin access to the repository"
  privacy     = "closed"
}

resource "github_team" "developer_team" {
  name        = "developers"
  description = "Team with write access to the repository"
  privacy     = "closed"
}

resource "github_team_repository" "admin_repo" {
  team_id    = github_team.admin_team.id
  repository = var.github_repository
  permission = "admin"
}

resource "github_team_repository" "developer_repo" {
  team_id    = github_team.developer_team.id
  repository = var.github_repository
  permission = "push"
}
