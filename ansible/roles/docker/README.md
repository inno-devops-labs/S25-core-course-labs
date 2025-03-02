# Docker Role

This role installs and configures Docker and Docker Compose.

## Requirements

- Ansible 2.9+
- Ubuntu 22.04

## Role Variables

- `docker_compose_version`: The version of Docker Compose to install (default: `v2.32.4`).

## Example Playbook

```yaml
---
- hosts: all
  become: true
  roles:
    - docker
```

## Specifics

- Role can be used as `docker-inside-docker` solution.
