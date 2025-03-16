## Application Deployment Role
Manages Docker-based application lifecycle including deployment, compose configuration, and cleanup operations.

Requirements
------------

- Ansible 2.9+
- Docker installed via the dependent docker role
- Ubuntu 22.04

Role Variables
--------------
- **`docker_image`**: Docker image to use (e.g., from Docker Hub).
- **`container_name`**: Name of the container.
- **`app_port`**: Host port mapped to container port 5000.
- **`web_app_full_wipe`**: Set to `true` to delete the container and its files.

Example Playbook
----------------
```bash
hosts: all
  become: true
  roles:
    - role: web_app
      vars:
        docker_image: "deedjei/lab2"
        container_name: "web_app_python"
        app_port: 5000
        container_port: 5000
```
