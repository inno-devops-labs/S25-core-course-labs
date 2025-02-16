# Docker Role

## Requirements

- Ansible version 2.9

## Role Variables

- `docker_edition`: Specifies the Docker edition to be installed ('ce' for Community Edition or 'ee' for Enterprise
  Edition).
- `docker_packages`: Array of Docker packages to be installed.
- `docker_service_manage`: Determines whether to manage the Docker service (default: `true`).
- `docker_service_state`: Sets the desired state of the Docker service (default: `started`).
- `docker_service_enabled`: Specifies whether the Docker service should start on boot (default: `true`).
- `docker_restart_handler_state`: Defines the state of the restart handler for the Docker service (
  default: `restarted`).
- `docker_install_compose_plugin`: Decides whether to install the Docker Compose plugin (default: `true`).
- `docker_compose_package`: Indicates the name of the Docker Compose package to be installed.
- `docker_compose_package_state`: Sets the desired state of the Docker Compose package (default: `present`).
- `docker_install_compose`: Determines whether to install Docker Compose (default: `false`).
- `docker_compose_version`: Specifies the version of Docker Compose to install.
- `docker_compose_arch`: Specifies the architecture of the system (default: `{{ ansible_architecture }}`).
- `docker_compose_url`: Specifies the URL to download Docker Compose from.
- `docker_compose_path`: Defines the path where Docker Compose should be installed.