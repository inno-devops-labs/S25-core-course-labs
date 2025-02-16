# Web App Role

This Ansible role deploys a web application using Docker and Docker Compose. It pulls a specified Docker image, configures deployment via a Jinja2-based Docker Compose template, and ensures the application is running on the target system.

## Requirements

- Ansible 2.9+
- Ubuntu 22.04 (or compatible Linux distributions)
- Docker and Docker Compose (are being installed via the `docker` role dependency)

## Role Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `docker_image` | The Docker image to deploy. | `iucd/fastapi-mt` |
| `image_tag` | The image tag to use. | `distroless` |
| `container_name` | The name of the deployed container. | `web_app_container` |
| `app_port` | The port on which the application runs. | `8080` |
| `web_app_full_wipe` | Whether to remove the existing container and image before deployment. | `false` |

## Example Playbook

```yaml
- name: Deploy Web Application
  hosts: all
  become: yes
  roles:
    - ../../../roles/web_app
```

## Role Tasks

### The Web App role includes the following tasks:

- **Pull Docker Image**: Ensures the specified Docker image is pulled.
- **Copy Compose Template**: Generates and places the `docker-compose.yml` file in the target user’s home directory.
- **Deploy Via Compose**: Uses Docker Compose to start the application in detached mode.
- **Container Removal (Optional)**: If `web_app_full_wipe` is enabled, stops and removes the container and image before redeploying.

## How To Use

1. Install Ansible.
2. Ensure the `docker` role ([link](https://github.com/creepydanunity/S25-core-course-labs/tree/lab6/ansible/roles/docker)) is available in your project.
3. Clone or download the `web_app` [role](https://github.com/creepydanunity/S25-core-course-labs/tree/lab6/ansible/roles/web_app) into your Ansible project.
4. Update the inventory file with the correct target hosts.
5. Run the playbook:

```bash
ansible-playbook -i ansible/inventory/default_yacloud_compute.yml ansible/playbooks/dev/app_python/main.yml
```

