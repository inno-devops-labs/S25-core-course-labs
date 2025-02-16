## Custom role for installing Docker

<details>
<summary>Custom role testing</summary>
    
```bash
gotterkiller@GOTTERKILLER:~/ansible$ ansible-playbook playbooks/dev/main.yaml --diff

PLAY [Dev] *************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************
ok: [vm-lab4]

TASK [docker : include_tasks] ******************************************************************************************
included: /home/gotterkiller/ansible/roles/docker/tasks/install_docker.yaml for vm-lab4

TASK [docker : Install packages] ***************************************************************************************
The following NEW packages will be installed:
  apt-transport-https
0 upgraded, 1 newly installed, 0 to remove and 15 not upgraded.
changed: [vm-lab4]

TASK [docker : Add GPG key] ********************************************************************************************
changed: [vm-lab4]

TASK [docker : Add repository] *****************************************************************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/download_docker_com_linux_ubuntu.list
@@ -0,0 +1 @@
+deb [arch=amd64] https://download.docker.com/linux/ubuntu jammy stable

changed: [vm-lab4]

TASK [docker : Install] ************************************************************************************************
The following additional packages will be installed:
  containerd.io docker-buildx-plugin docker-ce-cli docker-ce-rootless-extras
  docker-compose-plugin libltdl7 libslirp0 pigz slirp4netns
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite
The following NEW packages will be installed:
  containerd.io docker-buildx-plugin docker-ce docker-ce-cli
  docker-ce-rootless-extras docker-compose-plugin libltdl7 libslirp0 pigz
  slirp4netns
0 upgraded, 10 newly installed, 0 to remove and 15 not upgraded.
changed: [vm-lab4]

TASK [docker : Enable service] *****************************************************************************************
ok: [vm-lab4]

TASK [docker : Add user to group] **************************************************************************************
changed: [vm-lab4]

TASK [docker : include_tasks] ******************************************************************************************
included: /home/gotterkiller/ansible/roles/docker/tasks/install_compose.yaml for vm-lab4

TASK [docker : Install Docker Compose] *********************************************************************************
changed: [vm-lab4]

PLAY RECAP *************************************************************************************************************
vm-lab4                    : ok=10   changed=6    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

</details>


## Ansible inventory

<details>

<summary>ansible-inventory -i inventory/default_yc.yaml --list</summary>

```bash
gotterkiller@GOTTERKILLER:~/ansible$ ansible-inventory -i inventory/default_yc.yaml --list
{
    "_meta": {
        "hostvars": {
            "vm-lab4": {
                "ansible_host": "158.160.157.133",
                "ansible_user": "niyaz-devops"
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
            "vm-lab4"
        ]
    }
```
</details>

## Ansible inventory graph

<details>

<summary>ansible-inventory -i inventory/default_yc.yaml --graph</summary>

```bash
gotterkiller@GOTTERKILLER:~/ansible$ ansible-inventory -i inventory/default_yc.yaml --graph
@all:
  |--@ungrouped:
  |  |--vm-lab4
```
</details>

<details>
    
<summary>ansible-playbook playbooks/dev/main.yaml -i inventory/default_yc.yaml</summary>

```bash
gotterkiller@GOTTERKILLER:~/ansible$ ansible-playbook playbooks/dev/main.yaml -i inventory/default_yc.yaml

PLAY [Flask-app deploy] ************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************
ok: [vm-lab4]

TASK [docker : include_tasks] ******************************************************************************************
included: /home/gotterkiller/ansible/roles/docker/tasks/install_docker.yaml for vm-lab4

TASK [docker : Install packages] ***************************************************************************************
ok: [vm-lab4]

TASK [docker : Add GPG key] ********************************************************************************************
ok: [vm-lab4]

TASK [docker : Add repository] *****************************************************************************************
ok: [vm-lab4]

TASK [docker : Install] ************************************************************************************************
ok: [vm-lab4]

TASK [docker : Enable service] *****************************************************************************************
ok: [vm-lab4]

TASK [docker : Add user to group] **************************************************************************************
ok: [vm-lab4]

TASK [docker : include_tasks] ******************************************************************************************
included: /home/gotterkiller/ansible/roles/docker/tasks/install_compose.yaml for vm-lab4

TASK [docker : Install Docker Compose] *********************************************************************************
ok: [vm-lab4]

TASK [web_app : Pull Docker image] *************************************************************************************
changed: [vm-lab4]

TASK [web_app : Render docker-compose file] ****************************************************************************
changed: [vm-lab4]

TASK [web_app : Start application container using docker-compose] ******************************************************
changed: [vm-lab4]

TASK [web_app : Wipe Application Deployment] ***************************************************************************
skipping: [vm-lab4]

PLAY RECAP *************************************************************************************************************
vm-lab4                    : ok=13   changed=3    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0

```
    
</details>