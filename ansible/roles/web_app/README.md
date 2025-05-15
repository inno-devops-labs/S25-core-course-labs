# Web Application Deployment Role

## Overview
This Ansible role automates the deployment and management of containerized web applications using Docker Compose. It's designed for CI/CD pipelines and supports both initial deployments and updates.

## Prerequisites
| Requirement          | Version/Details              |
|----------------------|------------------------------|
| Ansible              | 2.18+                        |
| OS                   | Ubuntu 22.04 LTS             |
| Docker               | 20.10.0+                     |
| Docker Compose       | 1.29.2+                      |

## Configuration Variables
### Main Parameters
| Variable            | Default | Description                              |
|---------------------|---------|------------------------------------------|
| `app_port`          | 9200    | Host port mapped to container port       |
| `web_app_full_wipe` | false   | When true, performs complete redeploy    |

## Example Playbook

```yaml
- hosts: all
  become: true
  roles:
    - role: web_app
```