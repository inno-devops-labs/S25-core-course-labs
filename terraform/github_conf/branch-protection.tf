resource "github_branch_protection" "master" {
  repository_id = github_repository.core-course-labs.id
  pattern       = "master"

  allows_deletions = false

  required_pull_request_reviews {
    dismiss_stale_reviews = true
    require_code_owner_reviews = true
    required_approving_review_count = 1
  }

  required_status_checks {
    contexts = ["ci/circleci"]
  }

  enforce_admins = true
}