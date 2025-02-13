Web_app Role
=========

This role deploys application's Docker container using best practices for continuous deployment, maintenance, and cleanup. It integrates with a dependency on the Docker role to ensure Docker is installed and running before deploying your application.

Requirements
------------


- **Ansible:** Version 2.9 or higher.
- **OS:** Ubuntu 22.04 (or a compatible Linux distribution).
- **Docker & Docker Compose:** The Docker role (dependency) ensures Docker is installed. This role deploys your application container and manages a Docker Compose file.


Role Variables
--------------

Define these variables in `defaults/main.yml`:

- `docker_image`: The Docker image to deploy (default: `"latest"`).
- `container_name`: The name of the Docker container (default: `"web_app"`).

Defined in `vars/main.yml`:  
- `app_port`:  The port on the host machine to expose application (default: 8080) 

- `container_port`: The port inside the Docker container (default: 8080) 

- `web_app_full_wipe`: Set to `true` to enable wipe logic that removes the container and cleans up related files (default: `true`).


Dependencies
------------

This role depends on other roles available on Ansible Galaxy. Ensure that these roles are installed and properly configured before using this role.

### Required Roles

- **docker** (or **geerlingguy.docker**):  
  This role is required for installing and configuring Docker on target hosts. It provides essential variables and tasks needed by the web_app role.  

  **Key Variables Provided by the Docker Role:**
  - `docker_version`: Specifies the version of Docker to install (default: `latest`).
  - `docker_compose_version`: Specifies the version of Docker Compose to install (default: `1.29.2`).
  - `docker_service_name`: Name of the Docker service (commonly `docker`).

  **Installation Example:**
  ```bash
  ansible-galaxy install geerlingguy.docker

Example Playbook
----------------
```bash
- name: Deploy web_app
  hosts: reg_instance_1
  vars_files: 
    - vars/main.yml
  become: true
  roles:
    - web_app
```

License
-------

BSD

Author Information
------------------

B22-SD-02, Qodirzoda Anushervon, a.qodirzoda@innopolis.university 
