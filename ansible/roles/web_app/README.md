# Web App Role

This role deploys a web application using Docker and Docker Compose.

## Requirements

- Ansible 2.9+

- Ubuntu 22.04+

- Docker and Docker Compose installed

## Role Variables

docker_username: Docker username to pull docker image.

docker_image: Docker image for the web app.

docker_image_tag: Tag of the Docker image (`latest`).

web_app_name: Name of the web application container (`app_python`).

web_app_external_port: External port for accessing the web app.

web_app_internal_port: Internal port inside the container.

web_app_dir: Directory for application data (`~/app_python`).

web_app_full_wipe: Whether to remove all related Docker resources before deployment (default: false).

## Example Playbook

```bash
- hosts: all
  roles:
    - role: web_app
```

## Usage

To run the whole playbook with automated docker installation and dynamic inventory use command:

```bash
ansible-playbook playbooks/dev/main.yaml -i inventory/yacloud_compute.yml
```

To run a specific stage use flag --tags:

```bash
ansible-playbook playbooks/dev/main.yaml -i inventory/yacloud_compute.yml --tags <tag_you_want_to_run>
```

