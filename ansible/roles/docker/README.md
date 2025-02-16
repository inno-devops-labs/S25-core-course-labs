# Docker Role

   This role installs and configures Docker and Docker Compose.

   ## Requirements

   - Ansible 2.9+
   - Ubuntu 22.04
   - Privileges : The playbook must be run with elevated privileges (become: true) to install system-level packages.

   ## Role Variables

   - `docker_version`: The version of Docker to install (default: `latest`).
   - `docker_compose_version`: The version of Docker Compose to install (default: `1.29.2`).

   ## Example Playbook

   ```yaml
   - name: Install and configure Docker
  hosts: all
  become: true
  roles:
    - role: docker
      vars:
        docker_version: "latest"
        docker_compose_version: "1.29.2"
