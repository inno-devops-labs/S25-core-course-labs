# web_app Role

This role deploys a web application using Docker and Docker Compose.

## Requirements

- Ansible 2.9+
- Ubuntu 22.04
- Docker installed (this is handled by a dependency on the Docker role)

## Role Variables
- `docker_image`: The name of the Docker image to pull and deploy.
- `app_port`: The port on the host machine to map to the container.
- `web_app_full_wipe`: If set to true, this will remove the existing Docker container and image before deploying (default: false).

## Role Dependencies

This role depends on the following role to ensure Docker is installed and configured:

- `docker`: Installs Docker and Docker Compose.

## Tasks Overview

1. Wipe Logic:
   - If web_app_full_wipe is set to true, the previous Docker container and image will be removed.
   - This cleanup process is done in the `0-wipe.yml` file.

2. Fetch Latest Docker Image:
   - Pulls the latest version of the Docker image defined by the `docker_image` variable.

3. Generate Docker Compose Configuration:
   - A Jinja2 template is used to generate the `docker-compose.yml` configuration file based on the `docker_image` and `app_port` variables.

4. Launch Application Container:
   - Starts the application container using `docker-compose`.

## Example Playbook

```yml
- name: Install Docker on VМ
  hosts: all
  become: yes
  roles:
    - docker
    - web_app
```