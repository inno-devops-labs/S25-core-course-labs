# Docker Role

This role installs and configures Docker and Docker Compose on a target machine. It ensures Docker is installed, configured to start on boot, and adds the specified users to the `docker` group to avoid using `sudo` for Docker commands. Additionally, it secures Docker by configuring the `daemon.json` file with security settings.

---

## Requirements

- **Ansible**: 2.9+
- **Operating System**: Ubuntu 22.04 (or other Debian-based distributions)
- **Python**: 3.x

---

## Role Variables

The following variables are defined in `defaults/main.yml` and can be customized:

### Docker Installation

- `docker_edition`: The edition of Docker to install (`ce` for Community Edition or `ee` for Enterprise Edition). Default: `ce`.
- `docker_packages`: List of Docker packages to install. Default:

  ```yaml
  docker_packages:
    - "docker-{{ docker_edition }}"
    - "docker-{{ docker_edition }}-cli"
    - "docker-{{ docker_edition }}-rootless-extras"
    - "containerd.io"
    - docker-buildx-plugin
  ```

- `docker_packages_state`: The state of the Docker packages (`latest` or a specific version). Default: `latest`.
- `docker_obsolete_packages`: List of obsolete Docker packages to remove. Default:

  ```yaml
  docker_obsolete_packages:
    - docker
    - docker.io
    - docker-engine
    - docker-doc
    - podman-docker
    - containerd
    - runc
  ```

### Docker Service

- `docker_service_manage`: Whether to manage the Docker service. Default: `true`.
- `docker_service_state`: The state of the Docker service (`started` or `stopped`). Default: `started`.
- `docker_service_enabled`: Whether to enable Docker to start on boot. Default: `true`.
- `docker_restart_handler_state`: The state of the Docker service when handlers are triggered. Default: `restarted`.

### Docker Compose

- `docker_install_compose_plugin`: Whether to install the Docker Compose plugin. Default: `true`.
- `docker_compose_package`: The name of the Docker Compose package. Default: `docker-compose-plugin`.
- `docker_compose_package_state`: The state of the Docker Compose package (`latest` or a specific version). Default: `latest`.

### Repository Configuration

- `docker_add_repo`: Whether to add the Docker repository. Default: `true`.
- `docker_repo_url`: The URL of the Docker repository. Default: `https://download.docker.com/linux`.
- `docker_apt_ansible_distribution`: The distribution name for the Docker repository. Default: `ubuntu`.
- `docker_apt_release_channel`: The release channel for the Docker repository. Default: `stable`.
- `docker_apt_arch`: The architecture for the Docker repository. Default: `amd64`.
- `docker_apt_repository`: The repository string for the Docker repository. Default:

  ```yaml
  docker_apt_repository: "deb [arch={{ docker_apt_arch }}{{' signed-by=/etc/apt/keyrings/docker.asc' if add_repository_key is not failed}}] {{ docker_repo_url }}/{{ ansible_distribution | lower }} {{ ansible_distribution_release }} {{ docker_apt_release_channel }}"
  ```

- `docker_apt_ignore_key_error`: Whether to ignore errors when adding the Docker repository key. Default: `true`.
- `docker_apt_gpg_key`: The GPG key URL for the Docker repository. Default: `{{ docker_repo_url }}/{{ ansible_distribution | lower }}/gpg`.

### User Configuration

- `docker_users`: A list of users to add to the `docker` group. Default: `["ubuntu"]`.

---

## Tasks

The role performs the following tasks:

1. **Setup Repository**:
   - Removes old Docker packages and repositories.
   - Adds the Docker repository and GPG key.

2. **Install Docker**:
   - Installs Docker and its dependencies.

3. **Install Docker Compose**:
   - Installs the Docker Compose plugin.

4. **Configure Docker Service**:
   - Ensures Docker is started and enabled on boot.

5. **Add Users to Docker Group**:
   - Adds the specified users to the `docker` group.

6. **Secure Docker Configuration**:
   - Configures Docker with secure settings by modifying the `daemon.json` file.

---

## Example Playbook

To use this role in a playbook, include it as follows:

```yaml
---
- name: Ansible and Docker Deployment
  hosts: aws_ec2  # Target hosts from the AWS EC2 inventory
  become: true  # Use elevated privileges for all tasks
  roles:
    - roles/docker  # Include the custom Docker role
```

### Inventory File (`inventory/default_aws_ec2.yml`)

The inventory file uses the `aws_ec2` plugin to dynamically fetch EC2 instances:

```yaml
---
plugin: aws_ec2
regions:
  - us-east-1
filters:
  tag:Name: Ansible VM  # Filter instances by the tag "Name: Ansible VM"
  instance-state-name: running  # Only include running instances
```

---

## Handlers

The role includes the following handlers:

- **Restart Docker**: Restarts the Docker service when triggered (e.g., after installing Docker packages or modifying `daemon.json`).

---

## Secure Docker Configuration

The role includes a task to secure Docker by modifying the `daemon.json` file. The following security settings are applied:

- **User Namespace Remapping**: Enabled to prevent containers from running as root.
- **Inter-Container Communication (ICC)**: Disabled to reduce the attack surface.
- **Userland Proxy**: Disabled for better performance and security.
- **No New Privileges**: Enabled to prevent containers from gaining new privileges during runtime.

### Example `daemon.json`

```json
{
  "userns-remap": "default",
  "icc": false,
  "userland-proxy": false,
  "no-new-privileges": true
}
```
