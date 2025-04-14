# Docker Role

This role installs and configures Docker and Docker Compose.

## Requirements

- Ansible 2.9+
- Supported Operating Systems:
  - Arch Linux

## Role Variables

- `docker_version`: The version of Docker to install (default: `latest`).
- `docker_compose_version`: The version of Docker Compose to install (default: `v2.24.5`).

## Example Playbook

```yaml
- hosts: all
  become: true
  roles:
    - role: docker
```

## Usage

1. Include the role in your playbook.
2. Optionally override the default variables.
3. Run your playbook with the following command:
   ```bash
   ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml
   ```


# Web App Role

This role deploys a Docker image for the web application.

## Requirements

- Ansible 2.9+
- Docker installed on the target machine

## Role Variables

- `docker_image`: The Docker image to deploy (default: `favelanky/app_python`)
- `app_port`: The port to expose (default: `80`)
- `web_app_compose_dir`: Directory for Docker Compose files (default: `/opt/web-app`)
- `web_app_compose_file`: Name of the Docker Compose file (default: `docker-compose.yml`)
- `web_app_full_wipe`: Flag to enable/disable wipe logic (default: `false`)

## Example Playbook


## Usage

Run your playbook with the following command:

```bash
ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml

PLAY [Install Docker and Deploy Web App] *********************************************************************************************************

TASK [Gathering Facts] ***************************************************************************************************************************
ok: [localhost]

TASK [docker : Update apt cache] *****************************************************************************************************************
skipping: [localhost]

TASK [docker : Include Docker installation tasks] ************************************************************************************************
included: /home/fave/Uni/last_sem/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for localhost

TASK [docker : Check if Docker is installed] *****************************************************************************************************
changed: [localhost]

TASK [docker : Install Python dependencies for package management (Debian/Ubuntu)] ***************************************************************
skipping: [localhost]

TASK [docker : Install packages (Arch Linux)] ****************************************************************************************************
skipping: [localhost]

TASK [docker : Install packages (Debian/Ubuntu)] *************************************************************************************************
skipping: [localhost]

TASK [docker : Add Docker GPG key (Debian/Ubuntu)] ***********************************************************************************************
skipping: [localhost]

TASK [docker : Add Docker repository (Debian/Ubuntu)] ********************************************************************************************
skipping: [localhost]

TASK [docker : Install Docker (Debian/Ubuntu)] ***************************************************************************************************
skipping: [localhost]

TASK [docker : Install Docker (Arch Linux)] ******************************************************************************************************
skipping: [localhost]

TASK [docker : Ensure Docker service is enabled and started] *************************************************************************************
ok: [localhost]

TASK [docker : Add users to docker group] ********************************************************************************************************
skipping: [localhost]

TASK [docker : Add current user to docker group] *************************************************************************************************
ok: [localhost]

TASK [docker : Verify Docker Installation] *******************************************************************************************************
ok: [localhost]

TASK [docker : Debug Docker Version] *************************************************************************************************************
ok: [localhost] => {
    "msg": "Docker installed successfully: Docker version 27.5.1, build 9f9e405801"
}

TASK [docker : Include Docker Compose installation tasks] ****************************************************************************************
included: /home/fave/Uni/last_sem/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for localhost

TASK [docker : Download Docker Compose] **********************************************************************************************************
ok: [localhost]

TASK [web_app : Pull Docker image] ***************************************************************************************************************
ok: [localhost]

TASK [web_app : Create Docker Compose directory] *************************************************************************************************
ok: [localhost]

TASK [web_app : Template Docker Compose file] ****************************************************************************************************
ok: [localhost]

TASK [web_app : Start Docker Compose services] ***************************************************************************************************
ok: [localhost]

TASK [web_app : Start Docker container] **********************************************************************************************************
ok: [localhost]

TASK [web_app : Remove Docker container] *********************************************************************************************************
skipping: [localhost]

TASK [web_app : Remove Docker Compose files] *****************************************************************************************************
skipping: [localhost]

TASK [docker : Restart Docker] *******************************************************************************************************************
ok: [localhost]

PLAY RECAP ***************************************************************************************************************************************
localhost                  : ok=15   changed=1    unreachable=0    failed=0    skipped=7    rescued=0    ignored=0
```

