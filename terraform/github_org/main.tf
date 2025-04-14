resource "github_repository" "repo" {
  name        = var.repository_name
  description = var.repository_description
  visibility  = var.visibility
  auto_init   = var.auto_init
}

resource "github_branch_default" "master" {
  repository = var.repository_name
  branch     = var.default_branch
  depends_on = [github_repository.repo]
}

resource "github_branch_protection" "repo" {
  repository_id = github_repository.repo.id
  pattern       = var.default_branch

  required_status_checks {
    strict   = true
    contexts = []
  }

  required_pull_request_reviews {
    dismiss_stale_reviews      = true
    require_code_owner_reviews = true
  }

  enforce_admins = true
  depends_on     = [github_branch_default.master]
}

resource "github_team" "teams" {
  count = length(var.teams)

  name        = var.teams[count.index].name
  description = var.teams[count.index].description
}

resource "github_team_repository" "team_repo" {
  count = length(var.teams)

  team_id    = github_team.teams[count.index].id
  repository = github_repository.repo.name
  permission = var.teams[count.index].permission
  depends_on = [github_repository.repo, github_team.teams]
}
