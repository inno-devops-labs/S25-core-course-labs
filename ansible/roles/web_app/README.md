# Web App Role

This role automates the deployment of a web application using Docker and Docker Compose.

## Requirements

- Ansible 2.9+
- Ubuntu 22.04
- Docker and Docker Compose installed

## Role Variables

| Variable              | Default Value                   |
|----------------------|---------------------------------|
| `docker_image`      | `mirgasimovk/python-msk:latest` | 
| `app_port`          | `5000`                          |
| `web_app_full_wipe` | `true`                          |
| `deploy_dir` | `tmp`                           |
| `docker_container_name` | `app`                           | 


## Dependencies

This role depends on the `docker` role for installing and managing Docker.

## Directory Structure

```
roles/web_app/
|-- defaults
|   `-- main.yml
|-- meta
|   `-- main.yml
|-- tasks
|   |-- 0-wipe.yml
|   `-- main.yml
`-- templates
   `-- docker-compose.yml.j2
```

## Example Playbook

```yaml
- hosts: all
  roles:
    - role: web_app
      vars:
        docker_image: "my_app:latest"
        app_port: 8080
```

## Tags

| Tag      | Description |
|----------|-------------|
| `docker` | Pulls the Docker image and starts the container. |
| `setup`  | Installs and configures Docker. |
| `wipe`   | Removes the Docker container and related files. |

## Running Specific Tags

To run specific tasks, use:

```bash
ansible-playbook site.yml --tags docker
ansible-playbook site.yml --tags wipe
```

## Wipe Logic

To enable the wipe logic and remove the deployed container, set:

```yaml
web_app_full_wipe: true
```