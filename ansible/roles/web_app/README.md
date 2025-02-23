# web_app Role

This role deploys a web application using Docker and docker-compose.

## Requirements

- Docker and docker-compose must be installed on the target host.
- The `docker` role is required as a dependency.

## Role Variables

- **docker_image**: Docker image to deploy (default: `myregistry/myapp:latest`).
- **app_port**: Port on which the application will be accessible (default: `8080`).
- **web_app_full_wipe**: Set to `true` to remove existing containers and files before redeployment.

## Dependencies

- `docker` role

## Example Playbook

```yaml
- hosts: all
  become: yes
  roles:
    - docker
    - web_app
