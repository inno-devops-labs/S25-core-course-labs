# Web App Role

This role deploys a Docker-based web application using Ansible. It includes tasks to pull the Docker image, start the container, and manage the application lifecycle. The role supports both Python and Java applications and includes a wipe feature to clean up deployments.

---

## Requirements

- **Ansible 2.9+**
- **Docker** installed on the target host.
- **Ubuntu 22.04** (or a compatible Linux distribution).

---

## Role Variables

### Default Variables (`defaults/main.yml`)
- **`docker_image`**:  
  The Docker image to deploy (e.g., `nickwidbestie/region-time-api:latest`).  
  Default: `nickwidbestie/region-time-api:latest`

- **`app_port`**:  
  The port to expose for the application.  
  Default: `8080`

- **`container_port`**:  
  The port exposed by the Docker container.  
  Default: `80`

- **`web_app_full_wipe`**:  
  Whether to remove all containers and related files.  
  Default: `true`

- **`web_app_deploy_dir`**:  
  The directory where the application will be deployed.  
  Default: `/opt/web_app`

---

## Tasks

### Main Tasks (`tasks/main.yml`)
1. **Wipe Existing Deployment**:
   - Calls the `0-wipe.yml` task file to clean up existing deployments if `web_app_full_wipe` is enabled.

2. **Deploy Web Application**:
   - Creates the deployment directory.
   - Renders the `docker-compose.yml` file from the Jinja2 template.
   - Pulls the Docker image.
   - Starts the application container using Docker Compose.

### Wipe Tasks (`tasks/0-wipe.yml`)
1. **Stop and Remove Docker Containers**:
   - Runs `docker-compose down` to stop and remove the containers.

2. **Remove Deployment Directory**:
   - Deletes the deployment directory and all its contents.

---

## Role Dependencies

The `web_app` role depends on the `docker` role to ensure Docker is installed and configured. This is specified in `roles/web_app/meta/main.yml`:

```yaml
dependencies:
  - role: docker
```

Example of a playbook for Python Application:

```commandline
- name: Deploy Python Application using Docker Compose
  hosts: all
  become: yes
  roles:
    - role: web_app
      vars:
        docker_image: "nickwidbestie/region-time-api:latest"
        app_port: "8000"
        container_port: "80"
        web_app_deploy_dir: "/opt/app_python"
        web_app_full_wipe: true
```

For Java application:

```commandline
- name: Deploy Java Application using Docker Compose
  hosts: all
  become: yes
  roles:
    - role: web_app
      vars:
        docker_image: "nickwidbestie/random-color-picker:6d9f319aeb8fe1782ca1a1037371a90ab8867a3f"
        app_port: "8081"
        container_port: "8081"
        web_app_deploy_dir: "/opt/app_java"
        web_app_full_wipe: true
```

## Tags

Tasks are grouped using tags for selective execution:

- **`deploy`**: Tasks related to deploying the application.
- **`wipe`**: Tasks for stopping and removing containers and files.

---

## Example Commands

- Run only deployment tasks:
  ```bash
  ansible-playbook playbooks/dev/main.yaml --tags deploy
  ```
  
- Run only wipe task:
  ```commandline
ansible-playbook playbooks/dev/main.yaml --tags wipe
    ```

## Docker Compose Template

The `docker-compose.yml.j2` template is used to generate the `docker-compose.yml` file:

```yaml
version: '3'
services:
  app:
    image: "{{ docker_image }}"
    ports:
      - "{{ app_port }}:{{ container_port }}"
  ```

# Output after the deploying 2 applications explicitly

 **Java**:

```commandline
ansible-playbook playbooks/dev/app_java/main.yml --tags web_app
```

```commandline

PLAY [Deploy Python Application using Docker Compose] *******************************************************************************************************************************************************

TASK [Gathering Facts] **************************************************************************************************************************************************************************************
[WARNING]: Platform linux on host yandex_vm_1 is using the discovered Python interpreter at /usr/bin/python3.10, but future installation of another Python interpreter could change the meaning of that
path. See https://docs.ansible.com/ansible-core/2.17/reference_appendices/interpreter_discovery.html for more information.
ok: [yandex_vm_1]

TASK [web_app : Create deployment directory for web_app] ****************************************************************************************************************************************************
ok: [yandex_vm_1]

TASK [web_app : Render Docker Compose template for the application] *****************************************************************************************************************************************
ok: [yandex_vm_1]

TASK [web_app : Pull Docker image for the application] ******************************************************************************************************************************************************
ok: [yandex_vm_1]

TASK [web_app : Start the application container using Docker Compose] ***************************************************************************************************************************************
changed: [yandex_vm_1]

PLAY RECAP **************************************************************************************************************************************************************************************************
yandex_vm_1                : ok=5    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

**Python**:

```commandline
ansible-playbook playbooks/dev/app_python/main.yml --tags web_app
```

```commandline

PLAY [Deploy Python Application using Docker Compose] *******************************************************************************************************************************************************

TASK [Gathering Facts] **************************************************************************************************************************************************************************************
[WARNING]: Platform linux on host yandex_vm_1 is using the discovered Python interpreter at /usr/bin/python3.10, but future installation of another Python interpreter could change the meaning of that
path. See https://docs.ansible.com/ansible-core/2.17/reference_appendices/interpreter_discovery.html for more information.
ok: [yandex_vm_1]

TASK [web_app : Create deployment directory for web_app] ****************************************************************************************************************************************************
ok: [yandex_vm_1]

TASK [web_app : Render Docker Compose template for the application] *****************************************************************************************************************************************
ok: [yandex_vm_1]

TASK [web_app : Pull Docker image for the application] ******************************************************************************************************************************************************
ok: [yandex_vm_1]

TASK [web_app : Start the application container using Docker Compose] ***************************************************************************************************************************************
changed: [yandex_vm_1]

PLAY RECAP **************************************************************************************************************************************************************************************************
yandex_vm_1                : ok=5    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 
```
