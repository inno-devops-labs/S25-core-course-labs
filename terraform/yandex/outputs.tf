output "external_ip_address" {
  description = "Public IP address of the instance"
  value       = yandex_compute_instance.app.network_interface[0].nat_ip_address
}

output "internal_ip_address" {
  description = "Private IP address of the instance"
  value       = yandex_compute_instance.app.network_interface[0].ip_address
}

output "instance_fqdn" {
  description = "Fully Qualified Domain Name of the instance"
  value       = yandex_compute_instance.app.fqdn
}

output "app_url" {
  description = "URL to access the application"
  value       = "http://${yandex_compute_instance.app.network_interface[0].nat_ip_address}:${var.app_port}"
}

output "instance_status" {
  description = "Current status of the instance"
  value       = yandex_compute_instance.app.status
}

resource "local_file" "ansible_inventory" {
  content = templatefile("inventory.tmpl",
    {
      vm-python-app-address = yandex_compute_instance.app.network_interface[0].nat_ip_address
    }
  )
  filename = "../../ansible/inventory/yandex.yaml"
}
