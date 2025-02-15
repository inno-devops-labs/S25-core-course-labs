# App Java Role

This Ansible role deploys a Java application using Docker and Docker Compose.

## Requirements
- Ansible 2.9+
- Java application
- Docker installed on the target machine

## Variables
- `app_java_directory`: Directory where the Java app is deployed
- `app_java_image`: Docker image for the Java app
- `app_java_port`: Port exposed by the application

## Example Playbook

```yaml
- name: Deploy Java Application
  hosts: docker_vm
  become: yes
  roles:
    - app_java
