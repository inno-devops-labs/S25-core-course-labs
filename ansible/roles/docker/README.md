
# Docker Role

This role installs and configures Docker and Docker Compose.

## Requirements

- Ansible 2.17+ 
- Ubuntu 22.04

## Role Variables

- `docker_version`: The version of Docker to install (default: `latest`).
- `docker_compose_version`: The version of Docker Compose to install (default: `latest`).

## Playbook

```yaml
    ---
    - name: Prepare docker
    hosts: localhost
    connection: local
    roles:
        - docker