# Docker role
Ansible role that installs simple dockerized web apps.
## Variables
| Variable Name          | Description                                                                                                     | Example                                                          |
|------------------------|-----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| web_app_name           | Specifies the name of the web application                                                                       | "web_app"                                                        |
| web_app_dir            | Defines the installation directory for the web application, incorporating the web_app_name in the path          | "/opt/{{ web_app_name }}/"                                         |
| docker_registry        | Identifies the Docker registry hosting the application image                                                    | "docker.io"                                                      |
| docker_username        | Provides the username for accessing the Docker registry                                                         | "mihdenis85"                                                     |
| web_app_full_wipe      | Indicates whether a full wipe of the web application is needed                                                  | false                                                            |
| web_app_image          | Represents the complete image name, constructed from the registry, username, and application name                | "{{ docker_registry }}/{{ docker_username }}/{{ web_app_name }}"    |
| web_app_image_tag      | Specifies the tag of the web application image                                                                   | "latest"                                                         |
| web_app_internal_port  | The port on which the web application runs inside the container                                                  | 80                                                               |
| web_app_external_port  | The port through which the web application is accessible from outside the container                              | 8080                                                             |

## Requirements for hosts
- Ubuntu 22.04 Jammy;
- Python 3.
- Local docker role.
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
