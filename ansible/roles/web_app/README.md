# Docker Role

This role installs and configures Docker and Docker Compose.

## Requirements

- Ansible 2.9+
- Ubuntu 22.04

## Role Variables

- `web_app_dir`: The main app directory  (default: `/app`)
- `docker_image`: The application docker image (default: `innoenjoyer/moscow-time-app:latest`)
- `docker_container`: The application docker container name (default: `moscow-time-app`)
- `docker_compose_filename`: The docker compose filename (default: `docker-compose.yml`)
- `internal_port`: The application internal port (default: `5000`)
- `external_port`: The application external port (default: `5000`)
- `web_app_full_wipe`: Whether to perform wipe (default: `true`)
- 
## Example Playbook

```yaml
- name: Simple Python Web App
  hosts: all
  become: yes
  roles:
    - name: web_app
      vars:
        web_app_dir: "/app"
        docker_image: "innoenjoyer/moscow-time-app:latest"
        docker_container: "moscow-time-app"
        docker_compose_filename: "docker-compose.yml"
        internal_port: 5000
        external_port: 5000
        web_app_full_wipe: true
```