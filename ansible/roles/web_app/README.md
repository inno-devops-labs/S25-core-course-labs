# Web App Ansible Role

This Ansible role automates the deployment of an application using Docker and Docker Compose. It pulls the specified
Docker image, runs it as a container, and sets up Docker Compose configuration. Additionally, it provides tasks to clean
up by removing the container and Docker Compose file if needed.

## Requirements

**Target Hosts Requirements:**

- **Operating System**: Ubuntu 22.04 Jammy +
- **Python**: Python 3.6+ installed on target hosts

**Note:** If Docker is not installed on the target hosts, there is included a Docker installation role before applying
this role.

## Role Variables

### Application Deployment Variables

- `app_image_name` *(string, required)*:
  - **Description**: The name of the Docker image for the web application.
  - **Default**: `"your_docker_image_name"`

- `app_image_tag` *(string, optional)*:
  - **Description**: The tag/version of the Docker image.
  - **Default**: `"latest"`

- `app_container_name` *(string, optional)*:
  - **Description**: The name to assign to the running Docker container.
  - **Default**: `"web_app_container"`

- `container_port` *(integer, optional)*:
  - **Description**: The port on which the application inside the container listens.
  - **Default**: `80`

- `host_port` *(integer, optional)*:
  - **Description**: The port on the host to map to the container's port.
  - **Default**: `8080`

### Docker Compose Variables

- `compose_config_dir` *(string, optional)*:
  - **Description**: Directory on the host where the `docker-compose.yml` will be placed.
  - **Default**: `"/opt/webapp"`

- `compose_template_src` *(string, optional)*:
  - **Description**: Path to the `docker-compose.yml.j2` template file.
  - **Default**: `"docker-compose.yml.j2"`

- `compose_owner` *(string, optional)*:
  - **Description**: Owner of the Docker Compose configuration directory.
  - **Default**: `"root"`

- `compose_group` *(string, optional)*:
  - **Description**: Group of the Docker Compose configuration directory.
  - **Default**: `"root"`

- `compose_permissions` *(string, optional)*:
  - **Description**: Permissions for the Docker Compose configuration directory.
  - **Default**: `"0755"`

### Cleanup Variables

- `web_app_full_wipe` *(boolean, optional)*:
  - **Description**: Set to `true` to remove the Docker container and Docker Compose file.
  - **Default**: `false`

## Usage

Include the `web_app` role in your playbook to deploy the web application.

### Example Playbook

```yaml
---
- name: Deploy Python app
  hosts: docker_hosts
  become: true
  roles:
    - role: web_app
      vars:
        app_image_name: "catorleader/python-watch"
        app_image_tag: "distroless"
        app_container_name: "python-watch"
        container_port: "5000"
        host_port: "5000"
        app_full_wipe: true
```
