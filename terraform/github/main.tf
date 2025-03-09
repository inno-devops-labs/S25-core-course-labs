resource "github_repository" "repo" {
  name        = var.repo_name
  description = var.repo_description
  visibility  = var.repo_visibility
  auto_init   = true

  archive_on_destroy = false

  lifecycle {
    ignore_changes = [vulnerability_alerts]
  }
}


resource "github_branch_default" "default" {
  repository = github_repository.repo.name
  branch     = "master"  # Updated to "master"
}


resource "github_team" "developers" {
  name        = "Developers"
  description = "Team for developers with push access"
  privacy     = "closed"
}

resource "github_team" "admins" {
  name        = "Admins"
  description = "Team for admins with full control"
  privacy     = "closed"
}

resource "github_team_membership" "dev_member" {
  team_id  = github_team.developers.id
  username = "MoeJaafar"  
  role     = "member"
}

resource "github_team_membership" "admin_member" {
  team_id  = github_team.admins.id
  username = "MoeJaafar" 
  role     = "maintainer"
}

resource "github_team_repository" "developers_repo_access" {
  team_id    = github_team.developers.id
  repository = github_repository.repo.name
  permission = "push"  # Developers can push code
}

resource "github_team_repository" "admins_repo_access" {
  team_id    = github_team.admins.id
  repository = github_repository.repo.name
  permission = "admin"  # Admins have full control
}
