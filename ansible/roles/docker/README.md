# Docker Role

This role installs and configures Docker and Docker Compose.

## Requirements

- Python 3+
- Ubuntu 22.04

## Role Variables
I did not use any variables since I used the latest version.

## Playbook

```yaml
- hosts: all
- roles:
    - role: docker
      become: true