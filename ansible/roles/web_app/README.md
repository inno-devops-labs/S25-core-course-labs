# Docker role

Ansible role that installs simple dockerized web apps.

## Variables

| Variable Name          | Description                                                                                           | Example                |
|------------------------|-------------------------------------------------------------------------------------------------------|------------------------|
| web_app_name           | The name of the web application.                                                                      | "web_app"              |
| web_app_dir            | The directory where the web application is installed, using the value of web_app_name.               | "/opt/{{ web_app_name }}/ " |
| docker_registry       | The Docker registry where the web application image is hosted.                                         | "docker.io"            |
| docker_username       | The username for accessing the Docker registry.                                                        | "elonmaxx"              |
| web_app_full_wipe     | Determines whether a full wipe of the web application is required.                                     | false                  |
| web_app_image         | The full name of the web application image, including the registry, username, and application name.  | "{{ docker_registry }}/{{ docker_username }}/{{ web_app_name }}" |
| web_app_image_tag     | The tag for the web application image.                                                                 | "latest"               |
| web_app_internal_port | The internal port on which the web application operates within the container.                          | 80                     |
| web_app_external_port | The external port on which the web application is accessible outside the container.                    | 8080                   |

This table provides a clear and organized documentation for each variable, including their descriptions and examples.

## Requirements for the hosts

- Ubuntu 22.04 Jammy;
- Python 3.
- My local docker role.

## Usage

```yaml
---
- name: Deploy my_web_app
  hosts: all
  become: true
  roles:
    - web_app
  vars:
    web_app_name: my_web_app
    web_app_internal_port: 8080
    web_app_external_port: 8080
    web_app_full_wipe: true
```
