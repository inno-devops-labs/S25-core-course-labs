# Docker Role

This role deploys the Web Application using Docker Compose

## Requirements

- Ansible 2.17+
- Ubuntu 22.04
- docker role

## Role Variables

- `web_app_image`: The name of the Docker image for the web application. (default: "milanamilana/python-distroless-web-app:latest")
- `container_name`: The name assigned to the running Docker container. (default: "python_web_app")
- `docker_compose_file`: The filename of the Docker Compose configuration. (default: "docker-compose.yml")
- `web_app_directory`: The directory on the server where the web application will be deployed. (default: "/webapp")
- `internal_app_port`: The port inside the container that the application listens on. (default: 8000)
- `external_app_port`: The port on the host machine mapped to the application's internal port. (default: 8000)
- `web_app_full_wipe`: Whether to remove existing containers and volumes before deployment. (default: true)

## Example Playbook

  ```yaml
- name: Deploy python web app
  hosts: all
  become: yes
  roles:
    - name: web_app
      vars:
        web_app_image: "milanamilana/python-distroless-web-app:latest"
        container_name: "python_web_app"
        docker_compose_file: "docker-compose.yml"

        web_app_directory: "/webapp"

        internal_app_port: 5000
        external_app_port: 80

        web_app_full_wipe: false
