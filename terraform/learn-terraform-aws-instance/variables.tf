variable "access_key" {
  description = "Value of the access key"
  type        = string
  sensitive   = true
}

variable "secret_access_key" {
  description = "Value of the secret_access_key"
  type        = string
  sensitive   = true
}

variable "session_token" {
  description = "Value of the session_token"
  type        = string
  sensitive   = true
}
