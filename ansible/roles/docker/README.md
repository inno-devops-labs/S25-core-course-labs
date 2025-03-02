   # Docker Role

   This role installs and configures Docker and Docker Compose.

   ## Requirements

   - Ansible 2.12.0
   - Ubuntu 22.04

   ## Role Variables

   - `docker_version`: The version of Docker to install (default: `latest`).
   - `docker_compose_version`: The version of Docker Compose to install (default: `1.29.2`).
   - `docker_distro`: Ubuntu distribution for Docker installation (default: `"focal"`).
   - `docker_user`: User to add to the Docker group (default: current user `ansible_user`).

   ## Example Playbook

   ```yaml
  all:
  hosts:
    yc_instance:
      ansible_host: 51.250.19.210
      ansible_user: ubuntu
      ansible_ssh_private_key_file: ~/.ssh/id_rsa