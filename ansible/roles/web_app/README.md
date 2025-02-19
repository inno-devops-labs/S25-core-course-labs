# Web App Role

This role deploys your application's Docker image using Docker Compose.

## Requirements

- Ansible 2.9+
- Docker and Docker Compose (installed/configured by the dependent docker role)
- A compatible host (e.g., Ubuntu 22.04)

## Role Variables

- **docker_image**: The Docker image to deploy (default: `my_web_app:latest`).
- **app_port**: The host port to map to the container’s port 80 (default: `8000`).
- **web_app_full_wipe**: Set to `true` to remove any existing container and configuration before deployment.

## Dependencies

This role depends on the **docker** role.

## Tasks Performed

- Optionally wipes the current deployment.
- Deploys a Docker Compose file.
- Pulls the specified Docker image.
- Starts the application container using Docker Compose.

## Example Playbook

```yaml
- hosts: all
  become: yes
  roles:
    - web_app
