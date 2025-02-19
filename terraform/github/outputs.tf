output "repo_name" {
  value = github_repository.my_repo.name
}

output "repo_branch" {
  value = github_branch_default.main.branch
}

output "repo_id" {
  value = github_repository.my_repo.id
}