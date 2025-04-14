# Docker Role

This role installs and configures Docker and Docker Compose on Ubuntu systems.

## Requirements

- Ansible 2.9+
- Ubuntu 22.04

## Role Variables

- `docker_packages`: List of Docker packages to install
- `docker_users`: List of users to add to the Docker group

## Example Playbook

```yaml
- hosts: all
  roles:
    - role: docker
```