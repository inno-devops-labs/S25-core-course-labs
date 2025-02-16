# Docker Role

This Ansible role automates the **installation and configuration of Docker and Docker Compose** on a cloud VM.  
It is designed for **Lab 5 of the Ansible course**, ensuring Docker is correctly set up for **containerized application deployment**.

## Purpose

This role:

- Installs and configures Docker Engine and Docker Compose.
- Ensures Docker starts on boot.
- Adds the executing user to the `docker` group to allow non-root execution.
- Copies a `daemon.json` configuration if defined.
- Deploys the necessary components to support **a web application**.

## Requirements

- Ansible 2.9+
- Ubuntu 22.04

## Role Variables

The following variables are configurable in `defaults/main.yml`:

- `docker_version`: Specifies which Docker version to install (default: `latest`).
- `docker_compose_version`: Specifies which Docker Compose version to install (default: `v2.12.2`).
- `docker_daemon_options`: JSON configuration for the Docker daemon (if any).
- `docker_service_enabled`: Ensures Docker starts on boot (default: `true`).

## Tasks

This role performs the following actions:

1. Installs Docker dependencies (`ca-certificates`, `curl`, `gnupg`).
2. Adds the Docker GPG key and official repository.
3. Installs `docker.io` and `docker-compose-plugin`.
4. Enables and starts the Docker service.
5. Adds the user to the `docker` group (to allow non-root execution).
6. Deploys a `daemon.json` configuration file if needed.
7. Ensures Docker Compose is installed.

## Example Playbook

Below is a full example playbook that:

- Installs Docker using this role.
- Ensures Docker starts on boot.
- Deploys a web application using `docker-compose.yml`.

```yaml
- name: Deploy Docker and Web Application
  hosts: all
  become: true
  vars:
    docker_version: latest
    docker_compose_version: v2.12.2
  roles:
    - role: docker

- name: Deploy Web Application
  hosts: all
  become: true
  roles:
    - role: web_app
  vars:
    docker_image: nginx:latest
    app_port: 8080
```

## Usage Instructions

To use this role, ensure you have included it in your Ansible playbook and executed:

```sh
ansible-playbook -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/main.yaml
```

## Verification

After running the playbook, validate that Docker and Docker Compose are installed:

```sh
docker --version
docker compose version
```

Also, check that the service is running:

```sh
systemctl status docker
```

## Troubleshooting

- **If Docker is not installed** → Re-run the playbook.
- **If Docker Compose is missing** → Check the `install_compose.yml` task file.
- **If user permission issues occur** → Ensure the user is added to the `docker` group:

  ```sh
  sudo usermod -aG docker $USER
  ```
