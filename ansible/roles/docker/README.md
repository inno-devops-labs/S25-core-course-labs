# Docker Role

This role installs and configures Docker and Docker Compose.

## Requirements

- Ansible 2.9+
- Ubuntu 22.04

## Role Variables

- `docker_version`: The version of Docker to install (default: `latest`).
- `docker_compose_version`: The version of Docker Compose to install (default: `2.32.4`).
- `docker_gpg_key_url`: URL for the Docker GPG key.
- `docker_repo`: Repository for Docker installation.
- `docker_package_name`: The package name of Docker (default: `docker-ce`).

## Example Playbook

```yaml
- hosts: all
  become: yes
  roles:
    - role: docker
```
