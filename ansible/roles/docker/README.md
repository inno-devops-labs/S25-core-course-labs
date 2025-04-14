# Docker Role

   This role installs and configures Docker and Docker Compose.

## Requirements

- Ansible 2.9+
- Ubuntu 22.04

## Example Playbook

   ```yaml
   - name: Deploy Docker
     hosts: all
     become: true
     roles:
      - docker
      - web_app
```
