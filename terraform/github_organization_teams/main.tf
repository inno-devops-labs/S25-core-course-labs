terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 4.0"
    }
  }
}

provider "github" {
  token = var.token
  owner = var.organization
}

resource "github_repository" "repo" {
  name          = var.repo_config.name
  description   = var.repo_config.desc
  visibility    = var.repo_config.visibility
  has_downloads = var.repo_config.has_downloads
  has_projects  = var.repo_config.has_projects
  has_wiki      = var.repo_config.has_wiki
  auto_init     = var.repo_config.auto_init
}

resource "github_branch_default" "main" {
  repository = github_repository.repo.name
  branch     = var.default_branch
  depends_on = [github_repository.repo]
}

resource "github_branch_protection" "default" {
  repository_id                   = github_repository.repo.id
  pattern                         = var.default_branch
  require_conversation_resolution = var.require_conversation_resolution
  enforce_admins                  = var.enforce_admins
}



resource "github_team" "team_1" {
  name        = var.team_1_config.name
  description = var.team_1_config.desc
  privacy     = var.team_1_config.privacy
}

resource "github_team" "team_2" {
  name        = var.team_2_config.name
  description = var.team_2_config.desc
  privacy     = var.team_2_config.privacy
}

resource "github_team_repository" "team_1_access" {
  team_id    = github_team.team_1.id
  repository = github_repository.repo.name
  permission = var.team_1_config.permission
}

resource "github_team_repository" "team_2_access" {
  team_id    = github_team.team_2.id
  repository = github_repository.repo.name
  permission = var.team_2_config.permission
}
