resource "github_branch_protection" "default_branch_protection" {
  repository_id = github_repository.core_course_labs.id 
  pattern       = var.default_branch

  enforce_admins                = true
  require_conversation_resolution = true
  require_signed_commits        = false  


  required_pull_request_reviews {
    dismiss_stale_reviews           = true
    require_code_owner_reviews      = false  
    required_approving_review_count = 1
  }
}
