resource "github_repository" "repo" {
  name           = S25-core-course-labs
  visibility     = var.repo_visibility
  default_branch = var.default_branch
}

# Apply branch protection for the default branch
resource "github_branch_protection" "default" {
  repository_id  = github_repository.repo.node_id
  pattern        = var.default_branch
  enforce_admins = true

  required_status_checks {
    strict   = true
    contexts = ["continuous-integration/terraform"]
  }
}
