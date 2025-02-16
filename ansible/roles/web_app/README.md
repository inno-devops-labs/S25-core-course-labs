# Web App Role

   This Ansible role automates the deployment of a Dockerized web application using best practices. It includes tasks for setting up the Docker environment, deploying the application via a docker-compose.yml file, and managing lifecycle operations such as wiping the environment.

   ## Requirements

   - Ansible 2.9+
   - Ubuntu 22.04
   - Dependencies :
      - The docker role must be installed and configured before using this role.
      - Docker and Docker Compose must be installed on the target system.

   ## Role Variables

   - docker_image: Specifies the Docker image to deploy. Default value is nginx:latest.
   - app_port: Specifies the host port to map to the container's port 80. Default value is 8080.
   - web_app_full_wipe: Enables or disables the full wipe logic. Default value is false.

   ## Example Playbook

   ```yaml
  - name: Deploy Web Application
  hosts: all
  become: yes
  roles:
    - role: web_app
      vars:
        docker_image: "my-app:latest"
        app_port: "8080"
        web_app_full_wipe: false
