# Docker Role  

This role handles the installation and configuration of Docker along with Docker Compose.  

## Prerequisites  

- Ubuntu 22.04 operating system  
- Ansible version 2.9 or higher  

## Role Variables  

- `docker_version`: Specifies the Docker version to install (default: `latest`).  
- `docker_compose_version`: Specifies the Docker Compose version to install (default: `1.29.2`).  

## Example Playbook  

```yaml  
- name: Install and Configure Docker  
  hosts: all  
  become: true  
  roles:  
    - docker
