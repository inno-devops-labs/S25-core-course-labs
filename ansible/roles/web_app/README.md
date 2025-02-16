# Web App Role

This Ansible role is used for deploying and managing a web application using Docker.

## Requirements

- Ansible 2.10 or higher
- Target hosts should be Debian-based or RedHat-based systems.
- Ubuntu 18.04 or later
- Python 3.6 or later
- `pip3` installed
- Docker and docker-compose installed on target host

## Role Variables

- `docker_image`: Name of the Docker image for the web application.
- `docker_image_tag`: Tag of the Docker image.
- `docker_container_name`: Name of the Docker container for the web application.
- `docker_container_port`: Port inside the Docker container where the web application is listening.
- `docker_host_port`: Port on the host machine where the Docker container's port is mapped to.

## Dependencies

This role depends on the `docker` role.

### Usage

```yaml
- hosts: all
  roles:
    - role: docker
      become: true

    - role: web_app
      become: true

  vars:
    ansible_ssh_private_key_file: "~/.ssh/id_ed25519"
```
