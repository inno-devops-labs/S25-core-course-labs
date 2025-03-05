# Web App Role

This custom role pulls the application's Docker image and configures the container.
The role also deploys custom docker-compose config and provides wipe tasks, which can be run
separately with `wipe` tag or enabled by default with `web_app_full_wipe=true`.

## Requirements

- Ansible 2.9+
- Docker installed via the dependent `docker` role
- Ubuntu 22.04

## Role Variables

- `docker_image`: Docker image to deploy from Docker Hub (I use `nshlyakhtin/devops:lab2-amd64` python web app from
  lab2).
- `container_name`: Name for the container.
- `app_port`: Host port to map to container port 5000.
- `web_app_full_wipe`: Set to true to remove the container and related files.

## Tasks

- **Deploy Web App:** Pulls the image and starts the container.
- **Docker Compose:** Generates a docker-compose.yml from a Jinja2 template.
- **Wipe Logic:** Removes the container and docker-compose file when enabled.

## Example Playbook

```yaml
- hosts: all
  become: yes
  roles:
    - role: web_app
