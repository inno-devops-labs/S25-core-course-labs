# Docker Role

This role installs and configures Docker and Docker Compose.

## Requirements

- Ansible 2.9+
- Ubuntu 22.04 (or a compatible version)

## Role Variables

- `docker_version`: The version of Docker to install (default: `latest`).
- `docker_compose_version`: The version of Docker Compose to install (default: `1.29.2`).

## Tasks Performed

- Installs prerequisite packages.
- Adds Docker’s official GPG key and repository.
- Installs Docker Engine and Docker Compose.
- Ensures Docker is started and enabled on boot.
- Adds the current user to the docker group to allow non-sudo usage of Docker commands.

## Example Playbook

```yaml
- hosts: all
  roles:
    - role: docker
