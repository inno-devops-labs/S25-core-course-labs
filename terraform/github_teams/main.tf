terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 4.0"
    }
  }
}

provider "github" {
  owner = var.github_organization
  token = var.token
}

resource "github_repository" "repo" {
  name        = "S25-core-course-labs"
  visibility  = "public"
  has_issues  = true
  has_wiki    = true
  auto_init   = true
}

resource "github_branch_default" "main" {
  repository = github_repository.repo.name
  branch     = "main"
}

# Branch Protection Rule
resource "github_branch_protection" "default" {
  repository_id                   = github_repository.repo.id
  pattern                         = github_branch_default.main.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 0
  }
}

resource "github_team" "maintain_team" {
  name        = "maintain-team"
  description = "Team with maintain access to the repository"
  privacy     = "closed"
}

resource "github_team" "contributors_team" {
  name        = "contributors-team"
  description = "Team with push access to the repository"
  privacy     = "closed"
}

resource "github_team_repository" "maintain_team_repo" {
  team_id    = github_team.maintain_team.id
  repository = github_repository.repo.name
  permission = "maintain"
}

resource "github_team_repository" "contributors_team_repo" {
  team_id    = github_team.contributors_team.id
  repository = github_repository.repo.name
  permission = "push"
}