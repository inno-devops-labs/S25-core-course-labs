output "VM_ip" {
  description = "public IP address"
  value       = yandex_compute_instance.virtual-machine.network_interface.0.ip_address
}

output "instance_ssh_key" {
  description = "SSH key"
  value       = yandex_compute_instance.virtual-machine.metadata["ssh-keys"]
}