# Docker Role README
## Overview
This Ansible role automates the installation and configuration of Docker and Docker Compose on a target system. It ensures that Docker is installed, Docker Compose is available, and the current user is added to the Docker group for seamless Docker operations.

## Requirements
Ansible installed on the control machine.
Access to the target machine with sudo privileges.
## Role Variables
`ansible_user`: The user to be added to the Docker group. This is typically the user running the Ansible playbook.
## Dependencies
- Ansible 2.9+
 - Ubuntu 22.04

## Example Playbook
Here is an example of how to use this role in a playbook:

``` yaml
- hosts: localhost
  connection: local
  become: yes
  roles:
    - docker
```
## Tasks
- Update apt cache: Ensures the package list is up-to-date.
- Install Docker: Installs Docker using the apt module.
- Install Docker Compose: Downloads and installs Docker Compose from the official GitHub releases.
- Add current user to the Docker group: Adds the current user to the Docker group to allow running Docker commands without sudo.
## Usage
Ensure you have Ansible installed on your control machine.

Create a playbook file (e.g., main.yml) and include this role.

Run the playbook using the command:

``` bash
ansible-playbook -i local ./playbook/dev/main.yml
```
