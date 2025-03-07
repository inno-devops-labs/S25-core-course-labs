# Docker Role

This role installs and configures Docker and Docker Compose.

## Requirements

- **Ansible** 2.9+
- **Supported OS**: Ubuntu 22.04+

## Role Variables

- `compose_version`: The version of Docker-compose to install.
- `ansible_user`: Username in VM.

## Example Playbook

The playbook for role

```yaml
  - name: Install Docker
    hosts: all
    become: true
    roles:
      - docker
```
