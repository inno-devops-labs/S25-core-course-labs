provider "github" {
  token = "GITHUB_PERSONAL_ACCESS_TOKEN"
  owner = "organization"
}

resource "github_team" "developers" {
  name        = "Developers"
  description = "Developer team"
  privacy     = "closed"
}

resource "github_team" "qa" {
  name        = "QA"
  description = "Testing team"
  privacy     = "closed"
}

resource "github_team_repository" "dev_repo_access" {
  team_id    = github_team.developers.id
  repository = "repo-name"
  permission = "push"
}

resource "github_team_repository" "qa_repo_access" {
  team_id    = github_team.qa.id
  repository = "repo-name"
  permission = "pull"
}
