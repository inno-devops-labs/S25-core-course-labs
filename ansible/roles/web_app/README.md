# Web App Role

   This role deploys web app with Docker Compose.

   ## Requirements

   - Ansible 2.9+
   - Ubuntu 22.04
   - Docker

   ## Role Variables

   - `docker_image_python`: docker image repository
   - `app_python_port`: port for Python app

   ## Usage

   ```yaml
  - name: Deploy app_python
    hosts: all
    become: true
    roles:
        - web_app
    vars:
        web_app_name: app_python
        web_app_internal_port: 5000
        web_app_external_port: 5000
        web_app_full_wipe: true