# Web Application Role

This Ansible role deploys a web application using Docker and Docker Compose.

## Requirements

- Ansible 2.9 or higher
- Target machine with:
  - Ubuntu 22.04 (Jammy) or compatible OS
  - SSH access with sudo privileges
  - Docker and Docker Compose (installed via docker role dependency)

## Role Variables

### Required Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `web_app_name` | Name of the web application | `demo-app` |
| `web_app_port` | Port to expose the application on | `8080` |
| `web_app_image` | Docker image to use | `nginx:latest` |

### Optional Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `web_app_container_name` | Name of the Docker container | `{{ web_app_name }}` |
| `web_app_data_dir` | Directory to store application data | `/opt/{{ web_app_name }}` |
| `web_app_restart_policy` | Container restart policy | `unless-stopped` |
| `web_app_full_wipe` | Whether to completely wipe the application | `false` |
| `web_app_health_check_path` | Path to use for health checks | `/` |
| `web_app_health_check_timeout` | Timeout for health checks | `10` |
| `web_app_env_vars` | Environment variables for the container | `NODE_ENV: "production", LOG_LEVEL: "info"` |

## Dependencies

- `docker` role for Docker and Docker Compose installation

## Example Playbook

```yaml
- hosts: servers
  roles:
    - role: web_app
      web_app_name: "my-application"
      web_app_port: 8080
      web_app_image: "mycompany/app:latest"
```

## Tags

The role uses the following tags:

- `setup`: Configure the application environment
- `deploy`: Deploy and start the application
- `verify`: Run health checks
- `wipe`: Clean up the application (requires `web_app_full_wipe: true`)
- `web_app`: All web application tasks
- `never`: Tasks that should not run by default (like wipe)

## Usage Examples

### Deploy Application

```bash
ansible-playbook playbook.yml -i inventory
```

### Wipe Application and Deploy Fresh

```bash
ansible-playbook playbook.yml -i inventory -e "web_app_full_wipe=true" --tags wipe,setup,deploy
```

### Run Health Check Only

```bash
ansible-playbook playbook.yml -i inventory --tags verify
```

## Author Information

Eleonora Pikalo, SD-02

Created for S25 Core Course Labs 