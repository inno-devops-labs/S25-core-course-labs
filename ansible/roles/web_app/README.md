# Web App Role
This role deploys a Docker-based web application.

## Requirements
- Ansible 2.9+
- Docker installed (via `docker` role)

## Example Playbook
```yaml
- hosts: all
  become: yes
  roles:
    - web_app