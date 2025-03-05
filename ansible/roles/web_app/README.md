# Web App Ansible Role

This role deploys current time by docker

## Requirements

- Docker
- Docker Compose
- Python Docker modules for Ansible

## Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `docker_image` | Docker image to use | `dpttk/iu-devops-lab2:latest` |
| `docker_container_name` | Container name | `moscow_time_app` |
| `app_port` | App port | `5000` |
| `docker_compose_dir` | Docker Compose directory | `/opt/moscow_time` |
| `docker_compose_file` | Docker Compose file path | `"{{ docker_compose_dir }}/docker-compose.yml"` |
| `web_app_full_wipe` | Full wipe option | `false` |

## Dependencies

- docker role

## Example Playbook