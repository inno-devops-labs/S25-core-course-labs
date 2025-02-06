terraform {
  required_version = ">= 1.2.0"
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 4.0"
    }
  }
}

provider "github" {
  token = var.token
  owner = "DevOps-test-iu"
}

resource "github_repository" "repo" {
  name               = var.repository_name
  description        = var.repository_description
  visibility         = var.repository_visibility
  has_issues         = true
  has_wiki           = true
  auto_init          = true
  license_template   = "mit"
  gitignore_template = "VisualStudio"
}

resource "github_team" "dev_team" {
  name        = "Developers"
  description = "Development test team with write access"
  privacy     = "closed"
}

resource "github_team" "qa_team" {
  name        = "QA"
  description = "QA test team with read access"
  privacy     = "closed"
}

resource "github_team_repository" "dev_team_access" {
  team_id    = github_team.dev_team.id
  repository = github_repository.repo.name
  permission = "push"
}

resource "github_team_repository" "qa_team_access" {
  team_id    = github_team.qa_team.id
  repository = github_repository.repo.name
  permission = "pull"
}

resource "github_team_membership" "dev_user1" {
  team_id  = github_team.dev_team.id
  username = "creepydanunity"
  role     = "maintainer"
}

resource "github_branch_default" "default" {
  repository = github_repository.repo.name
  branch     = var.default_branch

  depends_on = [github_repository.repo]
}

resource "github_branch_protection" "default" {
  repository_id                   = github_repository.repo.id
  pattern                         = github_branch_default.default.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}
