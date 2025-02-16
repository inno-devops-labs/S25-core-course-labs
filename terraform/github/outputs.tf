output "name" {
  value = github_repository.repo.name
}

output "visibility" {
  value = github_repository.repo.visibility
}

output "description" {
  value = github_repository.repo.description
}

output "branch" {
  value = github_branch_default.master.branch
}
