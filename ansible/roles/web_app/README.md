# web_app Ansible Role

## Description

This Ansible role deploys a web application container using Docker and Docker Compose. It pulls the Docker image from the specified registry, creates the required network, and deploys the application in a container.

## Requirements

- Docker
- Docker Compose
- Ansible >= 2.9

## Role Variables

- `docker_image`: Docker image for the application (e.g., `petrel312/flask_app:latest`)
- `container_name`: Name of the Docker container (e.g., `flask_app`)
- `host_port`: Port on the host to map to the app port (default: `5000`)
- `app_port`: Port the app will listen on inside the container (default: `5000`)
- `network_name`: Name of the Docker network (default: `web_app_network`)
- `web_app_full_wipe`: Boolean to enable/disable full wipe (default: `false`)

## Dependencies

This role depends on the `docker` role to ensure Docker is installed and configured before deploying the web app.

## Usage

To deploy the web app:

```sh
ansible-playbook ansible/playbooks/dev/main.yaml
```