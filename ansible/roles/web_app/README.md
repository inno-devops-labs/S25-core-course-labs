# Web App Role

This role deploys the web application using Docker Compose.

## Requirements

- Ansible 2.17+
- Ubuntu 24.04
- `docker` role

## Role Variables

- `docker_image`: The Docker image for the web application from Docker Hub (default: `wellnotwell/lab2:latest`)
- `docker_container`: Name of the web application container (default: `python-web-app`)
- `docker_compose_file`: The Docker Compose file to use (default: `docker-compose.yml`)
- `web_app_dir`: Directory where the Docker Compose file will be placed (default: `/webapp`)
- `internal_port`: Internal port of the web application (default: `5000`)
- `external_port`: External port to expose the application (default: `80`)
- `web_app_full_wipe`: Whether to perform a full wipe of the web application (default: `true`)

## Example Playbook

```yaml
- name: Deploy Python Web App
  hosts: all
  become: yes
  roles:
    - name: web_app
      vars:
        docker_image: "wellnotwell/lab2:latest"
        docker_container: "python-web-app"
        docker_compose_filename: "docker-compose.yml"

        web_app_dir: "/webapp"

        internal_port: 5000
        external_port: 80

        web_app_full_wipe: true
```