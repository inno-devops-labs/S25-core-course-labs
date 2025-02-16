resource "github_team" "dev_team" {
  name        = "Developers"
  description = "Development Team"
  privacy     = "closed"
}

resource "github_team_repository" "dev_team_repo" {
  team_id    = github_team.dev_team.id
  repository = github_repository.course_repo.name
  permission = "push"
}
