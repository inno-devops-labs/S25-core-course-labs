# Ansible and Docker Deployment 
> Deploying Docker on a newly created cloud VM with Ansible.

## Deployment output

> Last 50 lines of the ouputs form the deployement command, obtained using `ansible-playbook <path_to your_playbook> --diff` command.

```sh
dew@dew:~/ansible$ ansible-playbook playbooks/dev/main.yaml --diff

TASK [Gathering Facts] *************************************************************************************************
ok: [server]

TASK [docker : include_tasks] ******************************************************************************************
included: /home/dew/ansible/roles/docker/tasks/install_docker.yaml for server

TASK [docker : Install packages] ***************************************************************************************
The following NEW packages will be installed:
  apt-transport-https
0 upgraded, 1 newly installed, 0 to remove and 15 not upgraded.
changed: [server]

TASK [docker : Add GPG key] ********************************************************************************************
changed: [server]

TASK [docker : Add repository] *****************************************************************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/download_docker_com_linux_ubuntu.list
@@ -0,0 +1 @@
+deb [arch=amd64] https://download.docker.com/linux/ubuntu jammy stable

changed: [server]

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
changed: [server]

TASK [docker : Enable service] *****************************************************************************************
ok: [server]

TASK [docker : Add user to group] **************************************************************************************
changed: [server]

TASK [docker : include_tasks] ******************************************************************************************
included: /home/gotterkiller/ansible/roles/docker/tasks/install_compose.yaml for server

TASK [docker : Install Docker Compose] *********************************************************************************
changed: [server]

PLAY RECAP *************************************************************************************************************
vm-lab4                    : ok=10   changed=6    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Inventory details

```sh
dew@dew:~/ansible$ ansible-inventory -i inventory/yandex_cloud.yml --list
{
    "_meta": {
        "hostvars": {
            "server": {
                "ansible_host": "158.160.36.151",
                "ansible_user": "dew1769"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "web_servers"
        ]
    },
    "web_servers": {
        "hosts": [
            "server"
        ]
    }
}
```


## Lab 6

Output for docker and web_app

dew@dew:~/ansible$ ansible-playbook playbooks/dev/main.yaml -i inventory/default_yc.yaml

PLAY [Deploy] ************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************
ok: [server]

TASK [docker : include_tasks] ******************************************************************************************
included: /home/gotterkiller/ansible/roles/docker/tasks/install_docker.yaml for vm-lab4

TASK [docker : Install packages] ***************************************************************************************
ok: [server]

TASK [docker : Add GPG key] ********************************************************************************************
ok: [server]

TASK [docker : Add repository] *****************************************************************************************
ok: [server]

TASK [docker : Install] ************************************************************************************************
ok: [server]

TASK [docker : Enable service] *****************************************************************************************
ok: [server]

TASK [docker : Add user to group] **************************************************************************************
ok: [server]

TASK [docker : include_tasks] ******************************************************************************************
included: /home/dew/ansible/roles/docker/tasks/install_compose.yaml for server

TASK [docker : Install Docker Compose] *********************************************************************************
ok: [server]

TASK [web_app : Pull Docker image] *************************************************************************************
changed: [server]

TASK [web_app : Render docker-compose file] ****************************************************************************
changed: [server]

TASK [web_app : Start application container using docker-compose] ******************************************************
changed: [server]

TASK [web_app : Wipe Application Deployment] ***************************************************************************
skipping: [server]

PLAY RECAP *************************************************************************************************************
server                    : ok=13   changed=3    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0

## Best practices
- Modules are responsible for one simple & small task.
- Every task has a meaningful name, empty lines are used for readability 
- Usage of recommended directory structure. 