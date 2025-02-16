# Docker Role

  This role installs and configures Docker and Docker Compose.

## Requirements

- Ansible 2.9+
- Ubuntu 22.04

## Role Variables

- `docker_version`: `latest`.
- `docker_package`: `docker-ce`
- `docker_compose_version`: `v2.20.3`

## Example Playbook

```yaml
  - name: Install Docker
    hosts: all
    become: yes
    roles:
    - role: docker
```