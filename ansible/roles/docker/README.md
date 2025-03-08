   # Docker Role

   This role installs and configures Docker and Docker Compose for Ubuntu 24.04 and compatible operating systems with. All tasks described in more detail in the [Tasks](#Tasks) section.

   ## Requirements

   - Ansible 2.9+
   - Ubuntu 24.04 and compatible with sudo privileges
   - Access to the network

   ## Role Variables

   - `docker_version`: The version of Docker to install (default: `latest`).
   - `docker_compose_version`: The version of Docker Compose to install (default: `1.29.2`).
   
   ## Tasks

   - Add GPG key:
      Set up key for Docker's repository.
   - Set up the Docker repository:
      Add Docker's repository to the packet manager's list.
   - Install Docker CE:
      Install Docker Comunity Edition.
   - Install docker-compose:
      Install Docker Compose.
   - Enable Docker service to start on boot:
      Ensble docker.servise to start up on boot usind systemd.
   - Add the current user to the docker group:
      Add user (user) to the docker group to avoid using `sudo` for operations with docker.

   ## Example Playbook

   ```yaml
   - name: Deploy Docker on VM in Yandex Cloud
      hosts: all
      become: true
      roles:
         - docker
   ```