# Web Application Deployment Role

This Ansible role deploys a web application using Docker and Docker Compose.

## Requirements

- Ansible 2.9+
- Docker must be installed on the target machine (handled via the `docker` role)
- Supported OS: Ubuntu 22.04 / Debian-based distributions

## Role Variables

You can configure the role using the following variables:

| Variable             | Default Value     | Description |
|----------------------|------------------|-------------|
| `docker_image`      | `"myapp:latest"`  | The Docker image to deploy. |
| `app_port`          | `8080`            | The port to expose the application. |
| `web_app_full_wipe` | `false`           | If `true`, removes the existing container and all related files before deployment. |

## Dependencies

This role depends on the `docker` role to ensure Docker is installed and configured.

## Example Playbook

```yaml
- hosts: all
  roles:
    - role: docker
    - role: web_app
      vars:
        docker_image: "g1l1a/my-django-app"
        app_port: 8080
