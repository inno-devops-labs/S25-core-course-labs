# Docker Role

This role deploys application in Docker container using docker compose

## Requirements

- Ansible 2.18+
- Ubuntu 24.04 LTS
- docker role (`../docker/`)

## Variables

| Variable Name          | Description                                                                                           | Example                |
|------------------------|-------------------------------------------------------------------------------------------------------|------------------------|
| web_app_name           | The name of the web application.                                                                      | "web_app"              |
| web_app_dir            | The directory where the web application is installed, using the value of web_app_name.               | "/opt/{{ web_app_name }}/ " |
| web_app_docker_registry       | The Docker registry where the web application image is hosted.                                         | "docker.io"            |
| web_app_docker_username       | The username for accessing the Docker registry.                                                        | "ebob"              |
| web_app_full_wipe     | Determines whether a full wipe of the web application is required.                                     | false                  |
| web_app_image         | The full name of the web application image, including the registry, username, and application name.  | "{{ web_app_docker_registry }}/{{ web_app_docker_username }}/{{ web_app_name }}" |
| web_app_image_tag     | The tag for the web application image.                                                                 | "latest"               |
| web_app_internal_port | The internal port on which the web application operates within the container.                          | 80                     |
| web_app_external_port | The external port on which the web application is accessible outside the container.                    | 8080                   |

This table provides a clear and organized documentation for each variable, including their descriptions and examples.

## Tags

We support tags for wipe only and deploy only, just add them at the end of `ansible-playbook` command:

```bash
--tags=wipe

--tags=deploy
```

## Usage

```yaml
- name: Deploy web_app
  hosts: all
  become: true
  roles:
    - web_app
  vars:
    web_app_name: web_app
    web_app_internal_port: 8080
    web_app_external_port: 8080
    web_app_full_wipe: true
```
