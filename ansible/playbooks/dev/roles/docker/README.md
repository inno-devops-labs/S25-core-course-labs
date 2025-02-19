# Docker Role

This role installs and configures Docker and Docker Compose.

### Requirements

- Ansible 2.9+
- Ubuntu 22.04 or compatible OS

### Role Variables

- `docker_version`: The version of Docker to install (default: `latest`).
- `docker_compose_version`: The version of Docker Compose to install (default: `1.29.2`).

### Docker role Tasks

1. Remove any old Docker GPG keys and sources.
2. Add the official Docker repository.
3. Install Docker and Docker Compose.
4. Configure Docker to start on boot.
5. Add the current user to the Docker group to allow running Docker commands without `sudo`.

### Example Playbook

```yaml
- name: Deploy docker on Cloud VM
  hosts: all
  become: true
  roles:
#    - geerlingguy.docker
    - docker
```