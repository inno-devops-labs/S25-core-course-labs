# Web App Role

This role deploys a web application using Docker.

## Requirements
- Docker must be installed on the target host.
- The `docker` role is required as a dependency.

## Role Variables
- `web_app_docker_image`: The Docker image to deploy.
- `web_app_container_port`: The port to expose the application on (default: `8080`).

## Playbook
```yaml
- name: Deploy Python app
  hosts: all
  become: true
  roles:
    - role: web_app
      vars:
        web_app_docker_image: "netpo4ki/python-web"
        web_app_docker_image_tag: "latest"
        web_app_container_name: python_web
        web_app_container_port: 5000
        web_app_port: 8081