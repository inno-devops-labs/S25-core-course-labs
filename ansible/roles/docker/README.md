# Docker Role

This role installs and configures Docker and Docker Compose.

## Requirements

- Ansible 2.17.7
- Ubuntu 24.04

## Role Variables

- `docker_version`: latest
- `docker_compose_version`: v2.33.0

## Example Playbook

```yaml
- hosts: all
  roles:
     - docker
```
