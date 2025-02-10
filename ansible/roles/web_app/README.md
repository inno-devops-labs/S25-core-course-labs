# Web Application Role

This role deploys the web application using Docker Compose.

## Requirements

- Ansible 2.17+
- Ubuntu 24.04
- `docker` role

## Role Variables

- `docker_image`: Web application image to use from Docker Hub (default: `magicwinnie/simple-python-web-app-distroless:latest`)
- `docker_container`: Web application container name (default: `python-web-app`)
- `docker_compose_filename`: Docker Compose file name to use (default: `docker-compose.yml`)
- `web_app_dir`: Where to put Docker Compose file (default: `/webapp`)
- `internal_port`: Web application internal port (default: `8000`)
- `external_port`: External port to use (default: `80`)
- `web_app_full_wipe`: Whether to perform wipe (default: `true`)

## Example Playbook

```yaml
- name: Deploy Python Web Application
  hosts: all
  become: yes
  roles:
    - name: web_app
      vars:
        docker_image: "magicwinnie/simple-python-web-app-distroless:latest"
        docker_container: "python-web-app"
        docker_compose_filename: "docker-compose.yml"

        web_app_dir: "/webapp"

        internal_port: 8000
        external_port: 80

        web_app_full_wipe: true
```
