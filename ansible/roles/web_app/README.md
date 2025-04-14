# Web Application Role

This role deploys the web application using Docker Compose.

## Requirements

- Ansible 2.17+
- Ubuntu 24.04
- `docker` role

## Role Variables

- `image`: Web App image from Docker Hub (default: `angelika2707/lab2:latest`)
- `container_name`: Web App container name (default: `python-web-app`)
- `docker_compose`: Docker Compose file name (default: `docker-compose.yml`)
- `web_app_dir`: Directory for Docker Compose file (default: `/webapp`)
- `internal_port`: Internal port for Web App (default: `5000`)
- `external_port`: External port for Web App (default: `80`)
- `web_app_full_wipe`: Wipe flag (default: `true`)

## Example Playbook

```yaml
- name: Deploy Python Web Application
  hosts: all
  become: yes
  roles:
    - name: web_app
      vars:
        image: "angelika2707/lab2:latest"
        container_name: "python-web-app"
        docker_compose: "docker-compose.yml"

        web_app_dir: "/webapp"

        internal_port: 5000
        external_port: 80

        web_app_full_wipe: true
```