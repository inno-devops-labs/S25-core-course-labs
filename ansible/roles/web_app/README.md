   # Web App Role

   This role deploys web application in Docker container. Details of realisation described in next sections.

   ## Requirements

   - Ansible 2.9+
   - Ubuntu 24.04 and compatible with sudo privileges
   - Access to the network

   ## Role Variables

   - `docker_image`: Name of docker image, which will be pulled and deloyed (default: `"voronm1522/devops:python-app"`)
   - `docker_container_name`: Name of the container (default: `"python-app"`)
   - `web_app_full_wipe`: Whether to wipe the space before deploying (default: `true`)

  ## Dependencies

  - `docker`: Deploying application in Docker conteiner depends on installation of the docker on the machine.
  
  ## Tasks

  - `0-wipe.yml`: Executes in case `web_app_full_wipe: true`. It stops the conteiner, remove it and remode its image
  - `main.yml`: It pulls the image from the Docker Hub and deploy it on the machine.

  ## Tags

    - `stop_container`: Stops specified container (ignore errors).
    - `remove_container`: Removes specified container (ignore errors).
    - `remove_image`: Removes specified image.
    - `docker_pull`: Pulls the image from the Docker Hub.
    - `start_container`: Starts the container.

  ## Example Playbook

   ```yaml
  - name: Deploy Docker on VM in Yandex Cloud
    hosts: all
    become: true
    vars:
      ansible_ssh_user: user
      ansible_ssh_private_key_file: /home/VM/.ssh/devops/yandex_cloud_vm
    roles:
      - web_app

  ```
