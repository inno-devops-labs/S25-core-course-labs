# APP_PYTHON

output "python_container_id" {
  description = "[APP_PYTHON] IMAGE NAME"
  value       = docker_image.python_app_image.name
}

output "python_image_id" {
  description = "[APP_PYTHON] IMAGE ID"
  value       = docker_image.python_app_image.image_id
}

output "python_container_name" {
  description = "[APP_PYTHON] CONTAINER NAME"
  value       = docker_container.python_app_container.name
}

# APP_JAVA
output "java_container_id" {
  description = "[APP_JAVA] IMAGE NAME"
  value       = docker_image.java_app_image.name
}

output "java_image_id" {
  description = "[APP_JAVA] IMAGE ID"
  value       = docker_image.java_app_image.image_id
}

output "java_container_name" {
  description = "[APP_JAVA] CONTAINER NAME"
  value       = docker_container.java_app_container.name
}
