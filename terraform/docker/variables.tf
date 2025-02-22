# APP_PYTHON

variable "python_app_context" {
  description = "[APP_PYTHON] CONTEXT"
  type        = string
  default     = "../app_python"
}

variable "java_app_context" {
  description = "[APP_JAVA] CONTEXT"
  type        = string
  default     = "../app_java"
}

variable "python_container_name" {
  description = "[PYTHON APP] CONTAINER NAME"
  type        = string
  default     = "python-watch"
}

# APP_JAVA

variable "python_app_image_name" {
  description = "[PYTHON APP] DOCKER IMAGE"
  type        = string
  default     = "python_app:latest"
}

variable "java_app_image_name" {
  description = "[JAVA APP] DOCKER IMAGE"
  type        = string
  default     = "java_app:latest"
}

variable "java_container_name" {
  description = "[JAVA APP] CONTAINER NAME"
  type        = string
  default     = "vacation-calculator"
}