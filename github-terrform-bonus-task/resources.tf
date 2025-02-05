resource "github_repository" "my_repo" {
  name        = "my-terraform-repo"
  description = "Managed by Terraform"
  visibility  = "public"
  auto_init   = true
}

resource "github_team" "developers" {
  name        = "Developers"
  description = "Team responsible for application development"
  privacy     = "closed"
}

resource "github_team" "qa" {
  name        = "QA"
  description = "Team responsible for testing and quality assurance"
  privacy     = "closed"
}

resource "github_team" "admins" {
  name        = "Admins"
  description = "Team with full access to the repository"
  privacy     = "closed"
}

resource "github_team_repository" "developers_access" {
  team_id    = github_team.developers.id
  repository = github_repository.my_repo.name
  permission = "push"
}

resource "github_team_repository" "qa_access" {
  team_id    = github_team.qa.id
  repository = github_repository.my_repo.name
  permission = "pull"
}

resource "github_team_repository" "admins_access" {
  team_id    = github_team.admins.id
  repository = github_repository.my_repo.name
  permission = "admin"
}