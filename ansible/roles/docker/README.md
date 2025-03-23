# Docker Role

This role installs and configures Docker and Docker Compose on Debian systems.

## Requirements

- Ansible 2.12+
- Debian 9+

## Role Variables

- `docker_users`: The users to add to the Docker group (default: the current Ansible remote user).
- `docker_on_boot`: Whether to enable systemctl service to start Docker on boot (default: `true`).

## Example Playbook

```yaml
- hosts: all
    roles:
    - role: docker
      become: true
```

## Installing Python Docker Module

For the Ansible's docker_images and other related modules to work, you need to install the `docker` package using pip. This role provides you with the option to install the package using the `install_docker_pip` variable (disabled by default).

```yaml
- hosts: all
    roles:
    - role: docker
      install_docker_pip: true
```

Under the hood, the role uses the `python3-pip` package to install the `docker` pip package.
