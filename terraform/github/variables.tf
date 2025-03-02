variable "token" {
  type        = string
  description = "GitHub PAT token"
  sensitive   = true
}
variable "git_repo_name" {
    type = string
    default = "S25-core-course-lab4-TF"
}

variable "git_repo_description" {
    type = string
    default = "Lab 4 repository, which is connected to the Terraform config."
}

variable "git_repo_visibility" {
    type = string
    default = "public"
}

variable "git_license" {
    type = string
    default = "mit"
}

variable "git_repo_default_branch" {
    type = string
    default = "master"
}

variable "git_existing_repo_name" {
    type = string
    default = "S25-core-course-labs"
}

variable "git_existing_repo_description" {
    type = string
    default = "This description was changed by the Terraform config."
}