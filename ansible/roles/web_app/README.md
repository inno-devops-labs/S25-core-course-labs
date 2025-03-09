# Custom Role

This role installs and configures Docker and Docker Compose.

## Requirements

- Ansible 2.9+
- Ubuntu latest

## Variables

`docker_image`: The Docker image to deploy

`app_port`: Port on which to deploy the app

## Example playbook

```yml
- name: Deploy Container
  hosts: all
  become: true
  roles:
      - ../../roles/web_app
```

