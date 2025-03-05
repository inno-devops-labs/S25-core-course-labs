# Docker Role

This custom role installs and configures Docker and Docker Compose for Ubuntu 22.04 systems.
It ensures that Docker is properly installed with all necessary dependencies,
Docker Compose is downloaded and verified,
the Docker service is enabled to start on boot,
and the current user is added to the docker group for passwordless usage.

## Requirements

- **Ansible:** Version 2.9 or later.
- **Python:** Version 3.8 or later.
- **Operating System:** Ubuntu 22.04 (or compatible) with sudo privileges.
- **Network:** Access to Docker repositories and GPG key servers.

## Role Variables

- `docker_version`: The version of Docker to install (default: `latest`).
- `docker_compose_version`: The version of Docker Compose to install (default: `1.29.2`).

## Role Tasks

The role performs the following key tasks:

- **Install Docker Dependencies:**  
  Installs required packages such as `apt-transport-https`, `ca-certificates`, `curl`, `gnupg`, and `lsb-release`

- **Add Docker's Official GPG Key and Repository:**  
  Imports the Docker GPG key into `/etc/apt/keyrings/docker.asc` and configures
  the Docker repository with the `signed-by` option to avoid conflicts

- **Install Docker CE:**  
  Installs the Docker Comunity Edition from the configured repository.

- **Install Docker Compose:**  
  Downloads the Docker Compose binary for AMD64 system architecture (default on Yandex Cloud VMs),
  sets the executable permission, and verifies the installation.

- **Enable Docker on Boot:**  
  Configures the Docker systemd service to start automaticaly on boot

- **Add User to Docker Group:**  
  Adds the current user to the `docker` group, allowing the execution of Docker commands without sudo

## Example Playbook

```yaml
- hosts: all
  become: yes
  roles:
    - role: docker
