terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 6.0"
    }
  }
}

provider "github" {
  token = var.token
  owner = var.organization
}

# Репозиторий
resource "github_repository" "repo" {
  name               = var.repository_name
  description        = var.repository_description
  visibility         = var.repository_visibility
  has_issues         = true
  has_wiki           = true
  auto_init          = true
  gitignore_template = "VisualStudio"
}

resource "github_branch_default" "master" {
  repository = github_repository.repo.name
  branch     = "main"
}

resource "github_branch_protection" "default" {
  repository_id                   = github_repository.repo.id
  pattern                         = github_branch_default.master.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}

resource "github_team" "dev" {
  name        = "Developsy"
  description = "developers team"
  privacy     = "closed"
}

resource "github_team" "qa" {
  name        = "Qa"
  description = "Qa team"
  privacy     = "closed"
}

resource "github_team_repository" "dev_access" {
  team_id    = github_team.dev.id
  repository = github_repository.repo.name
  permission = "push" 
}

resource "github_team_repository" "qa_access" {
  team_id    = github_team.qa.id
  repository = github_repository.repo.name
  permission = "pull"  
}
