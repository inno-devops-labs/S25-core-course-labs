# `web_app` role

This Ansible role deploys a Flask-based web application in a Docker container. It manages the creation of the application environment, the application directory, the Docker container, and the necessary configurations for the application to run seamlessly in a Docker container.

## Requirements

- Ansible 2.9+ 
- Ubuntu 20.04 or later
- Docker and Docker Compose installed (the role will install Docker if not present)
- Python 3.8+

## Role Variables

### `app_name`
The name of the application, used for the Docker image.

Default: `web_app`

### `app_user`
The name of the system user under which the application will run.

Default: `appuser`

### `app_group`
The name of the system group under which the application will run.

Default: `appgroup`

### `app_port`
The port on which the web application will be exposed.

Default: `5000`

### `app_dir`
The directory where the web application will be deployed inside the container.

Default: `/app`

### `docker_compose_file`
The path to the `docker-compose.yml` file used for the container orchestration.

Default: `{{ app_dir }}/docker-compose.yml`

### `app_src_dir`
The local directory containing the Python Flask web application source code (excluding `venv` directory).

Default: `/home/egor/PycharmProjects/S25-core-course-labs/app_python`

### `web_app_full_wipe`
A flag to determine if the Docker container and all related files should be wiped (set to `true` to wipe, `false` to skip wiping).

Default: `false`

## Dependencies

- The `docker` must be installed and included as a dependency.
- The web application is assumed to be a Flask application using Python.

## Example Playbook

```yaml
- name: Deploy docker on Cloud VM
  hosts: all
  become: true
  vars:
    web_app_full_wipe: true
  roles:
#    - geerlingguy.docker
#    - docker
    - web_app
```
