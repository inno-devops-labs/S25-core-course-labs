# Docker role

Ansible role that installs Docker and Docker Compose.

## Requirements for the hosts

- Ubuntu 22.04 Jammy;
- Python 3.

## Usage

```yaml
- hosts: all
- roles:
    - role: docker
      become: true
```
