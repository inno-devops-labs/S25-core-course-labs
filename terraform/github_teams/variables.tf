variable "token" {
  type        = string
  default = "token"
  sensitive   = true
}

variable "github_organization" {
  type        = string
  description = "Organization"
  default     = "tolmachdr-groups"
}