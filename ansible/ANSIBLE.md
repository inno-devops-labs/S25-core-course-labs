## File Breakdown

### 1. **Inventory File: `ansible/inventory/default_yacloud_compute.yml`**

This file contains the inventory configuration for the target cloud instance (`ya_cloud_vm`). It includes the VM's IP address, SSH user, and private key location.

Content:
```yaml
all:
  hosts:
    ya_cloud_vm:
      ansible_host: 158.160.143.18
      ansible_user: ren
      ansible_ssh_private_key_file: /home/ren/.ssh/id_ed25519
```

- **Explanation**: The `ansible_host` specifies the IP address of the VM, and the `ansible_ssh_private_key_file` points to the private SSH key for authentication.

---

### 2. **Custom Docker Role Playbook: `ansible/playbooks/dev/customRole.yml`**

This playbook is used to set up the custom Docker role on the cloud instance. The role installs Docker and Docker Compose, configures them to start on boot, and adds the current user to the Docker group.

Content:
```yaml
- name: Setup Custom Docker Role
  hosts: ya_cloud_vm
  become: true
  roles:
    - "../../roles/docker"
```

- **Explanation**: The playbook applies the custom Docker role located in `roles/docker` to the `ya_cloud_vm` host.

---

### 3. **Initial Docker Role Playbook: `ansible/playbooks/dev/initial.yml`**

This playbook uses a pre-existing role from Ansible Galaxy (`geerlingguy.docker`) to set up Docker.

Content:
```yaml
- name: Setup Docker on VM
  hosts: ya_cloud_vm
  become: true
  roles:
    - geerlingguy.docker
```

---

### 4. **Docker Version and Docker Compose Version: `ansible/roles/docker/defaults/main.yml`**

This file defines the default versions of Docker and Docker Compose to be installed.

Content:
```yaml
docker_version: "5:27.5.1-1~ubuntu.24.04~noble"
docker_compose_version: "v2.33.0"
```

---

### 5. **Installing Docker Compose: `ansible/roles/docker/tasks/install_compose.yml`**

This task installs Docker Compose by downloading the specified version from GitHub and saving it to `/usr/local/bin/docker-compose`.

Content:
```yaml
- name: Install Docker Compose
  get_url:
    url: "https://github.com/docker/compose/releases/download/{{ docker_compose_version }}/docker-compose-{{ ansible_system | lower }}-{{ ansible_architecture }}"
    dest: "/usr/local/bin/docker-compose"
    mode: '0755'
```

- **Explanation**: The `get_url` module is used to download the Docker Compose binary for the specified operating system and architecture.

---

### 6. **Installing Docker: `ansible/roles/docker/tasks/install_docker.yml`**

This task adds Docker’s GPG key, sets up the repository, and installs Docker using `apt`.

Content:
```yaml
- name: Install Docker
  apt:
    name: "docker-ce={{ docker_version }}"
    state: present
    force: yes
    update_cache: yes
```

---

### 7. **Main Docker Role Tasks: `ansible/roles/docker/tasks/main.yml`**

This is the main task file for the Docker role. It installs necessary dependencies, includes the tasks to install Docker and Docker Compose, enables Docker to start on boot, and adds the current user to the Docker group, configures security settings.

Content:
```yaml
- name: Setup Docker Env
  block:
    - name: Install packages
      apt:
        name:
          - apt-transport-https
          - ca-certificates
          - curl
          - software-properties-common
        state: present
        update_cache: yes

    - name: Add Docker's GPG key
      apt_key:
        url: https://download.docker.com/linux/ubuntu/gpg
        state: present

    - name: Set up the repository
      apt_repository:
        repo: "deb [arch=amd64] https://download.docker.com/linux/ubuntu {{ ansible_distribution_release | lower }} stable"
        state: present
        update_cache: yes
  tags:
    - setup

- include_tasks: install_docker.yml

- include_tasks: install_compose.yml

- name: Post-Setup Docker Configuration
  block:
    - name: Configure Docker security settings
      copy:
        content: |
          {
            "no-new-privileges": true,
            "userns-remap": "default",
            "selinux-enabled": true
          }
        dest: /etc/docker/daemon.json
        owner: root
        group: root
        mode: '0644'
      notify:
        - Restart Docker

    - name: Enable Docker service to start on boot
      systemd:
        name: docker
        enabled: yes
        state: started

    - name: Add current user to docker group
      user:
        name: "{{ ansible_user }}"
        groups:
          - docker
        append: yes
```

- **Explanation**: This task file manages package installations, Docker installation, Docker Compose installation, service management, security settings, and user group update. It ensures that Docker is set to start on boot and the user has the necessary permissions to run Docker without `sudo`.

---

## Running the Playbook

To run the playbook and verify the changes without applying them, used the following command:

```bash
ansible-playbook ansible/playbooks/dev/customRole.yml --check --diff
```

### Diff output (tail -n 50)
```text
PLAY [Setup Custom Docker Role] ************************************************
 
TASK [Gathering Facts] *********************************************************
ok: [ya_cloud_vm]
 
TASK [../../roles/docker : Install packages] ***********************************
ok: [ya_cloud_vm]
 
TASK [../../roles/docker : include_tasks] **************************************
included: /home/ren/labs/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for ya_cloud_vm
 
TASK [../../roles/docker : Add Docker's GPG key] *******************************
changed: [ya_cloud_vm]
 
TASK [../../roles/docker : Set up the repository] ******************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/download_docker_com_linux_ubuntu.list
@@ -0,0 +1 @@
+deb [arch=amd64] https://download.docker.com/linux/ubuntu noble stable
 
changed: [ya_cloud_vm]
 
TASK [../../roles/docker : Install Docker] *************************************
ok: [ya_cloud_vm]
 
TASK [../../roles/docker : include_tasks] **************************************
included: /home/ren/labs/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for ya_cloud_vm
 
TASK [../../roles/docker : Install Docker Compose] *****************************
changed: [ya_cloud_vm]
 
TASK [../../roles/docker : Enable Docker service to start on boot] *************
ok: [ya_cloud_vm]
 
TASK [../../roles/docker : Add current user to docker group] *******************
changed: [ya_cloud_vm]
 
PLAY RECAP *********************************************************************
ya_cloud_vm                : ok=10   changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Inventory Details

### List
```json
{
    "_meta": {
        "hostvars": {
            "ya_cloud_vm": {
                "ansible_host": "158.160.143.18",
                "ansible_ssh_private_key_file": "/home/ren/.ssh/id_ed25519",
                "ansible_user": "ren"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped"
        ]
    },
    "ungrouped": {
        "hosts": [
            "ya_cloud_vm"
        ]
    }
}
```

### Graph
```text
@all:
  |--@ungrouped:
  |  |--ya_cloud_vm
```

## Dynamic Inventory (Yandex Cloud)
Unfortunately, after around 4-5 hours of work, I didnt reach the goal of the task. I have tried to use given [plugin](https://github.com/rodion-goritskov/yacloud_compute) but it seems to be outdated or I just havent found enough info to set this up properly. 

### What Was Done:
- 1. Downloaded yacloud_compute.py (plugin)
- 2. Plugin moved to ~/ansible/inventory/ folder
- 3. Previous inventory file renamed to yacloud_compute.yml and content changed to be suitable for plugin (according to .py doc: folder_names, cloud_names, oauth token).
- 4. Modified ansible/ansible.cfg to point onto the script
- 5. Tested playbook. Fixed yandexcloud missed package and some other errors
- 6. Tested another [plugin](https://gitlab.com/tyumentsev4/yandex-cloud-ansible-dynamic-inventory?ysclid=m77qqo7f4r965912550) found on gitlab
- 7. Some more actions to satisfy requirements
- 8. Surrender
- 9. Rollback to the previously created inventory file

## Securing Docker Configuration:

- Security settings are being changed via modifying `daemon.json`
```yaml
- name: Configure Docker security settings
  copy:
    content: |
      {
        "no-new-privileges": true,
        "userns-remap": "default",
        "selinux-enabled": true
      }
    dest: /etc/docker/daemon.json
    owner: root
    group: root
    mode: '0644'
  notify:
    - Restart Docker
```

- Docker restart (`roles/docker/handlers/main.yml`) being triggered after the configuration is copied
```yaml
- name: Restart Docker
  systemd:
    name: docker
    state: restarted
```

## Application Deployment Log (Lab 6 Task 1)

```text
PLAY [Deploy Python Web App] ***************************************************

TASK [Gathering Facts] *********************************************************
ok: [ya_cloud_vm]

TASK [../../../roles/web_app : Pull Docker Image] ******************************
changed: [ya_cloud_vm]

TASK [../../../roles/web_app : Start Docker] ***********************************
--- before
+++ after
@@ -1,3 +1,3 @@
 {
-    "exists": false
+    "exists": true
 }

changed: [ya_cloud_vm]

PLAY RECAP *********************************************************************
ya_cloud_vm                : ok=3    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 
```

## Applycation Deployment Log (Web App Role, Lab 6 Task 2)
```text
PLAY [Deploy Python Web App] ***************************************************

TASK [Gathering Facts] *********************************************************
ok: [ya_cloud_vm]

TASK [docker : Install packages] ***********************************************
ok: [ya_cloud_vm]

TASK [docker : Add Docker's GPG key] *******************************************
ok: [ya_cloud_vm]

TASK [docker : Set up the repository] ******************************************
ok: [ya_cloud_vm]

TASK [docker : include_tasks] **************************************************
included: /home/ren/labs/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for ya_cloud_vm

TASK [docker : Install Docker] *************************************************
ok: [ya_cloud_vm]

TASK [docker : include_tasks] **************************************************
included: /home/ren/labs/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for ya_cloud_vm

TASK [docker : Install Docker Compose] *****************************************
ok: [ya_cloud_vm]

TASK [docker : Configure Docker security settings] *****************************
ok: [ya_cloud_vm]

TASK [docker : Enable Docker service to start on boot] *************************
ok: [ya_cloud_vm]

TASK [docker : Add current user to docker group] *******************************
ok: [ya_cloud_vm]

TASK [../../../roles/web_app : Pull Docker Image] ******************************
ok: [ya_cloud_vm]

TASK [../../../roles/web_app : Copy Compose Template] **************************
ok: [ya_cloud_vm]

TASK [../../../roles/web_app : Deploy Via Compose] *****************************
changed: [ya_cloud_vm]

TASK [../../../roles/web_app : include_tasks] **********************************
skipping: [ya_cloud_vm]

PLAY RECAP *********************************************************************
ya_cloud_vm                : ok=14   changed=1    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
```

## Applycation Deployment+Prev. Wipe Log (Go Web App Role, Lab 6 Bonus Task)
```bash
ansible-playbook playbooks/dev/app_go/main.yml -e "web_app_full_wipe=true"
```

```text
PLAY [Deploy Go Web App] *******************************************************
 
TASK [Gathering Facts] *********************************************************
ok: [ya_cloud_vm]
 
TASK [docker : Install packages] ***********************************************
ok: [ya_cloud_vm]
 
TASK [docker : Add Docker's GPG key] *******************************************
ok: [ya_cloud_vm]
 
TASK [docker : Set up the repository] ******************************************
ok: [ya_cloud_vm]
 
TASK [docker : include_tasks] **************************************************
included: /home/ren/labs/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for ya_cloud_vm
 
TASK [docker : Install Docker] *************************************************
ok: [ya_cloud_vm]
 
TASK [docker : include_tasks] **************************************************
included: /home/ren/labs/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for ya_cloud_vm
 
TASK [docker : Install Docker Compose] *****************************************
ok: [ya_cloud_vm]
 
TASK [docker : Configure Docker security settings] *****************************
ok: [ya_cloud_vm]
 
TASK [docker : Enable Docker service to start on boot] *************************
ok: [ya_cloud_vm]
 
TASK [docker : Add current user to docker group] *******************************
ok: [ya_cloud_vm]
 
TASK [../../../roles/go_web_app : include_tasks] *******************************
included: /home/ren/labs/S25-core-course-labs/ansible/roles/go_web_app/tasks/0-wipe.yml for ya_cloud_vm
 
TASK [../../../roles/go_web_app : Stop and Remove container] *******************
ok: [ya_cloud_vm]
 
TASK [../../../roles/go_web_app : Remove Image] ********************************
changed: [ya_cloud_vm]
 
TASK [../../../roles/go_web_app : Pull Docker Image] ***************************
changed: [ya_cloud_vm]
 
TASK [../../../roles/go_web_app : Created Directory] ***************************
ok: [ya_cloud_vm]
 
TASK [../../../roles/go_web_app : Copy Compose Template] ***********************
ok: [ya_cloud_vm]
 
TASK [../../../roles/go_web_app : Deploy Via Compose] **************************
changed: [ya_cloud_vm]
 
PLAY RECAP *********************************************************************
ya_cloud_vm                : ok=18   changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Results

- Deployed via ansible applications can be accessed via the links:
  - [Go Web App](http://158.160.143.18:8080)
  - [Python Web App](http://158.160.143.18:8000)