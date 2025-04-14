# Docker role

This role set ups Docker and Docker-compose on debian-based distro.

## Requirements

- Ansible 2.9+
- Ubuntu 22.04

## Variables

- `docker_users`: List of users (by default, current user who runs the ansible), to add to `docker` group
- `docker_packages`: List of packages needed to set up Docker itself. Recommended to leave defaults.

## Example Playbook

```yaml
- hosts: all
   roles:
      - role: docker
```
