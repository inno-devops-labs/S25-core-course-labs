resource "github_branch_protection" "default_branch" {
  repository_id = github_repository.s25_core_course_labs.node_id
  pattern       = var.default_branch

  required_status_checks {
    strict   = true
    contexts = ["ci/build", "ci/test"]
  }

  enforce_admins = true

  required_pull_request_reviews {
    required_approving_review_count = 1
    dismiss_stale_reviews           = true
  }

}
