# Web Application Deployment Role

This Ansible role automates the deployment of a web application using Docker and Docker Compose v2.

## Requirements

- Ansible 2.9+
- Docker and Docker Compose v2 installed on the target host
- The `docker` Ansible role (declared as a dependency)

## Role Variables

All variables can be overridden in your playbook or inventory. Default values are set in `defaults/main.yml`:

| Variable                | Default Value                                 | Description                                 |
|-------------------------|-----------------------------------------------|---------------------------------------------|
| `docker_image`          | `grisharybolovlev/fastapi-app-python:latest`  | Docker image to deploy                      |
| `app_port`              | `8000`                                       | Host port to expose the application         |
| `web_app_full_wipe`     | `false`                                      | If true, removes all containers/files       |
| `docker_compose_version`| `3`                                           | Docker Compose file version (for template)  |
| `app_container_name`    | `web_app`                                    | Name of the Docker container                |
| `app_restart_policy`    | `unless-stopped`                             | Container restart policy                    |

## Usage Example

Add this role to your playbook:

```yaml
- hosts: webservers
  become: true
  roles:
    - role: web_app
      vars:
        docker_image: "grisharybolovlev/fastapi-app-python:latest"
        app_port: 8000
```

Run the playbook with the desired tags:

```bash
# Deploy the application
ansible-playbook playbooks/site.yml -i inventory/default_aws_ec2.yml --tags deploy

# Wipe the application (remove containers/files)
ansible-playbook playbooks/site.yml -i inventory/default_aws_ec2.yml --tags wipe -e web_app_full_wipe=true

# Full redeploy (wipe and deploy)
ansible-playbook playbooks/site.yml -i inventory/default_aws_ec2.yml --tags "wipe,deploy" -e web_app_full_wipe=true
```

## Tags

- `setup`: Prepare directories and environment
- `deploy`: Deploy and start the application
- `wipe`: Remove containers and related files
- `docker`: Docker-related operations

## Dependencies

- `docker` role (for Docker installation and setup)

## Structure

```
roles/web_app/
├── defaults/
│   └── main.yml
├── meta/
│   └── main.yml
├── tasks/
│   ├── 0-wipe.yml
│   └── main.yml
├── templates/
│   └── docker-compose.yml.j2
└── README.md
```