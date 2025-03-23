# Docker Role

This role installs and configures Docker and Docker Compose.

## Requirements

- Ansible 2.17+
- Ubuntu 24.04
- Python3+

## Role Variables

- `docker_version`: The version of Docker to install (default: `latest`).
- `docker_compose_version`: The version of Docker Compose to install (default: `latest`).

## Example Playbook

```yaml
- name: Install and Configure Docker
  hosts: all
  become: yes
  roles:
    - role: docker
```

