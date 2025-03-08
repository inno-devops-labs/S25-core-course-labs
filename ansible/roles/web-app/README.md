# WebApp Role README
## Overview
This Ansible role automates the deployment of a web application using Docker Compose. It ensures that Docker Compose is installed, creates the necessary directory structure, copies the Docker Compose configuration, and deploys the application.

## Requirements
Ansible installed on the control machine.
Access to the target machine with sudo privileges.
The docker role must be available to ensure Docker Compose is installed.
## Role Variables
`ansible_user` : The user who will own the application directory and files. This is typically the user running the Ansible playbook.
## Dependencies
The docker role is a dependency and must be included to ensure Docker Compose is installed.
Example Playbook
Here is an example of how to use this role in a playbook:

```yaml
- hosts: localhost
  connection: local
  become: yes
  roles:
    - web-app
```
## Tasks
1. Ensure Docker Compose is installed: Includes the docker role to install Docker Compose.
2. Create directory for app: Creates a directory at /opt/web-app for the application, setting the owner and group to the current user.
3. Copy Docker Compose template: Copies the Docker Compose configuration template to the application directory.
4. Deploy application with Docker Compose: Uses Docker Compose to deploy the application from the configuration file.
## Usage
Ensure you have Ansible installed on your control machine.

Create a playbook file  and include this role.

Run the playbook using the command:

``` bash
ansible-playbook -i local ./playbook/dev/main.yml
```
