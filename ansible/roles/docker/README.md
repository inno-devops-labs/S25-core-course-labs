# Docker Role

This role installs and configures Docker and Docker Compose plugin.

## Requirements

- Ansible 2.9+
- Ubuntu 22.04

## Role Variables

- `docker_version`: The version of Docker to install (default unspecified which is latest).
- `docker_compose_version`: The version of Docker Compose plugin to install (default: `>=2.32.4`).

## Example Playbook

```yaml
- hosts: all
  become: yes
  roles:
    - docker
```
