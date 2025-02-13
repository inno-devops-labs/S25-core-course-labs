   # Docker Role

   This role installs and configures Docker and Docker Compose.

   ## Requirements

   - Ansible 2.9+
   - Ubuntu 22.04
   - Python 3

   ## Role Variables

   - `docker_version`: The version of Docker to install (default: `latest`).
   - `docker_compose_version`: The version of Docker Compose to install (default: `latest`).

   ## Example Playbook

   ```yaml
   - name: Install Docker on VM
     hosts: all
     become: true
     roles:
        - docker