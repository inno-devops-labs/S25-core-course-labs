# Docker Role with Ansible

This Ansible role installs and configures Docker and Docker Compose on a target machine, such as an AWS EC2 instance running Ubuntu.

---

## Requirements

- Ansible version: 2.17.8 or newer
- Target OS: Ubuntu 22.04

---

## Role Variables

### Package Handling

- `docker_packages`: Packages required for Docker installation.
- `docker_obsolete_packages`: Outdated Docker packages to be removed.

### Repository Configuration

- `docker_add_repo`: Toggle to add Docker APT repository (default: `true`)
- `docker_repo_url`: Base Docker repository source.
- `docker_apt_repository`: Full APT repository line.

### Docker Service Management

- `docker_service_manage`: Whether to control the Docker service via Ansible.
- `docker_service_enabled`: Whether Docker should start on boot.

### Docker Compose Settings

- `docker_install_compose_plugin`: Toggle to install Compose plugin (default: `true`)
- `docker_install_compose`: Install Compose binary directly (default: `false`)
- `docker_compose_version`: Docker Compose version (e.g., `v2.32.1`)
- `docker_compose_url`: URL to fetch the Docker Compose binary.
- `docker_compose_path`: Target path to place the Docker Compose binary.

### User Access

- `docker_users`: List of users to be granted non-root Docker access.

### Daemon Options

- `docker_daemon_options`: Additional key-value pairs to modify Docker daemon settings.

---

## Tasks Included in the Role

- `main.yml`
  - Orchestrates setup
  - Runs Docker install task
  - Adds user to Docker group

- `install_docker.yml`
  - Installs Docker after removing conflicting versions
  - Ensures Docker service is enabled
  - Triggers Compose installation

- `install_compose.yml`
  - Installs Docker Compose if enabled
  - Removes conflicting Compose binaries

---

## Playbook

```yaml
- name: Deploy Docker
  hosts: aws # Targets all hosts under the aws group (from the inventory file).
  become: true # Runs tasks with sudo privileges.
  roles:
    - roles/docker # Calls the docker role from the roles/docker directory.
```

This playbook assigns the `docker` role to AWS EC2 instance, ensuring Docker and Compose are fully installed and configured.

---