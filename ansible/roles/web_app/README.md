# Web Application Deployment Role

This Ansible role is designed to automate the deployment of a Dockerized web application. It ensures the required container is pulled and executed, and optionally cleans up previous containers if requested.

---

## Prerequisites

- Ansible 2.17.8 or later
- Ubuntu 22.04
- Docker version 27.5.1

---

## Configurable Variables

- `docker_image_name`: Docker image to pull and deploy
- `docker_container_name`: Name to assign to the Docker container
- `container_port`: Port to expose for the web application
- `web_app_full_wipe`: Boolean flag to trigger full reset of the container (default: false)
- `dest_file`: Destination path where the Docker Compose file will be placed on the host

---

## Tasks Included

### `main.yml`

- Retrieves the Docker image from DockerHub
- Launches the container with specified settings
- Copies a pre-defined Docker Compose file to the server
- Executes `0-wipe.yml` if `web_app_full_wipe` is set to `true`

### `0-wipe.yml`

- Stops any running container with the defined name
- Deletes the container to ensure a fresh deployment

---

## Playbook

```yaml
  hosts: aws
  become: true
  roles:
    - roles/web_app
```

This playbook applies the `web_app` role to EC2 instances in the `aws` inventory group, enabling consistent and automated web app deployments using Docker.

---