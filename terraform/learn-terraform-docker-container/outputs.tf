output "container_id" {
  description = "081384876dbcc90b1f4c09fe41b18c1569064c4ff7b790b718dab2366816885e"
  value       = docker_container.nginx.id
}

output "image_id" {
  description = "sha256:9bea9f2796e236cb18c2b3ad561ff29f655d1001f9ec7247a0bc5e08d25652a1nginx:latest"
  value       = docker_image.nginx.id
}
