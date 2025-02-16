# Ansible Deployment - Lab 5

## Overview

This document outlines the deployment process for Docker using Ansible. The objective of this lab is to automate the installation of Docker and Docker Compose on a remote server using Ansible and ensure that a containerized web application is successfully deployed.

## Repository Structure

Ensure your repository follows this structure:

```sh
.
|-- ansible
|   |-- inventory
|   |   `-- default_aws_ec2.yml
|   |-- playbooks
|   |   `-- dev
|   |       `-- main.yaml
|   |-- roles
|   |   |-- docker
|   |   |   |-- defaults
|   |   |   |   `-- main.yml
|   |   |   |-- handlers
|   |   |   |   `-- main.yml
|   |   |   |-- tasks
|   |   |   |   |-- install_compose.yml
|   |   |   |   |-- install_docker.yml
|   |   |   |   `-- main.yml
|   |   |   `-- README.md
|   |   `-- web_app
|   |       |-- defaults
|   |       |   `-- main.yml
|   |       |-- handlers
|   |       |   `-- main.yml
|   |       |-- meta
|   |       |   `-- main.yml
|   |       |-- tasks
|   |       |   `-- main.yml
|   |       `-- templates
|   |           `-- docker-compose.yml.j2
|   `-- ansible.cfg
```

## Setup and Execution

### **Step 1: Install Dependencies**

Run the Ansible playbook to install Docker and deploy the application:

```sh
ansible-playbook -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/main.yaml
```

### **Step 2: Verify Docker Installation**

Check if Docker and Docker Compose are correctly installed:

```sh
docker --version
docker compose version
```

### **Step 3: Validate Deployment**

Verify that the application is running by checking active Docker containers:

```sh
docker ps
```

If successful, the application should be running and accessible via:

```sh
http://52.90.192.156:8080
```

## Playbook Execution

The playbook executes the following steps:

1. Installs required dependencies such as `ca-certificates`, `curl`, and `gnupg`.
2. Adds the Docker GPG key and repository to the system.
3. Installs Docker and Docker Compose.
4. Ensures Docker is enabled and started on boot.
5. Copies the `docker-compose.yml` template to the remote server.
6. Starts the web application using Docker Compose.

- **Dry run (`--check` mode)**:

  ```sh
  ansible-playbook -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/main.yaml --check --diff
  ```

- **Last 50 lines of execution output**:

  ```sh

PLAY [all] ***********************************************************************************************************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************************************************************************************************
ok: [server1]

TASK [docker : include_tasks] ****************************************************************************************************************************************************************************
included: /home/moe/Uni/DOVEPS1/S25-core-course-labss/ansible/roles/docker/tasks/install_docker.yml for server1

TASK [docker : Install required dependencies] ************************************************************************************************************************************************************
ok: [server1]

TASK [docker : Ensure /etc/apt/keyrings directory exists] ************************************************************************************************************************************************
ok: [server1]

TASK [docker : Add Docker GPG key] ***********************************************************************************************************************************************************************
changed: [server1]

TASK [docker : Add Docker repository] ********************************************************************************************************************************************************************
changed: [server1]

TASK [docker : Update package cache] *********************************************************************************************************************************************************************
changed: [server1]

TASK [docker : Install Docker packages] ******************************************************************************************************************************************************************
ok: [server1]

TASK [docker : Ensure /etc/docker/ directory exists] *****************************************************************************************************************************************************
ok: [server1]

TASK [docker : Configure Docker daemon options (if any)] *************************************************************************************************************************************************
skipping: [server1]

TASK [docker : Ensure Docker is started and enabled at boot] *********************************************************************************************************************************************
ok: [server1]

TASK [docker : Flush handlers to restart Docker immediately] *********************************************************************************************************************************************

TASK [docker : include_tasks] ****************************************************************************************************************************************************************************
included: /home/moe/Uni/DOVEPS1/S25-core-course-labss/ansible/roles/docker/tasks/install_compose.yml for server1

TASK [docker : Check current docker-compose version] *****************************************************************************************************************************************************
ok: [server1]

TASK [docker : Extract current version of Docker Compose] ************************************************************************************************************************************************
ok: [server1]

TASK [docker : Delete existing Docker Compose version if outdated] ***************************************************************************************************************************************
ok: [server1]

TASK [docker : Install Docker Compose if not installed or outdated] **************************************************************************************************************************************
skipping: [server1]

TASK [docker : Install Docker Compose Plugin] ************************************************************************************************************************************************************
ok: [server1]

TASK [docker : include_tasks] ****************************************************************************************************************************************************************************
included: /home/moe/Uni/DOVEPS1/S25-core-course-labss/ansible/roles/docker/tasks/install_compose.yml for server1

TASK [docker : Check current docker-compose version] *****************************************************************************************************************************************************
ok: [server1]

TASK [docker : Extract current version of Docker Compose] ************************************************************************************************************************************************
ok: [server1]

TASK [docker : Delete existing Docker Compose version if outdated] ***************************************************************************************************************************************
ok: [server1]

TASK [docker : Install Docker Compose if not installed or outdated] **************************************************************************************************************************************
skipping: [server1]

TASK [docker : Install Docker Compose Plugin] ************************************************************************************************************************************************************
ok: [server1]

TASK [docker : Enable Docker to start on boot] ***********************************************************************************************************************************************************
ok: [server1]

TASK [docker : Add user to the Docker group] *************************************************************************************************************************************************************
changed: [server1]

TASK [web_app : Deploy Web Application] ******************************************************************************************************************************************************************
ok: [server1]

TASK [web_app : Start Application] ***********************************************************************************************************************************************************************
changed: [server1]

PLAY RECAP ***********************************************************************************************************************************************************************************************
server1                    : ok=24   changed=5    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0

## Inventory Details

- Run the following to check the inventory:

  ```sh
  ansible-inventory -i ansible/inventory/default_aws_ec2.yml --list
  ```

- Validate the inventory structure:

  ```sh
  ansible-inventory -i ansible/inventory/default_aws_ec2.yml --graph
  ```

## Deployment Verification

After running the playbook, verify the following:

1. **Check running Docker containers**:

   ```sh
   docker ps
   ```

   Ensure that a container is running with the expected image and port mapping.

2. **Test web application access**:
   - Open a web browser and navigate to:

     ```sh
     http://52.90.192.156:8080
     ```

   - You should see the default page or application UI if configured correctly.

3. **Check Docker logs**:

   ```sh
   docker logs nginx:latest 
   ```

   This helps troubleshoot any issues if the application does not start as expected.

## Screenshots

To verify successful deployment, included the following screenshots:

- **Docker Installed:**
 ![Docker Installed](Docker_installed.png)
- **Docker Compose Installed:**
 ![Docker Compose Installed](docker_compose_installed.png)
- **Running Containers:**
 ![Docker ps](docker_ps.png)
- **Ansible Inventory:**
 ![Inventory](inventory.png)

## Conclusion

This setup successfully deploys Docker and a web application using Ansible. All deployment steps and verifications ensure that Docker and the web application are configured correctly for further development.
