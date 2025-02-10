# Web App Role

## Requirements

- Ansible 2.9+
- Ubuntu 22.04

## Role Variables

- `app_port`: Host port to map to container port.
- `docker_image`: Docker image to deploy from Docker Hub.
- `container_name`: Container's name.
- `web_app_full_wipe`: Set to true to remove the container and related files.

## Example Playbook

```yaml
- hosts: all
  become: yes
  roles:
    - role: web_app
```

## Deployment Steps

1. Pull Docker Image
The playbook first pulls the specified Docker image from a registry.

The source: pull ensures that the latest version is retrieved.

2. Start the Web App Container
After pulling the image, the playbook starts a new container.

* container_name: Name of the container.
* restart_policy: always: Ensures the container restarts automatically if it stops.
* published_ports: Maps the container's internal port to the host.

3. Create a Directory for docker-compose
To manage the application via docker-compose, a directory is created.

Ensures the /opt/docker/web_app directory exists with correct permissions.
4. Deploy docker-compose File
The playbook then places a docker-compose.yml file from a Jinja2 template.

The template file docker-compose.yml.j2 is rendered and saved to the target location.

5. Wiping the Deployment
If web_app_full_wipe is true, the following tasks run:

5.1. Import Wipe Tasks
Imports additional cleanup tasks if a full wipe is required.

5.2. Remove Existing Web App Container

Stops and removes the container.

7. Remove docker-compose.yml

Deletes the docker-compose configuration.

Tags Usage
* docker: Used for Docker-related tasks.
* deploy: Used for deployment steps.
* wipe: Used for cleanup tasks.