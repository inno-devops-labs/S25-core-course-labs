# Docker Role

Docker and Docker Compose installation via Ansible role.

## Requirements

- Ansible 2.9+

## Playbook Instance

```yaml
- hosts: all

  roles:
    - roles/docker	
```