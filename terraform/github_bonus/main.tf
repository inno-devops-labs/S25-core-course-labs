resource "github_repository" "devops_labs" {
  name        = "S25-core-course-labs"
  description = "DevOps course labs solutions"
  visibility  = "public"
}


resource "github_team" "read_team" {
  name        = "read-team"
  description = "Team with read access to the repo"
  privacy     = "closed"
}

resource "github_team" "write_team" {
  name        = "write-team"
  description = "Team with write access to the repo"
  privacy     = "closed"
}

resource "github_team" "admin_team" {
  name        = "admin-team"
  description = "Team with admin access to the repo"
  privacy     = "closed"
}

resource "github_team_repository" "read_team_repo" {
  team_id    = github_team.read_team.id
  repository = github_repository.devops_labs.name
  permission = "pull"
}

resource "github_team_repository" "write_team_repo" {
  team_id    = github_team.write_team.id
  repository = github_repository.devops_labs.name
  permission = "push"
}

resource "github_team_repository" "admin_team_repo" {
  team_id    = github_team.admin_team.id
  repository = github_repository.devops_labs.name
  permission = "admin"
}
