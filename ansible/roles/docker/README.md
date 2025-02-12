# Docker Role

This role automates the installation and configuration docker and docker compose.

## Requirements for the hosts

- Ubuntu 22.04 Jammy
- Python 3+

## Role Variables

No additional variables are required. The role installs the latest versions of docker and compose by default.

## Usage

```yaml
- hosts: all
- roles:
    - role: docker
      become: true
```
