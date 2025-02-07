resource "github_team" "dev_team" {
  name        = "Developers"
  description = "Team for developers with write access"
  privacy     = "closed"
}

resource "github_team" "ops_team" {
  name        = "Ops"
  description = "Team for operations with read access"
  privacy     = "closed"
}

resource "github_team_repository" "dev_team_repo" {
  team_id    = github_team.dev_team.id
  repository = github_repository.core_course_labs.name
  permission = "push"
}

resource "github_team_repository" "ops_team_repo" {
  team_id    = github_team.ops_team.id
  repository = github_repository.core_course_labs.name
  permission = "pull"
}
