## Docker Role

### Description

This Ansible role installs Docker on target hosts. It also installs Docker Compose and manages Docker-related configurations.

### Requirements

- Ansible 2.10 or higher
- Target hosts should be Debian-based or RedHat-based systems.

### Role Variables

- `docker_edition`: Specifies the Docker edition to install ('ce' for Community Edition or 'ee' for Enterprise Edition).
- `docker_packages`: List of Docker packages to install.
- `docker_service_manage`: Whether to manage the Docker service (default: `true`).
- `docker_service_state`: Desired state of the Docker service (default: `started`).
- `docker_service_enabled`: Whether the Docker service should start on boot (default: `true`).
- `docker_restart_handler_state`: State of the restart handler for Docker service (default: `restarted`).
- `docker_install_compose_plugin`: Whether to install Docker Compose plugin (default: `true`).
- `docker_compose_package`: Name of the Docker Compose package to install.
- `docker_compose_package_state`: Desired state of the Docker Compose package (default: `present`).
- `docker_install_compose`: Whether to install Docker Compose (default: `false`).
- `docker_compose_version`: Version of Docker Compose to install.
- `docker_compose_arch`: Architecture of the system (default: `{{ ansible_architecture }}`).
- `docker_compose_url`: URL to download Docker Compose from.
- `docker_compose_path`: Path where Docker Compose should be installed.

### Example Playbook

```yaml
- hosts: all
  roles:
    - role: docker
      become: true

  vars:
    ansible_ssh_private_key_file: "~/.ssh/id_ed25519"
```
