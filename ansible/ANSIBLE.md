
# Ansible

I used Yandex Cloud VM to complete the tasks.

## Playbook and Testing

```bash

(dev) deedjei@deedjei:~/Desktop/devops/S25-core-course-labs$ ansible-playbook -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/main.yaml --diff

PLAY [Install Docker and Docker Compose] ***********************************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************************************
[WARNING]: Platform linux on host docker_host is using the discovered Python interpreter at /usr/bin/python3.12, but future installation of another Python
interpreter could change the meaning of that path. See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more
information.
ok: [docker_host]

TASK [../../roles/docker : Include Docker installation tasks] **************************************************************************************************
included: /home/deedjei/Desktop/devops/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for docker_host

TASK [../../roles/docker : Remove Docker packages] *************************************************************************************************************
ok: [docker_host] => (item=docker)
ok: [docker_host] => (item=docker-engine)
ok: [docker_host] => (item=docker.io)
ok: [docker_host] => (item=containerd)
ok: [docker_host] => (item=runc)

TASK [../../roles/docker : Remove Docker repositories] *********************************************************************************************************
ok: [docker_host] => (item=/etc/apt/sources.list.d/docker.list)
ok: [docker_host] => (item=/etc/apt/sources.list.d/docker.list.save)
ok: [docker_host] => (item=/etc/apt/sources.list.d/docker-ce.list)
ok: [docker_host] => (item=/etc/apt/sources.list.d/docker-ce.list.save)

TASK [../../roles/docker : Remove Docker GPG keys] *************************************************************************************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
     "path": "/etc/apt/keyrings/docker.asc",
-    "state": "file"
+    "state": "absent"
 }

changed: [docker_host] => (item=/etc/apt/keyrings/docker.asc)
ok: [docker_host] => (item=/usr/share/keyrings/docker-archive-keyring.gpg)

TASK [../../roles/docker : Clean apt cache] ********************************************************************************************************************
changed: [docker_host]

TASK [../../roles/docker : Install prerequisites] **************************************************************************************************************
ok: [docker_host]

TASK [../../roles/docker : Create Docker keyring directory] ****************************************************************************************************
ok: [docker_host]

TASK [../../roles/docker : Add Docker GPG key] *****************************************************************************************************************
changed: [docker_host]

TASK [../../roles/docker : Add Docker repository] **************************************************************************************************************
ok: [docker_host]

TASK [../../roles/docker : Install Docker components] **********************************************************************************************************
ok: [docker_host]

TASK [../../roles/docker : Start and enable Docker service] ****************************************************************************************************
ok: [docker_host]

TASK [../../roles/docker : Add current user to docker group] ***************************************************************************************************
ok: [docker_host]

TASK [../../roles/docker : Include Docker Compose installation tasks] ******************************************************************************************
included: /home/deedjei/Desktop/devops/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for docker_host

TASK [../../roles/docker : Download Docker Compose] ************************************************************************************************************
ok: [docker_host]

PLAY RECAP *****************************************************************************************************************************************************
docker_host                : ok=15   changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```
#### ansible-inventory -i ansible/inventory/default_aws_ec2.yml --list

```bash
(dev) deedjei@deedjei:~/Desktop/devops/S25-core-course-labs$ ansible-inventory -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/main.yaml --list
{
    "_meta": {
        "hostvars": {
            "docker_host": {
                "ansible_host": "158.160.56.43",
                "ansible_ssh_private_key_file": "~/.ssh/id_ed25519",
                "ansible_user": "deedjei"
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
            "docker_host"
        ]
    }
}
```

## Installed Docker && Docker compose 
```bash
deedjei@compute-vm-2-2-20-hdd-1739598294518:~$ docker --version && docker compose version
Docker version 27.5.1, build 9f9e405
Docker Compose version v2.32.4

```

## Lab 6: Ansible and Docker Deployment

`ansible-playbook playbooks/dev/app_python/main.yml`
```bash
(dev) deedjei@deedjei:~/Desktop/devops/S25-core-course-labs/ansible$ ansible-playbook playbooks/dev/app_python/main.yml

PLAY [Deploy Python Web App] *****************************************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************************************************
[WARNING]: Platform linux on host docker_host is using the discovered Python interpreter at /usr/bin/python3.12, but future installation of another
Python interpreter could change the meaning of that path. See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html
for more information.
ok: [docker_host]

TASK [docker : Include Docker installation tasks] ********************************************************************************************************
included: /home/deedjei/Desktop/devops/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for docker_host

TASK [docker : Remove Docker packages] *******************************************************************************************************************
ok: [docker_host] => (item=docker)
ok: [docker_host] => (item=docker-engine)
ok: [docker_host] => (item=docker.io)
ok: [docker_host] => (item=containerd)
ok: [docker_host] => (item=runc)

TASK [docker : Remove Docker repositories] ***************************************************************************************************************
ok: [docker_host] => (item=/etc/apt/sources.list.d/docker.list)
ok: [docker_host] => (item=/etc/apt/sources.list.d/docker.list.save)
ok: [docker_host] => (item=/etc/apt/sources.list.d/docker-ce.list)
ok: [docker_host] => (item=/etc/apt/sources.list.d/docker-ce.list.save)

TASK [docker : Remove Docker GPG keys] *******************************************************************************************************************
changed: [docker_host] => (item=/etc/apt/keyrings/docker.asc)
ok: [docker_host] => (item=/usr/share/keyrings/docker-archive-keyring.gpg)

TASK [docker : Clean apt cache] **************************************************************************************************************************
ok: [docker_host]

TASK [docker : Install prerequisites] ********************************************************************************************************************
ok: [docker_host]

TASK [docker : Create Docker keyring directory] **********************************************************************************************************
ok: [docker_host]

TASK [docker : Add Docker GPG key] ***********************************************************************************************************************
changed: [docker_host]

TASK [docker : Add Docker repository] ********************************************************************************************************************
ok: [docker_host]

TASK [docker : Install Docker components] ****************************************************************************************************************
ok: [docker_host]

TASK [docker : Start and enable Docker service] **********************************************************************************************************
ok: [docker_host]

TASK [docker : Add current user to docker group] *********************************************************************************************************
ok: [docker_host]

TASK [docker : Include Docker Compose installation tasks] ************************************************************************************************
included: /home/deedjei/Desktop/devops/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for docker_host

TASK [docker : Download Docker Compose] ******************************************************************************************************************
ok: [docker_host]

TASK [web_app : Pull Docker image] ***********************************************************************************************************************
ok: [docker_host]

TASK [web_app : Start the web app container] *************************************************************************************************************
ok: [docker_host]

TASK [web_app : Create directory for docker-compose file] ************************************************************************************************
ok: [docker_host]

TASK [web_app : Deploy docker-compose file] **************************************************************************************************************
changed: [docker_host]

TASK [web_app : Remove container] ************************************************************************************************************************
skipping: [docker_host]

TASK [web_app : Remove docker-compose file] **************************************************************************************************************
skipping: [docker_host]

PLAY RECAP ***********************************************************************************************************************************************
docker_host                : ok=19   changed=3    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0
```