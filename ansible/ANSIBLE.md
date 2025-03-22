# Ansible

## Installing the existing Ansible docker role

1. To install the Ansible Galaxy role for Docker, run the following command:

```bash
ansible-galaxy role install geerlingguy/.docker
```

Sample output:

```bash
Starting galaxy role install process
- downloading role 'docker', owned by geerlingguy
- downloading role from https://github.com/geerlingguy/ansible-role-docker/archive/7.4.5.tar.gz
- extracting geerlingguy.docker to /home/yoqub/Desktop/IU/Spring25/DevOps/S25-core-course-labs/ansible/roles/geerlingguy.docker
- geerlingguy.docker (7.4.5) was installed successfully
```

## Using the Existing Ansible Role for Docker

1. Set the Ansible configuration file environment variable:

```bash
export ANSIBLE_CONFIG=/mnt/c/devops/kubespray/ansible.cfg
```

2.Execute the playbook to install and configure Docker:

```bash
ansible-playbook playbooks/dev/main.yaml
```

Sample output:

```bash
PLAY [Install and Configure Docker] ********************************************************************************

TASK [Gathering Facts] *********************************************************************************************
ok: [master_vm]

TASK [docker : Install prerequisites for Docker] *******************************************************************
ok: [master_vm]

TASK [docker : Add Docker's official GPG key] **********************************************************************
ok: [master_vm]

TASK [docker : Set up the Docker repository] ***********************************************************************
ok: [master_vm]

TASK [docker : Install Docker CE] **********************************************************************************
ok: [master_vm]

TASK [docker : Download Docker Compose] ****************************************************************************
ok: [master_vm]

TASK [docker : Enable and start Docker] ****************************************************************************
ok: [master_vm]

TASK [docker : Add user to docker group] ***************************************************************************
ok: [master_vm]

PLAY RECAP *********************************************************************************************************
master_vm                  : ok=8    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

3.List the Ansible inventory to ensure the correct hosts are recognized:

```bash
ansible-inventory -i inventory/default_aws_ec2.yml --list
```

Sample output:

```bash
{
    "_meta": {
        "hostvars": {
            "master_vm": {
                "ansible_host": "89.169.157.38",
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
            "master_vm"
        ]
    }
}
```

4.To visualize the inventory hierarchy, use the following command:

```bash
ansible-inventory -i inventory/default_aws_ec2.yml --graph
```

Sample output:

```bash
@all:
  |--@ungrouped:
  |  |--master_vm
```

## Application Deployment with a new role

`ansible-playbook playbooks/dev/main.yaml`

```bash
PLAY [Install and Configure Docker, Run the Web App] **********************************************************

TASK [Gathering Facts] ****************************************************************************************
ok: [master_vm]

TASK [docker : Install prerequisites for Docker] **************************************************************
ok: [master_vm]

TASK [docker : Add Docker's official GPG key] *****************************************************************
ok: [master_vm]

TASK [docker : Set up the Docker repository] ******************************************************************
ok: [master_vm]

TASK [docker : Install Docker CE] *****************************************************************************
ok: [master_vm]

TASK [docker : Download Docker Compose] ***********************************************************************
ok: [master_vm]

TASK [docker : Enable and start Docker] ***********************************************************************
ok: [master_vm]

TASK [docker : Add user to docker group] **********************************************************************
ok: [master_vm]

TASK [web_app : Create application directory] *****************************************************************
ok: [master_vm]

TASK [web_app : Deploy Docker Compose template] ***************************************************************
ok: [master_vm]

TASK [web_app : Ensure Docker image is pulled] ****************************************************************
ok: [master_vm]

TASK [web_app : Run Python application container] *************************************************************
ok: [master_vm]

PLAY RECAP ****************************************************************************************************
master_vm                  : ok=12   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```
