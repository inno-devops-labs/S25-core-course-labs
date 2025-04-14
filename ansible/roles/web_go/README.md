# Web App Role

This role manages the lifecycle of a web application running inside a Docker container. It is designed to handle the deployment, cleanup, and full wipe of the web application's environment.

---

## Requirements

- **Ansible**: 2.17.8 or higher
- **Operating System**: Ubuntu 22.04
- **Docker**: Installed and running on the target machine

---

## Role Variables

The following variables are defined in `defaults/main.yml` and can be customized:

### Web App Container

- `docker_image_name`: The name of the Docker image associated with the web application. Default: `"saleemasekrea/app_go"`.
- `docker_image_tag`: The tag for the Docker image. Default: `"latest"`.
- `docker_container_name`: The name of the Docker container running the web application. Default: `"app_go"`.
- `app_port`: The published ports for the Docker container. Default: `"8002:8002"`.

### Web App Full Wipe

- `web_app_full_wipe`: Toggle to enable or disable full wipe logic (removing containers, images, and volumes). Default: `true`.

### Docker Compose Configuration

- `docker_compose_src`: The path to the Docker Compose template file. Default: `"templates/docker-compose.yml.j2"`.
- `docker_compose_dest`: The destination path where the Docker Compose file will be created. Default: `"./docker-compose.yml"`.

---

## Tasks

### Main Task File (`tasks/main.yml`)

The main task file contains the logic for deploying  the web app container .

1. **Deploy Web App Container**:
   - Pull the Docker image from DockerHub using the `community.docker.docker_image` module.
   - Create and start the container with the specified image, ports, and volumes using the `community.docker.docker_container` module.

2. **Deliver Docker Compose File**:
   - Use the `ansible.builtin.template` module to generate a `docker-compose.yml` file from the provided template (`templates/docker-compose.yml.j2`).

3. **Execute Wipe Logic**:
   - If the `web_app_full_wipe` variable is set to `true`, the role includes the `0-wipe.yml` task file, which handles the cleanup and removal of containers, images, and volumes.

### Wipe Task File (`tasks/0-wipe.yml`)

The `0-wipe.yml` task file contains the cleanup logic for removing the web app container, its image, and related volumes.

1. **Stop and Remove Web App Container**:
   - Stops and removes the container using the `community.docker.docker_container` module.

2. **Remove Docker Image**:
   - Removes the Docker image from the system using the `community.docker.docker_image` module.

3. **Remove Docker Volumes**:
   - Deletes the Docker volumes associated with the container using the `ansible.builtin.file` module.

## Docker Compose Template (`templates/docker-compose.yml.j2`)

The `docker-compose.yml.j2` template defines how the Docker Compose file will be generated.