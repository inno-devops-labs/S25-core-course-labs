# Custom Role

This role installs and configures Docker and Docker Compose.

## Requirements

- Ansible 2.9+
- Ubuntu latest

## Variables

`docker_version`: The version of Docker to install

`docker_compose_version`: The version of Docker Compose to install

## Example playbook

```yml
- name: Deploy Container
  hosts: all
  become: true
  roles:
      - ../../roles/docker
```

