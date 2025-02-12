# Docker Role

This role installs and configures Docker and Docker Compose.

## Requirements

- Ansible 2.9+
- Ubuntu 22.04

## Role Variables

No variables used.

Needed versions:
- docker version: latest.
- docker-compose version`: 1.29.2.

## Playbook

```yaml
- hosts: all
  become: yes
  roles:
    - role: docker
```
