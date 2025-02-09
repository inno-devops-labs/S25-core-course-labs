# Docker Role

This role installs and configures Docker and Docker Compose.

## Requirements for the hosts

- Ubuntu 22.04 Jammy
- Python 3+

## Role Variables

No variables used. Installing latest versions.

## Usage

```yaml
- hosts: all
- roles:
    - role: docker
      become: true
```