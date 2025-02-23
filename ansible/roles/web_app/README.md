# Role Name

Deploys a python web application using Docker

## Requirements

- `Ansible 2.9+`
- `community.docker`

## Role Variables

| Parameter                | Description                                           | Value                               |
| ------------------------ | ----------------------------------------------------- | ----------------------------------- |
| `web_app_image`          | Defines the Docker image used for the web application | `yoqub/app_python`                  |
| `web_app_image_tag`      | Specifies the tag of the web application image        | `latest`                            |
| `web_app_container_name` | Name of the Docker container running the application  | `app_python`                        |
| `web_app_ports`          | Port mapping between host and container               | `8080:5000`                         |
| `web_app_restart_policy` | Restart policy for the application container          | `unless-stopped`                    |
| `web_app_full_wipe`      | Determines whether to remove the app and its data     | `false`                             |
| `app_install_dir`        | Directory where the application is installed          | `/opt/{{ web_app_container_name }}` |

## Dependencies

- `docker` role to install Docker

## Example Playbook

```yaml
- name: Install and Configure Docker, Run the Web App
  hosts: all
  become: true
  roles:
    - web_app
```

Wipe deployment:

```yaml
- name: Install and Configure Docker, Run the Web App
  hosts: all
  become: true
  roles:
    - role: web_app
  vars:
    web_app_full_wipe: true
  tags: wipe
```

## License

MIT-0
