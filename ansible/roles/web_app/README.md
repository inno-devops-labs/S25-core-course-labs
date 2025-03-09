# Ansible Role: web_app

## Description
The `web_app` role deploys a Docker container with an application using `docker-compose`.

## Requirements
- Ansible 2.9+
- Docker and Docker Compose installed
- `geerlingguy.docker` role

## Variables
| Variable            | Description            | Default Value         |
|---------------------|------------------------|-----------------------|
| `docker_image`      | Docker image to deploy | `my-app:latest` |
| `app_port`          | Application port       | `8080`                |
| `web_app_full_wipe` | Enable wipe logic      | `false`               |

## Usage

Run the deployment:

 ```bash
 ansible-playbook site.yml --tags deploy