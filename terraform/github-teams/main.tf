
resource "github_team" "justcgh9" {
  name        = "OP team"
  description = "the best team there is"
  privacy     = "closed"
}

resource "github_team" "others" {
  name        = "just guys"
  description = "average team"
  privacy     = "closed"
}

resource "github_repository" "repo" {
  name             = "bonus-repo"
  description      = ""
  visibility       = "public"
  has_issues       = true
  has_wiki         = true
  auto_init        = true
  license_template = "mit"
}

resource "github_branch_default" "repo_main" {
  repository = github_repository.repo.name
  branch     = "main"
}

resource "github_branch_protection" "repo_protection" {
  repository_id                   = github_repository.repo.id
  pattern                         = github_branch_default.repo_main.branch
  require_conversation_resolution = true
  enforce_admins                  = true

  required_pull_request_reviews {
    required_approving_review_count = 1
  }
}

resource "github_team_repository" "justcgh9_repo" {
  team_id    = github_team.justcgh9.id
  repository = github_repository.repo.name
  permission = "push"
}

resource "github_team_repository" "others_repo" {
  team_id    = github_team.others.id
  repository = github_repository.repo.name
  permission = "maintain"
}