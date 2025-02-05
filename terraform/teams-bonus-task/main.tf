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
  token = var.github_token
}

# 🏢 Create GitHub Teams
resource "github_team" "maintainers" {
  name        = "Repository Maintainers"
  description = "Stakeholders"
  privacy     = "closed"
}

resource "github_team" "contributors" {
  name        = "Repository Contributors"
  description = "Contributors from open-source"
  privacy     = "closed"
}

# 📦 Create a GitHub Repository
resource "github_repository" "repository" {
  name         = "DevOps-Course"
  description  = "Let's create this to testing purposes"
  visibility   = "public"
  has_issues   = true
  has_wiki     = false
  auto_init    = true
  allow_auto_merge = true
  delete_branch_on_merge = true
}

# 🔀 Set Default Branch
resource "github_branch_default" "main_branch" {
  repository = github_repository.repository.name
  branch     = "main"
}

# 🛡️ Enable Branch Protection
resource "github_branch_protection" "repo_protection" {
  repository_id                   = github_repository.repository.id
  pattern                         = github_branch_default.main_branch.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 3
  }

    required_status_checks {
    strict   = true
    contexts = ["CI/CD Pipeline", "Linting", "Tests"]
  }
}

# 👥 Assign Teams to Repository
resource "github_team_repository" "maintainers" {
  team_id    = github_team.maintainers.id
  repository = github_repository.repository.name
  permission = "maintain"
}

resource "github_team_repository" "contributors" {
  team_id    = github_team.contributors.id
  repository = github_repository.repository.name
  permission = "push"
}
