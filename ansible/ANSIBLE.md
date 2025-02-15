## File Breakdown

### 1. **Inventory File: `ansible/inventory/default_aws_ec2.yml`**

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
- name: Add Docker's GPG key
  apt_key:
    url: https://download.docker.com/linux/ubuntu/gpg
    state: present

- name: Set up the repository
  apt_repository:
    repo: "deb [arch=amd64] https://download.docker.com/linux/ubuntu {{ ansible_distribution_release | lower }} stable"
    state: present
    update_cache: yes

- name: Install Docker
  apt:
    name: "docker-ce={{ docker_version }}"
    state: present
    force: yes
    update_cache: yes
```

---

### 7. **Main Docker Role Tasks: `ansible/roles/docker/tasks/main.yml`**

This is the main task file for the Docker role. It installs necessary dependencies, includes the tasks to install Docker and Docker Compose, enables Docker to start on boot, and adds the current user to the Docker group.

Content:
```yaml
- name: Install packages
  apt:
    name:
      - apt-transport-https
      - ca-certificates
      - curl
      - software-properties-common
    state: present
    update_cache: yes

- include_tasks: install_docker.yml
- include_tasks: install_compose.yml

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

- **Explanation**: This task file manages package installations, Docker installation, Docker Compose installation, service management, and user group update. It ensures that Docker is set to start on boot and the user has the necessary permissions to run Docker without `sudo`.

---

## Running the Playbook

To run the playbook and verify the changes without applying them, used the following command:

```bash
ansible-playbook -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/customRole.yml --check --diff
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