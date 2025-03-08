# Docker Role

This role installs and configures Docker and Docker Compose.

## Requirements

- Ansible 2.18+
- Ubuntu 24.04

## Role Variables

- `docker_compose_version`: The version of Docker Compose to install (default: `v2.32.1`).

## Example Playbook

```yaml
- name: Install and Configure Docker
  hosts: all
  become: true
  roles:
    - docker
```
