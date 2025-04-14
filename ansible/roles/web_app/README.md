# Web App Role

This role enables pulling the Docker image of a Web App and deploying it using Ansible.
It also provides an option to fully wipe the deployment using the wipe tag and web_app_full_wipe=true.

## Requirements

- Ansible 2.9+
- Ubuntu 22.04 (other distributions may require adjustments)

## Role Variables

- `web_app_docker_image` Name of webapp image to use
- `web_app_docker_image_tag` Docker image tag to use
- `web_app_container_name` Name of the deployed container
- `web_app_container_port` Port on which the application runs in container
- `web_app_port` Port on which the application opened on VM in Yandex Cloud
- `web_app_full_wipe` Enables removal of generated container and Docker Compose file

## Role Tasks

- Pull the Docker image.

- Start the container.

- Deploy the Docker Compose file.

- Optionally, remove the container and Docker Compose file when web_app_full_wipe=true.

## Example Playbook

```yaml
- name: Deploying Python Moscow Time App
  hosts: all
  become: true
  roles:
    - role: web_app
      vars:
        web_app_docker_image: "vladis7love/app_python"
        web_app_docker_image_tag: "latest"
        web_app_container_port: 5000
        web_app_port: 5000
        web_app_container_name: python_webapp
```
