# Docker role

Ansible role that installs `docker` with `docker-compose`, pull application image, and setup services for it.

## Tags

| Tag                    | Description                  |
|------------------------|------------------------------|
| wipe                   | Wipes all application's artifacts: stops services and deletes `web_app_dir` with configs             |
| deploy                 | Only pulls and (re-)starts of application service using `docker-compose` with defined paraments      |

## Variables

| Variable Name         | Description                                                                                           | Example                |
|-----------------------|-------------------------------------------------------------------------------------------------------|------------------------|
| web_app_name          | The name of the web application (also is docker image name).                                          | "app_python"              |
| web_app_dir           | The directory where the web application is installed, using the value of `web_app_name`.              | "/opt/{{ web_app_name }}" |
| docker_registry       | The Docker registry where the web application image is hosted.                                        | "docker.io"            |
| docker_username       | The username for accessing the Docker registry.                                                       | "raleksan"              |
| docker_image_tag      | The tag for the web application image.                                                                | "v0.1"               |
| docker_image          | The full name of the web application image, including the registry, username, and application name.   | "{{ docker_registry }}/{{ docker_username }}/{{ web_app_name }}:{{ docker_image_tag }}" |
| app_internal_port     | The internal port on which the web application operates within the container.                         | 8000                   |
| app_external_port     | The external port on which the web application is accessible outside the container.                   | 8000                   |
| web_app_full_wipe     | Determines whether a full wipe of the web application is required.                                    | False                  |

This table provides a clear and organized documentation for each variable, including their descriptions and examples.

## Requirements for the hosts

- Ubuntu 22.04
- Python 3.12
- Self-made docker role (available locally only).

## Usage

```yaml
---
- name: Deploy app_python
  hosts: all
  become: yes
  roles:
    - web_app
  vars:
    web_app_name: "app_python"
    app_internal_port: 8000
    app_external_port: 8000
    web_app_full_wipe: False

```

```yaml
---
- name: Deploy app_rust
  hosts: all
  become: yes
  roles:
    - web_app
  vars:
    web_app_name: "app_rust_distroless"
    app_internal_port: 8001
    app_external_port: 8000
    web_app_full_wipe: False

```
