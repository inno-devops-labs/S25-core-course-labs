output "vm_id" {
  description = "The ID of the created Yandex Cloud VM instance"
  value       = yandex_compute_instance.vm.id
}

output "vm_name" {
  description = "The name of the VM instance"
  value       = yandex_compute_instance.vm.name
}

output "vm_external_ip" {
  description = "The external IP address of the VM"
  value       = yandex_compute_instance.vm.network_interface[0].nat_ip_address
}

output "vm_internal_ip" {
  description = "The internal IP address of the VM"
  value       = yandex_compute_instance.vm.network_interface[0].ip_address
}

output "vm_status" {
  description = "Current status of the VM instance"
  value       = yandex_compute_instance.vm.status
}
