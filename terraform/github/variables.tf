variable "github_token" {
  type        = string
  description = "GitHub personal access token for authentication"
}

variable "repo_name" {
  type    = string
  default = "S25-core-course-labs"
}

variable "repo_description" {
  type    = string
  default = "A GitHub repository managed with Terraform"
}

variable "repo_visibility" {
  type    = string
  default = "public"  
}

