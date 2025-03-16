# Web App Role

This role deploys the web application Docker container using a docker-compose file.

## Requirements

- Ansible 2.18
- Docker and Docker Compose installed (via dependency on the `docker` role)

## Role Variables

- `docker_image`: Docker image to deploy (default: "myapp:latest")
- `app_port`: Port mapping for the application (default: 8080)
- `web_app_full_wipe`: Set to true to wipe the existing container and remove files

## Example Playbook

```yaml
- hosts: all
  become: yes
  roles:
    - web_app
