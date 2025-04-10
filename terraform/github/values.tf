variable "token" {
  description = "GitHub Personal Access Token"
  type        = string
  sensitive   = true
}

variable "repo_name" {
  description = "Repository name"
  type        = string
  default     = "SoftArch9"
}

variable "repo_visibility" {
  description = "Repository visibility"
  type        = string
  default     = "public"
}
