output "time_app_py_container_id" {
  description = "ID of the Docker container of app_python"
  value       = docker_container.time_app_py.id
}

output "time_app_py_container_image" {
  description = "Image of the Docker container of app_python"
  value       = docker_container.time_app_py.image
}

output "time_app_py_container_name" {
  description = "Name of the Docker container of app_python"
  value       = docker_container.time_app_py.name
}
