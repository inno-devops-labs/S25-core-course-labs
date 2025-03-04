# Docker Role

This role installs and configures Docker and Docker Compose.

## Requirements

- Ansible 2.17+
- Ubuntu 22.04
- Python3+

## Role Variables

- `docker_version`: The version of Docker to install (default: `latest`).
- `docker_compose_version`: The version of Docker Compose to install (default: `latest`).

## Example Playbook

```yaml
- name: Deploy Docker
  hosts: docker_hosts
  become: yes
  roles:
    - role: docker
```

## Example Inventory

```yaml
[docker_hosts]
51.250.40.65 ansible_user=catorleader ansible_ssh_private_key_file=~/.ssh/id_ed25519
```
