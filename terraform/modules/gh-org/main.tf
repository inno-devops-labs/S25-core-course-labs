provider "github" {
  organization = "inno-devops-fallenchromium"
}

# Create a repository inside the organization
resource "github_repository" "example_repo" {
  name        = var.repo_name
  description = "An example repository managed by Terraform"
  visibility  = "public" # Options: public, private, internal
}

# Create Teams with different privacy settings
resource "github_team" "developers" {
  name        = "Developers"
  description = "Team of developers"
  privacy     = "closed" # Options: closed (visible) or secret
}

resource "github_team" "qa" {
  name        = "QA"
  description = "Quality Assurance team"
  privacy     = "closed"
}

resource "github_team" "admins" {
  name        = "Admins"
  description = "Team with full access"
  privacy     = "secret"
}

# Assign Teams to Repository with Different Permissions
resource "github_team_repository" "developers_access" {
  team_id    = github_team.developers.id
  repository = github_repository.example_repo.name
  permission = "push" # Options: pull (read), push (write), maintain, admin
}

resource "github_team_repository" "qa_access" {
  team_id    = github_team.qa.id
  repository = github_repository.example_repo.name
  permission = "pull" # Read-only access
}

resource "github_team_repository" "admins_access" {
  team_id    = github_team.admins.id
  repository = github_repository.example_repo.name
  permission = "admin" # Full access
}
