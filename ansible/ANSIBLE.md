# Ansible Docs

## Check connection to server(s)
To check is connection to server for deploy successful, let's run following command
```sh
ansible -i ansible/inventory/default_aws_ec2.yml all -m ping
```
Output:
```
vm | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```

---

## Running the Playbook
To execute the playbook, run:
```sh
ansible-playbook -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/main.yaml -K
```

```
PLAY [Deploy Docker] **************************************************************************

TASK [Gathering Facts] ************************************************************************
ok: [vm]

TASK [docker : Include installation tasks] ****************************************************
included: /home/ivans/for vs code/DevOps/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for vm

TASK [docker : Install required system packages] **********************************************
ok: [vm]

TASK [docker : Add Docker official GPG key] ***************************************************
ok: [vm]

TASK [docker : Set up the Docker stable repository] *******************************************
ok: [vm]

TASK [docker : Install Docker CE, CLI, and containerd] ****************************************
ok: [vm]

TASK [docker : Start and enable Docker service] ***********************************************
ok: [vm]

TASK [docker : Add user to Docker group] ******************************************************
ok: [vm]

TASK [docker : Include Docker Compose tasks] **************************************************
included: /home/ivans/for vs code/DevOps/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for vm

TASK [docker : Download Docker Compose] *******************************************************
changed: [vm]

TASK [docker : Verify Docker Compose installation] ********************************************
ok: [vm]

TASK [docker : debug] *************************************************************************
ok: [vm] => {
    "msg": "Docker Compose version: Docker Compose version v2.33.0"
}

PLAY RECAP ************************************************************************************
vm                         : ok=12   changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

```

## Output `nsible-inventory --list`
```
{
    "_meta": {
        "hostvars": {
            "vm": {
                "ansible_host": "89.169.154.202",
                "ansible_python_interpreter": "/usr/bin/python3",
                "ansible_ssh_private_key_file": "~/.ssh/id_ed25519",
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
            "vm"
        ]
    }
}
```

## Output of `ansible-inventory --graph`
```
@all:
  |--@ungrouped:
  |  |--vm
```

## Running the Playbook with web-app
```sh
ansible-playbook -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/main.yaml -K
```

```
PLAY [Deploy Docker] **************************************************************************

TASK [Gathering Facts] ************************************************************************
ok: [vm]

TASK [docker : Include installation tasks] ****************************************************
included: /home/ivans/for vs code/DevOps/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for vm

TASK [docker : Install required system packages] **********************************************
ok: [vm]

TASK [docker : Add Docker official GPG key] ***************************************************
ok: [vm]

TASK [docker : Set up the Docker stable repository] *******************************************
ok: [vm]

TASK [docker : Install Docker CE, CLI, and containerd] ****************************************
ok: [vm]

TASK [docker : Start and enable Docker service] ***********************************************
ok: [vm]

TASK [docker : Add user to Docker group] ******************************************************
ok: [vm]

TASK [docker : Include Docker Compose tasks] **************************************************
included: /home/ivans/for vs code/DevOps/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for vm

TASK [docker : Download Docker Compose] *******************************************************
ok: [vm]

TASK [docker : Verify Docker Compose installation] ********************************************
ok: [vm]

TASK [docker : debug] *************************************************************************
ok: [vm] => {
    "msg": "Docker Compose version: Docker Compose version v2.33.0"
}

TASK [web_app : Create Docker network] ********************************************************
ok: [vm]

TASK [web_app : Deploy application using Docker Compose] **************************************
ok: [vm]

TASK [web_app : Start application with Docker Compose] ****************************************
changed: [vm]

PLAY RECAP ************************************************************************************
vm                         : ok=15   changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 
```

## `ansible-playbook ansible/playbooks/dev/main.yaml --tags wipe`
```
PLAY [Deploy Web Application] *****************************************************************

TASK [Gathering Facts] ************************************************************************
ok: [vm]

PLAY [Wipe Web Application] *******************************************************************

TASK [Gathering Facts] ************************************************************************
ok: [vm]

TASK [Remove Docker container] ****************************************************************
skipping: [vm]

TASK [Remove Docker image] ********************************************************************
skipping: [vm]

TASK [Remove Docker volumes] ******************************************************************
skipping: [vm]

PLAY RECAP ************************************************************************************
vm                         : ok=2    changed=0    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0   
```
