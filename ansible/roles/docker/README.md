# Docker Role

This role installs and configures Docker and Docker Compose on Ubuntu-based systems. It also ensures Docker is set to start on boot and that the current user is added to the Docker group to avoid using `sudo` for Docker commands.

## Requirements

- Ansible 2.9+
- Ubuntu 22.04 (or compatible Ubuntu versions)

## Role Variables

- `docker_version`: The version of Docker to install. Default is `5:27.5.1-1~ubuntu.24.04~noble`.
- `docker_compose_version`: The version of Docker Compose to install. Default is `v2.33.0`.

## Example Playbook

### Example: Using Custom Docker Role

```yaml
- name: Setup Custom Docker Role
  hosts: ya_cloud_vm
  become: true
  roles:
    - "../../roles/docker"
```

## Role Tasks

### The Docker role includes the following tasks:

- Install packages: Installs required packages like apt-transport-https, ca-certificates, curl, and software-properties-common.
- Install Docker: Adds Docker’s GPG key, sets up the repository, and installs the specified version of Docker.
- Install Docker Compose: Downloads the specified version of Docker Compose and places it in /usr/local/bin/docker-compose.
- Configure Docker security settings.
- Enable Docker on boot: Configures the Docker service to start on boot.
- Add user to Docker group: Adds the current user to the Docker group to avoid using sudo for Docker commands.

## How To Use

- 1. Install Ansible
- 2. Clone the [repository](https://github.com/creepydanunity/S25-core-course-labs/tree/lab6) or download the [docker role](https://github.com/creepydanunity/S25-core-course-labs/tree/lab6/ansible/roles/docker) to your Ansible project.
- 3. Update inventory file (`ansible/inventory/default_yacloud_compute.yml`) with the correct hosts.
- 4. Run the playbook:
```bash
ansible-playbook -i ansible/inventory/default_yacloud_compute.yml ansible/playbooks/dev/customRole.yml
```
