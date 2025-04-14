variable "token" {
  description = "Github token"
  type        = string
  sensitive   = true
}

variable "repository_name" {
  description = "Repository name"
  type        = string
  default     = "Terraform-test-teams"
}

variable "repository_description" {
  description = "Description of repository"
  type        = string
  default     = "DevOps lab4 bonus task | Minnemullin Nail"
}

variable "visibility" {
  description = "Repository visibility"
  type        = string
  default     = "public"
}

variable "default_branch" {
  description = "Default branch "
  type        = string
  default     = "main"
}

variable "organization_name" {
  description = "Organiztion name"
  type        = string
  default     = "DevOps2025-n-minnemullin"
}