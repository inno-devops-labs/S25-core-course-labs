output "container_id" {
  description = "Python app Container ID"
  value = docker_container.my_container.id
}
