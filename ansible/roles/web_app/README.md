# Web App Role

This role deploys the web application Docker image using Docker Compose.

## Requirements

- Docker and Docker Compose must be installed.
- The `docker` role is a dependency and will be installed automatically.

## Role Variables

- `docker_image`: The Docker image to deploy (default: `jlfkajlkifj/app_python`).
- `app_port`: The port on the host to map to the container's port (default: `"8000"`).
- `compose_file_path`: The path where the docker-compose file is rendered (default: `/opt/web_app/docker-compose.yml`).
- `web_app_full_wipe`: Set to `true` to remove the container and its files (default: `false`).

## Example Playbook

```yaml
- hosts: all
  become: true
  roles:
    - role: web_app
```