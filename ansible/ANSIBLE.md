# Lab 6: Ansible and Application Deployment

## Overview

This lab demonstrates how to use **Ansible** to set up a **Continuous Deployment (CD) process** for a **Python and Node.js application**, using **Docker** and **Docker Compose**. The setup ensures:

- **`main.yaml` installs Docker only**.
- **`app_python/main.yaml` installs Docker and deploys the Python app**.
- **`app_node/main.yaml` installs Docker and deploys the Node.js app, ensuring Python remains deployed**.

This configuration prevents **overwriting issues** and ensures that both applications can run concurrently without conflicts.

---

## Repository Structure Now

```sh
ansible/
├── inventory/
│   ├── default_aws_ec2.yml
│   ├── dynamic_inventory.yml
│
├── playbooks/
│   ├── dev/
│   │   ├── main.yaml   # Installs Docker only
│   │   ├── app_python/
│   │   │   ├── main.yaml   # Installs Docker and deploys Python
│   │   ├── app_node/
│   │   │   ├── main.yaml   # Installs Docker and deploys Node.js
│
├── roles/
│   ├── web_app/
│   │   ├── defaults/
│   │   │   ├── main.yml
│   │   ├── tasks/
│   │   │   ├── main.yml
│   │   ├── templates/
│   │   │   ├── docker-compose.yml.j2  # Default for Python
│   │   │   ├── docker-compose-node.yml.j2  # Custom for Node.js
│   │   ├── meta/
│   │   │   ├── main.yml
│
└── ansible.cfg
```

---

## Task 1: Application Deployment

### **Setting Up the `web_app` Role**

- Created `ansible/roles/web_app` using `ansible-galaxy init roles/web_app`.
- Defined **Docker image variables** in `defaults/main.yml`:

```yaml
docker_image_python: "em1999jay/python-app"
docker_image_node: "em1999jay/moscow-time-app-node:v1"

app_python_port: "5000"
app_node_port: "3000"

web_app_full_wipe: false  # Can be set to true for wipe logic

```

- Created **`tasks/main.yml`** to pull Docker images and start containers.

### **Updating `docker-compose.yml.j2` and `docker-compose-node.yml.j2`**

**Python Application (Default Template):**

```yaml
services:
  python_app:
    image: "{{ docker_image_python }}"
    ports:
      - "{{ app_python_port }}:5000"
    restart: always
```

**Node.js Application (Custom Template):**

```yaml
services:
  node_app:
    image: "{{ docker_image_node }}"
    ports:
      - "{{ app_node_port }}:3000"
    restart: always
```

---

## Task 2: Ansible Best Practices

### **Using Blocks to Group Tasks**

- Organized `tasks/main.yml` with `block:` to group related tasks.

```yaml
- name: Pull Python Docker Image
  when: app_port == app_python_port
  community.docker.docker_image:
    name: "{{ docker_image_python }}"
    source: pull
  tags:
    - docker

- name: Pull Node.js Docker Image
  when: app_port == app_node_port
  community.docker.docker_image:
    name: "{{ docker_image_node }}"
    source: pull
  tags:
    - docker

- name: Deploy Python Application with Docker Compose (Default Template)
  when: app_port == app_python_port
  ansible.builtin.template:
    src: docker-compose.yml.j2  # Existing default template for Python
    dest: /home/ubuntu/docker-compose.yml
    owner: ubuntu
    group: ubuntu
    mode: "0644"

- name: Deploy Node.js Application with Custom Docker Compose
  when: app_port == app_node_port
  ansible.builtin.template:
    src: docker-compose-node.yml.j2  # New separate template for Node.js
    dest: /home/ubuntu/docker-compose-node.yml
    owner: ubuntu
    group: ubuntu
    mode: "0644"

- name: Start Python Application with Docker Compose v2
  when: app_port == app_python_port
  community.docker.docker_compose_v2:
    project_src: /home/ubuntu
  tags:
    - deploy

- name: Start Node.js Application with Docker Compose v2
  when: app_port == app_node_port
  community.docker.docker_compose_v2:
    project_src: /home/ubuntu
  tags:
    - deploy

```

### **Role Dependencies**

- Added `meta/main.yml` to make `web_app` **depend on `docker`**:

```yaml
dependencies:
  - role: docker
```

### **Implementing Wipe Logic**

- Created `tasks/0-wipe.yml` to remove previous containers and files:

```yaml
- name: Remove Existing Containers
  community.docker.docker_container:
    name: web_app
    state: absent
  when: web_app_full_wipe | bool
```

- Used a **separate wipe tag**:

```sh
ansible-playbook ansible/playbooks/dev/main.yaml --tags wipe
```

## Final Steps and Verification

### **Run Docker Setup Only**

```sh
ansible-playbook -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/main.yaml
```

- **Last 50 lines of execution output of <app_python/main.yaml>**:

```sh
moe@Moe-Laptop:~/Uni/DOVEPS1/S25-core-course-labss$ ansible-playbook -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/app_python/main.yaml

PLAY [Setup Docker and Deploy Python Application] ********************************************************************************************************************************************************

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

TASK [docker : include_tasks] ****************************************************************************************************************************************************************************
included: /home/moe/Uni/DOVEPS1/S25-core-course-labss/ansible/roles/docker/tasks/secure_docker_config.yml for server1

TASK [docker : Secure Docker Daemon Configuration] *******************************************************************************************************************************************************
ok: [server1]

TASK [docker : Enable Docker to start on boot] ***********************************************************************************************************************************************************
ok: [server1]

TASK [docker : Add user to the Docker group] *************************************************************************************************************************************************************
ok: [server1]

TASK [web_app : Pull Python Docker Image] ****************************************************************************************************************************************************************
ok: [server1]

TASK [web_app : Pull Node.js Docker Image] ***************************************************************************************************************************************************************
skipping: [server1]

TASK [web_app : Deploy Python Application with Docker Compose (Default Template)] ************************************************************************************************************************
changed: [server1]

TASK [web_app : Deploy Node.js Application with Custom Docker Compose] ***********************************************************************************************************************************
skipping: [server1]

TASK [web_app : Start Python Application with Docker Compose v2] *****************************************************************************************************************************************
changed: [server1]

TASK [web_app : Start Node.js Application with Docker Compose v2] ****************************************************************************************************************************************
skipping: [server1]

PLAY RECAP ***********************************************************************************************************************************************************************************************
server1                    : ok=27   changed=5    unreachable=0    failed=0    skipped=6    rescued=0    ignored=0   

moe@Moe-Laptop:~/Uni/DOVEPS1/S25-core-course-labss$ 
```

### **Run Python App**

```sh
ansible-playbook -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/app_python/main.yaml
```

Verify it is running:

```sh
curl http://18.233.159.212:5000
```

### **Run Node.js App**

```sh
ansible-playbook -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/app_node/main.yaml
```

Verify it is running:

```sh
curl http://18.233.159.212:3000
```

### **Confirm Running Containers**

```sh
docker ps
```

Output:

![bothrunning](./Screenshots/bothrunning.png)

---

## **Conclusion**

**`main.yaml` installs Docker only.**  
**`app_python/main.yaml` installs Docker and deploys Python.**  
**`app_node/main.yaml` installs Docker and deploys Node.js without overwriting Python.**  
**Ansible best practices: structured roles, dependencies, and modular playbooks.**  
**Successfully deployed both applications using Ansible.**  

## Ansible Deployment - Lab 5

### Overview Lab 5

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
```

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

1: Check running Docker containers:

```sh
  ubuntu@ip-172-31-83-93:~$ docker ps
  CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                                     NAMES
  4f0b6c5fb044   nginx:latest   "/docker-entrypoint.…"   35 minutes ago   Up 35 minutes   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   ubuntu-app-1
```

   Ensure that a container is running with the expected image and port mapping.

2: Check Docker logs:

   ```sh
    ubuntu@ip-172-31-83-93:~$ docker logs 4f0b6c5fb044
    /docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
    /docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
    /docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
    10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
    10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
    /docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
    /docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
    /docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
    /docker-entrypoint.sh: Configuration complete; ready for start up
    2025/02/15 23:53:45 [notice] 1#1: using the "epoll" event method
    2025/02/15 23:53:45 [notice] 1#1: nginx/1.27.4
    2025/02/15 23:53:45 [notice] 1#1: built by gcc 12.2.0 (Debian 12.2.0-14) 
    2025/02/15 23:53:45 [notice] 1#1: OS: Linux 6.8.0-1021-aws
    2025/02/15 23:53:45 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
    2025/02/15 23:53:45 [notice] 1#1: start worker processes
    2025/02/15 23:53:45 [notice] 1#1: start worker process 29
   ```

   This helps troubleshoot any issues if the application does not start as expected.

## Screenshots

To verify successful deployment, included the following screenshots:

- **Docker Installed:**

 ![Docker Installed](./Screenshots/Docker_installed.png)

- **Docker Compose Installed:**

 ![Docker Compose Installed](./Screenshots/docker_compose_installed.png)

- **Running Containers:**

 ![Docker ps](./Screenshots/docker_ps.png)

- **Ansible Inventory:**

 ![Inventory](./Screenshots/inventory.png)

- **Ansible Graph:**

 ![Graph](./Screenshots/graph.png)

## Conclusion

This setup successfully deploys Docker and a web application using Ansible. All deployment steps and verifications ensure that Docker and the web application are configured correctly for further development.

## Bonus Task: Dynamic Inventory for AWS

### Implement AWS EC2 Dynamic Inventory

I created a new dynamic inventory file has been created to dynamically fetch AWS EC2 instances instead of using a static inventory file.

**File:** `ansible/inventory/dynamic_inventory.yml`

```yaml
plugin: amazon.aws.aws_ec2
regions:
  - us-east-1
filters:
  tag:Name: "ExampleAppServerInstance"
  instance-state-name: running
hostnames:
  - tag:Name
  - public-ip-address
compose:
  ansible_host: public-ip-address
```

## Bonus Task: Secure Docker Configuration

### **Step 1: Secure Docker Daemon Configuration**

A new security configuration has been added to ensure Docker is hardened against privilege escalation and unnecessary risks. The configuration is applied using the `copy` module in Ansible.

**Task File:** `ansible/roles/docker/tasks/secure_docker_config.yml`

```yaml
- name: Secure Docker Daemon Configuration
  ansible.builtin.copy:
    content: |
      {
        "no-new-privileges": true,
        "userns-remap": "default",
        "log-driver": "json-file",
        "log-opts": {
          "max-size": "10m",
          "max-file": "3"
        },
        "icc": false,
        "live-restore": true,
        "userland-proxy": false
      }
    dest: /etc/docker/daemon.json
    owner: root
    group: root
    mode: '0644'
  notify: restart docker
```

### **Step 2: Ensure Docker Restarts After Applying Security Settings**

**Handler File:** `ansible/roles/docker/handlers/main.yml`

```yaml
- name: restart docker
  ansible.builtin.systemd:
    name: docker
    state: restarted
    enabled: yes
```

### **Step 3: Verify Docker Security Configuration**

After applying the playbook, confirm that the security settings are enforced.

Run the following command on the remote server:

```sh
cat /etc/docker/daemon.json
```

Expected Output:

```json
{
  "no-new-privileges": true,
  "userns-remap": "default",
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "10m",
    "max-file": "3"
  },
  "icc": false,
  "live-restore": true,
  "userland-proxy": false
}
```

### **Screenshots**

- **Secure Docker Configuration Applied:**

![Secure Docker Config](./Screenshots/bonus.png)

## Conclusion Of This Task

This setup successfully deploys Docker and a web application using Ansible while implementing additional security enhancements through `daemon.json`. All deployment steps and verifications ensure that Docker and the web application are configured correctly for further development.
