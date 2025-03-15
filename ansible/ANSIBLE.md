# Ansible Setup

This document describes the steps to install and configure ansible on a local machine and use it to provision
an Yandex Cloud instance with Docker and Docker Compose.

## Best Practices

### Descriptive task names

- **Clear and descriptive task names**:  
  Every task in the playbook is given a clear, descriptive name. This enhances the playbook’s readability, making it
  easier for developers to understand the purpose of each task. It also simplifies debugging when reviewing logs or
  output during execution.

### Pre-Execution validation

- **Dry-Run execution**:  
  Before executing the playbook, it was run in dry-run mode using the `--check` flag to simulate the changes without
  applying them. This ensures no unintended changes are made to the environment.

- **Syntax check**:  
  The playbook's syntax was validated using the `--syntax-check` flag to ensure there were no errors before deployment.
  This step helps catch potential mistakes in the playbook's structure early.

### Use of handlers

- **Handlers for conditional actions**:  
  Handlers were employed to restart services like Docker only when necessary. This avoids unnecessary service
  interruptions, reduces downtime, and optimizes resource usage by ensuring that actions like restarting Docker are
  triggered only if the configuration changes.

### Secure docker configuration

- **Enhances Docker security**:  
  By copying a new `/etc/docker/daemon.json` file with `"no-new-privileges": true`, preventing processes from gaining
  additional privileges,
  and `"userns-remap": "default"`, isolating users within containers to restrict their access to the host system. It
  sets ownership to root, with `0644` permissions, ensuring only root can modify it. The task triggers a Docker restart
  via notify: Restart Docker to apply changes, reducing security risks by restricting privilege escalation inside
  containers.

## Deployment Output

### **📌 Dry Run (Check):**

```bash
> ansible-playbook -i ansible/inventory/default_yandex_cloud.yml ansible/playbooks/dev/main.yml --check
```

### **📋 Output:**

```bash
PLAY [Deploy Docker on Yandex Cloud VM] ****************************************

TASK [Gathering Facts] *********************************************************
ok: [yandex_instance_1]

TASK [docker : Update apt package index] ***************************************
changed: [yandex_instance_1]

TASK [docker : Install dependencies] *******************************************
changed: [yandex_instance_1] => (item=apt-transport-https)
ok: [yandex_instance_1] => (item=ca-certificates)
ok: [yandex_instance_1] => (item=curl)
changed: [yandex_instance_1] => (item=gnupg-agent)
ok: [yandex_instance_1] => (item=software-properties-common)

TASK [docker : Add Docker GPG key] *********************************************
changed: [yandex_instance_1]...


TASK [geerlingguy.docker : Get docker group info using getent.] ****************
skipping: [yandex_instance_1]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] ***
skipping: [yandex_instance_1]

TASK [geerlingguy.docker : include_tasks] **************************************
skipping: [yandex_instance_1]

PLAY RECAP *********************************************************************
yandex_instance_1          : ok=14   changed=3    unreachable=0    failed=0
   skipped=11   rescued=0    ignored=3
```

### **📌 Command:**

```bash
> ansible-playbook -i ansible/inventory/default_yandex_cloud.yml ansible/playbooks/dev/main.yml --diff
```

### **📋 Output:**

```bash
PLAY [Deploy Docker on Yandex Cloud VM] ****************************************

TASK [Gathering Facts] *********************************************************
ok: [yandex_instance_1]

TASK [geerlingguy.docker : Load OS-specific vars.] *****************************
ok: [yandex_instance_1]

TASK [geerlingguy.docker : include_tasks] **************************************
skipping: [yandex_instance_1]

TASK [geerlingguy.docker : include_tasks] **************************************
included: /mnt/c/Users/Vladi/PycharmProjects/S25-core-course-labs/ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for yandex_instance_1

TASK [geerlingguy.docker : Ensure apt key is not present in trusted.gpg.d] *****
ok: [yandex_instance_1]

TASK [geerlingguy.docker : Ensure old apt source list is not present in /etc/apt/sources.list.d] ***
ok: [yandex_instance_1]

TASK [geerlingguy.docker : Ensure the repo referencing the previous trusted.gpg.d key is not present] ***
ok: [yandex_instance_1]

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] ***
ok: [yandex_instance_1]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] ***
skipping: [yandex_instance_1]

TASK [geerlingguy.docker : Add Docker repository.] *****************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/docker.list
@@ -0,0 +1 @@
+deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu noble stable

changed: [yandex_instance_1]

TASK [geerlingguy.docker : Install Docker packages.] ***************************
skipping: [yandex_instance_1]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] ***
The following additional packages will be installed:
  docker-compose-plugin libltdl7 libslirp0 pigz slirp4netns
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite
The following NEW packages will be installed:
  containerd.io docker-buildx-plugin docker-ce docker-ce-cli
  docker-ce-rootless-extras docker-compose-plugin libltdl7 libslirp0 pigz
  slirp4netns
0 upgraded, 10 newly installed, 0 to remove and 120 not upgraded.
changed: [yandex_instance_1]

....

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] ***
skipping: [yandex_instance_1]

TASK [geerlingguy.docker : include_tasks] **************************************
skipping: [yandex_instance_1]

PLAY RECAP *********************************************************************
yandex_instance_1          : ok=15   changed=5    unreachable=0    failed=0
   skipped=11   rescued=0    ignored=0
```

### **📌 Run Custom Playbook + BONUS:**

```bash
> ansible-playbook -i ansible/inventory/default_yandex_cloud.yml ansible/playbooks/dev/main.yml
```

### **📋 Output:**

```bash
PLAY [Deploy Docker on Yandex Cloud VM] ****************************************

TASK [Gathering Facts] *********************************************************
ok: [yandex_instance_1]

TASK [docker : Install Docker dependencies] ************************************
ok: [yandex_instance_1]

TASK [docker : Create keyrings directory] **************************************
ok: [yandex_instance_1]

TASK [docker : Add Docker's official GPG key] **********************************
ok: [yandex_instance_1]

TASK [docker : Set up the Docker repository] ***********************************
ok: [yandex_instance_1]

TASK [docker : Install Docker using official installation script] **************
ok: [yandex_instance_1]

TASK [docker : Download Docker Compose] ****************************************
changed: [yandex_instance_1]

TASK [docker : Verify installation] ********************************************
ok: [yandex_instance_1]

TASK [docker : Ensure docker group exists] *************************************
ok: [yandex_instance_1]

TASK [docker : Add current user to the docker group] ***************************
changed: [yandex_instance_1]

TASK [docker : Secure Docker Configuration - Disable Root Access] **************
changed: [yandex_instance_1]

RUNNING HANDLER [docker : Restart Docker] **************************************
changed: [yandex_instance_1]
```

### **❗ Check installation:**

```bash
user@HonorVladisLove:/mnt/c/...$ ssh ubuntu@89.169.158.227
```

### **📋 VM:**

```bash
> ubuntu@fhm7p44s09ksonkmg1n5:~$ docker --version
Docker version 27.5.1, build 9f9e405

> ubuntu@fhm7p44s09ksonkmg1n5:~$ docker-compose --version
Docker Compose version v2.32.4
```

### **📌 Command:**

```bash
> ansible-inventory -i ansible/inventory/default_yandex_cloud.yml --list
```

### **📋 Output:**

```bash
{
    "_meta": {
        "hostvars": {
            "yandex_instance_1": {
                "ansible_host": "89.169.158.227",
                "ansible_ssh_private_key_file": "~/.ssh/id_rsa",
                "ansible_user": "ubuntu"
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
            "yandex_instance_1"
        ]
    }
}
```

### **📌 Command:**

```bash
> ansible-inventory -i ansible/inventory/default_yandex_cloud.yml --graph
```

### **📋 Output:**

```bash
@all:
  |--@ungrouped:
  |  |--yandex_instance_1
```

## Lab 6 Output

### **📌 Command:**

```bash
> ansible-playbook -i ansible/inventory/default_yandex_cloud.yml ansible/playbooks/dev/app_python/main.yml
```

### **📋 Output:**

```text
PLAY [Deploying Python Moscow Time App] ****************************************

TASK [Gathering Facts] *********************************************************
ok: [yandex_instance_1]

TASK [docker : Install Docker dependencies] ************************************
ok: [yandex_instance_1]

TASK [docker : Create keyrings directory] **************************************
ok: [yandex_instance_1]

TASK [docker : Add Docker's official GPG key] **********************************
ok: [yandex_instance_1]

TASK [docker : Set up the Docker repository] ***********************************
ok: [yandex_instance_1]

TASK [docker : Install Docker using official installation script] **************
ok: [yandex_instance_1]

TASK [docker : Download Docker Compose] ****************************************
changed: [yandex_instance_1]

TASK [docker : Verify installation] ********************************************
ok: [yandex_instance_1]

TASK [docker : Ensure docker group exists] *************************************
ok: [yandex_instance_1]

TASK [docker : Add current user to the docker group] ***************************
ok: [yandex_instance_1]

TASK [docker : Secure Docker Configuration - Disable Root Access] **************
ok: [yandex_instance_1]

TASK [web_app : Deploying our application] *************************************
included: /mnt/c/Users/Vladi/PycharmProjects/S25-core-course-labs/ansible/roles/web_app/tasks/deploy_web_app.yml for yandex_instance_1

TASK [web_app : Pull Docker image] *********************************************
changed: [yandex_instance_1]

TASK [web_app : Start container] ***********************************************
changed: [yandex_instance_1]

TASK [web_app : Create directory for docker-compose file] **********************
changed: [yandex_instance_1]

TASK [web_app : Deploy docker-compose file] ************************************
changed: [yandex_instance_1]

TASK [web_app : Remove container] **********************************************
skipping: [yandex_instance_1]

TASK [web_app : Remove docker-compose file] ************************************
skipping: [yandex_instance_1]

PLAY RECAP *********************************************************************
yandex_instance_1          : ok=16   changed=5    unreachable=0    failed=0
   skipped=2    rescued=0    ignored=0
```


### **📌 Command:**

```bash
> ansible-playbook -i ansible/inventory/default_yandex_cloud.yml ansible/playbooks/dev/app_javascript/main.yml
```

### **📋 Output:**

```text
PLAY [Deploying Javascript App] ************************************************

TASK [Gathering Facts] *********************************************************
ok: [yandex_instance_1]

TASK [docker : Install Docker dependencies] ************************************
ok: [yandex_instance_1]

TASK [docker : Create keyrings directory] **************************************
ok: [yandex_instance_1]

TASK [docker : Add Docker's official GPG key] **********************************
ok: [yandex_instance_1]

TASK [docker : Set up the Docker repository] ***********************************
ok: [yandex_instance_1]

TASK [docker : Install Docker using official installation script] **************
ok: [yandex_instance_1]

TASK [docker : Download Docker Compose] ****************************************
ok: [yandex_instance_1]

TASK [docker : Verify installation] ********************************************
ok: [yandex_instance_1]

TASK [docker : Ensure docker group exists] *************************************
ok: [yandex_instance_1]

TASK [docker : Add current user to the docker group] ***************************
ok: [yandex_instance_1]

TASK [docker : Secure Docker Configuration - Disable Root Access] **************
ok: [yandex_instance_1]

TASK [web_app : Deploying our application] *************************************
included: /mnt/c/Users/Vladi/PycharmProjects/S25-core-course-labs/ansible/roles/web_app/tasks/deploy_web_app.yml for yandex_instance_1

TASK [web_app : Pull Docker image] *********************************************
changed: [yandex_instance_1]

TASK [web_app : Start container] ***********************************************
changed: [yandex_instance_1]

TASK [web_app : Create directory for docker-compose file] **********************
ok: [yandex_instance_1]

TASK [web_app : Deploy docker-compose file] ************************************
changed: [yandex_instance_1]

TASK [web_app : Remove container] **********************************************
skipping: [yandex_instance_1]

TASK [web_app : Remove docker-compose file] ************************************
skipping: [yandex_instance_1]

PLAY RECAP *********************************************************************
yandex_instance_1          : ok=16   changed=3    unreachable=0    failed=0
   skipped=2    rescued=0    ignored=0
```


### **❗ Check installation:**

```bash
user@HonorVladisLove:/mnt/c/...$ ssh -i ~/.ssh/id_rsa ubuntu@89.169.155.240
```

### **📋 VM:**

```bash
> ubuntu@fhm7p44s09ksonkmg1n5:~$ docker --version
Docker version 27.5.1, build 9f9e405

> ubuntu@fhm7p44s09ksonkmg1n5:~$ docker ps
CONTAINER ID   IMAGE                    COMMAND                  CREATED       STATUS       PORTS                    NAMES
d1503e15b22e   vladis7love/app_js       "docker-entrypoint.s…"   1 hours ago   Up 1 hours   0.0.0.0:8080->8080/tcp   js_webapp
f29adb752697   vladis7love/app_python   "python -m flask run…"   1 hours ago   Up 1 hours   0.0.0.0:5000->5000/tcp   python_webapp

> ubuntu@fhm7p44s09ksonkmg1n5:~$ curl http://localhost:5000
<h1>Current Time in Moscow: 2025-02-14 15:37:33</h1>
```
