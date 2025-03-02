# Web App Role

## Description

This role deploys a Docker-based web application using Ansible.

## Requirements

- Docker must be installed (Handled via role dependency)
- Ansible 2.9+ required

## Variables

| Variable | Default Value | Description |
|----------|-------------|-------------|
| `docker_image` | `matveyplat/flask--app` | Docker image to pull |
| `container_name` | `web_app` | Name of the container |
| `container_port` | `5000` | Port inside the container |
| `host_port` | `5000` | Port exposed on the host |
| `web_app_full_wipe` | `false` | Set to `true` to wipe the container |

## Usage

```sh
ansible-playbook -i inventory/default_yandex.yml playbooks/dev/main.yaml
