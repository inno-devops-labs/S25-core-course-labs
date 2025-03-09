terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 4.0"
    }
  }
}

provider "github" {
  token = var.token # or `GITHUB_TOKEN`
  owner = "terraformOrgSecretanry"
}

#Create and initialise a public GitHub Repository with MIT license and a Visual Studio .gitignore file (incl. issues and wiki)
resource "github_repository" "repo" {
  name               = "TerraformRepo"
  description        = "My awesome automated codebase"
  visibility         = "public"
  has_issues         = true
  has_wiki           = true
  auto_init          = true
  license_template   = "mit"
  gitignore_template = "VisualStudio"
}

#Set default branch 'main'
resource "github_branch_default" "main" {
  repository = github_repository.repo.name
  branch     = "main"
}

resource "github_branch_protection" "default" {
  repository_id                   = github_repository.repo.id
  pattern                         = github_branch_default.main.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}

resource "github_team" "dev_team" {
  name        = "Dev Team"
  description = "Team responsible for development work."
  privacy     = "closed"
}

resource "github_team" "qa_team" {
  name        = "QA Team"
  description = "Team responsible for quality assurance."
  privacy     = "closed"
}

resource "github_team" "ops_team" {
  name        = "Ops Team"
  description = "Team responsible for operations and administrative access."
  privacy     = "closed"
}

resource "github_team_repository" "dev_team_repo_access" {
  team_id    = github_team.dev_team.id
  repository = github_repository.repo.name
  permission = "push"
}

resource "github_team_repository" "qa_team_repo_access" {
  team_id    = github_team.qa_team.id
  repository = github_repository.repo.name
  permission = "triage"
}

resource "github_team_repository" "ops_team_repo_access" {
  team_id    = github_team.ops_team.id
  repository = github_repository.repo.name
  permission = "admin"
}