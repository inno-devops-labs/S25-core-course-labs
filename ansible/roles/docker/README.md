# Docker Role

This role installs, configures and secures Docker and Docker Compose on target machines. It provides a robust, production-ready Docker environment with security best practices enabled by default.

---

## Requirements

- **Ansible**: 2.9+
- **Operating System**: Ubuntu 22.04 (or other Debian-based distributions)
- **Python**: 3.x
- **Memory**: Minimum 2GB RAM recommended
- **Storage**: At least 20GB available disk space

---

## Role Variables

The following variables can be customized in `defaults/main.yml`:

### Docker Installation

- `docker_edition`: Docker edition to install (`ce` or `ee`). Default: `ce`.
- `docker_packages`: List of Docker packages to install. Default:

  ```yaml
  docker_packages:
    - "docker-{{ docker_edition }}"
    - "docker-{{ docker_edition }}-cli"
    - "docker-{{ docker_edition }}-rootless-extras"
    - "containerd.io"
    - docker-buildx-plugin
  ```

- `docker_packages_state`: Package state (`latest` or specific version). Default: `latest`.
- `docker_obsolete_packages`: Legacy packages to remove. Default:

  ```yaml
  docker_obsolete_packages:
    - docker
    - docker.io
    - docker-engine
    - docker-doc
    - podman-docker
    - containerd
    - runc
  ```

### Docker Service Configuration

- `docker_service_manage`: Enable service management. Default: `true`.
- `docker_service_state`: Service state (`started`/`stopped`). Default: `started`.
- `docker_service_enabled`: Start on boot. Default: `true`.
- `docker_restart_handler_state`: Handler trigger state. Default: `restarted`.

### Docker Compose Plugin

- `docker_install_compose_plugin`: Install Compose plugin. Default: `true`.
- `docker_compose_package`: Package name. Default: `docker-compose-plugin`.
- `docker_compose_package_state`: Package state. Default: `latest`.

### Repository Management

- `docker_add_repo`: Add Docker repository. Default: `true`.
- `docker_repo_url`: Repository URL. Default: `https://download.docker.com/linux`.
- `docker_apt_ansible_distribution`: Distribution name. Default: `ubuntu`.
- `docker_apt_release_channel`: Release channel. Default: `stable`.
- `docker_apt_arch`: Architecture. Default: `amd64`.
- `docker_apt_repository`: Repository configuration. Default:

  ```yaml
  docker_apt_repository: "deb [arch={{ docker_apt_arch }}{{' signed-by=/etc/apt/keyrings/docker.asc' if add_repository_key is not failed}}] {{ docker_repo_url }}/{{ ansible_distribution | lower }} {{ ansible_distribution_release }} {{ docker_apt_release_channel }}"
  ```

- `docker_apt_ignore_key_error`: Ignore key errors. Default: `true`.
- `docker_apt_gpg_key`: GPG key URL. Default: `{{ docker_repo_url }}/{{ ansible_distribution | lower }}/gpg`.

### User Management

- `docker_users`: Users to add to docker group. Default: `["ubuntu"]`.

---

## Role Tasks

The role executes these tasks in sequence:

1. **Repository Setup**
   - Removes legacy Docker packages
   - Configures official Docker repository
   - Imports GPG keys

2. **Docker Installation**
   - Installs core Docker packages
   - Configures service parameters

3. **Docker Compose Setup**
   - Installs Docker Compose plugin
   - Verifies installation

4. **Service Configuration**
   - Enables and starts Docker daemon
   - Configures systemd integration

5. **User Access Management**
   - Creates docker group
   - Adds specified users

6. **Security Hardening**
   - Implements security best practices
   - Configures daemon.json

## Task Organization

The role's tasks are modularly organized:

- `main.yml`: Primary task orchestrator
- `setup_debian.yml`: Repository management
- `install_docker.yml`: Core installation
- `install_compose.yml`: Compose plugin setup
- `secure_docker.yml`: Security configuration
- `docker_users.yml`: Access control
