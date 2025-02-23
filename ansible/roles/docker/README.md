   # Docker Role

   This role installs and configures Docker and Docker Compose.

   ## Requirements

   - Ansible 2.9+
   - Ubuntu 22.04

   ## Role Variables

   - **`docker_users`**:  
  Specifies the users who will have access to Docker. Defaults to the Ansible user running the playbook.

- **`docker_package_state`**:  
  Defines whether Docker should be installed (`present`) or removed (`absent`). Default is `present`.

- **`docker_ubuntu_release`**:  
  Specifies the Ubuntu release codename (e.g., `jammy` for Ubuntu 22.04).

- **`docker_gpg_key_url`**:  
  URL to Docker's GPG key for verifying package authenticity.

- **`docker_repo`**:  
  Docker repository configuration for Ubuntu.

- **`docker_package_name`**:  
  Name of the Docker package to install (`docker-ce`).

- **`docker_version`**:  
  Version of Docker to install. Default is `latest`.

- **`docker_compose_version`**:  
  Version of Docker Compose to install (e.g., `v2.32.4`).

- **`docker_compose_url`**:  
  URL to download Docker Compose, dynamically generated based on the system and architecture.
 # Playbook

 ```yaml
 - name: Deploy Docker on Yandex Cloud VM
   hosts: all
   become: yes
   roles:
    - docker
 ```