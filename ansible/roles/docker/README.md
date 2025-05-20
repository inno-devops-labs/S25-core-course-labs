# Docker Role

This Ansible role installs and configures the official Docker Engine (docker-ce) and Docker Compose plugin on Ubuntu 22.04+ using the official Docker repository.

## Requirements

- Ansible 2.9+
- Ubuntu 22.04 or later
- Python 3.x

## Role Variables

- No custom variables required for basic usage. All versions are set to latest by default.

## Example Playbook

```yaml
- hosts: webservers
  become: yes
  roles:
    - role: docker
```
