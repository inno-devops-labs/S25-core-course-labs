# Web App Role

This role Deploys a docker image

## Requirements

- Ansible 2.17.8
- Ubuntu 22.04
- Docker 27.5.1

## Role Variables

- **`docker_image_name`**: The name of the image we're pulling to deploy.
- **`docker_container_name`**: The name of the container we're deploying.
- **`container_port`**: The port we are deploying the container on.
- **`web_app_full_wipe`**: A boolean value used to stop and delete the container.
- **`dest_file`**: The path of the docker compose file we are delivering to the targeted machines.

## Tasks

The Role has 2 tasks:

- `main.yml`:
  - Pulls the of the app from DockerHub.
  - Run a docker container of our app.
  - Deliver a docker compose file of our image to the targeted machine.
  - Calls for `0-wipe.yml` if `web_app_full_wipe` is `true`.

- `0-wipe.yml`:
  - Stops the container running on the targeted machine.
  - Remove the container form the targeted machine.

## Playbook

### Overview

The Ansible playbook applies the Docker role to the aws hosts, ensuring Docker and Docker Compose are installed and configured correctly.

### Playbook Structure

```yaml
- hosts: aws # Targets all hosts under the aws group (from the inventory file).
  become: true # Runs tasks with sudo privileges.
  roles:
    - roles/web_app # Calls the wep-app role from the roles/web_app directory.
```
