# Docker Role

This role installs and configures Docker and Docker Compose.

## Requirements

- Ansible 2.17.8
- Ubuntu 22.04

## Role Variables

### Package Management

- **`docker_packages`**: List of Docker packages to install.
- **`docker_obsolete_packages`**: List of old/obsolete Docker packages to remove.

### Installation & Repository Management

- **`docker_add_repo`**: Whether to enable Docker repository setup (`true` by default).
- **`docker_repo_url`**: Base URL for Docker repositories.
- **`docker_apt_repository`**: The full APT repository URL used for installation.

### Service Configuration

- **`docker_service_manage`**: Whether Ansible should manage the Docker service.  
- **`docker_service_enabled`**: Whether to enable Docker to start on boot.  

### Docker Compose

- **`docker_install_compose_plugin`**: Whether to install the Docker Compose plugin (`true` by default).
- **`docker_install_compose`**: Whether to install Docker Compose separately.(`false` by default)
- **`docker_compose_version`**: The version of Docker Compose to install (version `v2.32.1`).
- **`docker_compose_url`**: The URL to download the Docker Compose binary from.
- **`docker_compose_path`**: The installation path for the Docker Compose binary.

### User & Permissions

- **`docker_users`**: List of users to be added to the `docker` group for permission to run Docker commands without `sudo` (empty by default).

### Daemon Configuration

- **`docker_daemon_options`**: Dictionary of additional Docker daemon configuration settings.

## Tasks

The Role has three tasks:

- `main.yml`:
  - Sets up the environment and prepares it by downloading all the required packages to install docker and docker compose.
  - Calls `install_docker.yml`.
  - Adds the currend user to the docker group to avoid using `sudo` for docker commands.

- `install_docker.yml`:
  - Installs docker on the instance we are running it on making sure to delete any different versions.
  - Calls for `install_compose.yml`.
  - Ensures that docker is enabled on boot.

- `install_compose.yml`: Installs docker compose making sure to delete any different versions.

## Playbook

### Overview

The Ansible playbook applies the Docker role to the aws hosts, ensuring Docker and Docker Compose are installed and configured correctly.

### Playbook Structure

```yaml
- hosts: aws # Targets all hosts under the aws group (from the inventory file).
  become: true # Runs tasks with sudo privileges.
  roles:
    - roles/docker # Calls the docker role from the roles/docker directory.
```
