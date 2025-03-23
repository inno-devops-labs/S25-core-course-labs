# Ansible

## Installing Existing Ansible Role for Docker:

```bash
ansible-galaxy role install geerlingguy.docker
Starting galaxy role install process
- downloading role 'docker', owned by geerlingguy
- downloading role from https://github.com/geerlingguy/ansible-role-docker/archive/7.4.5.tar.gz
- extracting geerlingguy.docker to /Users/emilgainullin/.ansible/roles/geerlingguy.docker
- geerlingguy.docker (7.4.5) was installed successfully

```

## Custom Docker Role

Exporting the config:
```bash
export ANSIBLE_CONFIG=/mnt/c/devops/kubespray/ansible.cfg
```

Running Playbook:
```bash
ansible-playbook playbooks/dev/main.yaml

PLAY [Install and Configure Docker] ********************************************************************************************************************************************

TASK [Gathering Facts] *********************************************************************************************************************************************************
The authenticity of host '158.160.51.157 (158.160.51.157)' can't be established.
ED25519 key fingerprint is SHA256:zrPb/XIZfPT2XnUkDLH6P8eY0/zIXhHEYo43iFcY49Q.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
ok: [master_vm]

TASK [docker : Install prerequisites for Docker] *******************************************************************************************************************************
changed: [master_vm]

TASK [docker : Add Docker's official GPG key] **********************************************************************************************************************************
changed: [master_vm]

TASK [docker : Set up the Docker repository] ***********************************************************************************************************************************
changed: [master_vm]

TASK [docker : Install Docker CE] **********************************************************************************************************************************************
changed: [master_vm]

TASK [docker : Download Docker Compose] ****************************************************************************************************************************************
changed: [master_vm]

TASK [docker : Enable and start Docker] ****************************************************************************************************************************************
ok: [master_vm]

TASK [docker : Add user to docker group] ***************************************************************************************************************************************
changed: [master_vm]

RUNNING HANDLER [docker : Restart Docker] **************************************************************************************************************************************
changed: [master_vm]

PLAY RECAP *********************************************************************************************************************************************************************
master_vm                  : ok=9    changed=7    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

```

Inventory:
```bash
 ansible-inventory -i inventory/default_aws_ec2.yml --list
{
    "_meta": {
        "hostvars": {
            "master_vm": {
                "ansible_host": "158.160.51.157",
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

Validating Inventory:
```bash
ansible-inventory -i inventory/default_aws_ec2.yml --graph
@all:
  |--@ungrouped:
  |  |--master_vm

```


## Application Deployment:

Running playbook:
```bash
ansible-playbook playbooks/dev/main.yaml

PLAY [Install and Configure Docker] ********************************************************************************************************************************************

TASK [Gathering Facts] *********************************************************************************************************************************************************
The authenticity of host '158.160.49.79 (158.160.49.79)' can't be established.
ED25519 key fingerprint is SHA256:p38wGqqq5k7oCusGm8CzDv+yipwXp0PGSZB8vsr3aN4.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
ok: [master_vm]

TASK [docker : Install prerequisites for Docker] *******************************************************************************************************************************
changed: [master_vm]

TASK [docker : Add Docker's official GPG key] **********************************************************************************************************************************
changed: [master_vm]

TASK [docker : Set up the Docker repository] ***********************************************************************************************************************************
changed: [master_vm]

TASK [docker : Install Docker CE] **********************************************************************************************************************************************
changed: [master_vm]

TASK [docker : Download Docker Compose] ****************************************************************************************************************************************
changed: [master_vm]

TASK [docker : Enable and start Docker] ****************************************************************************************************************************************
ok: [master_vm]

TASK [docker : Add user to docker group] ***************************************************************************************************************************************
changed: [master_vm]

TASK [web_app : Ensure Docker image is pulled] *********************************************************************************************************************************
changed: [master_vm]

TASK [web_app : Run Python application container] ******************************************************************************************************************************
[WARNING]: Docker warning: The requested image's platform (linux/arm64/v8) does not match the detected host platform (linux/amd64/v3) and no specific platform was requested
changed: [master_vm]

RUNNING HANDLER [docker : Restart Docker] **************************************************************************************************************************************
changed: [master_vm]

PLAY RECAP *********************************************************************************************************************************************************************
master_vm                  : ok=11   changed=9    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  
```

Final Playbook Run:
```bash
ansible-playbook playbooks/dev/main.yaml

PLAY [Install and Configure Docker] ********************************************************************************************************************************************

TASK [Gathering Facts] *********************************************************************************************************************************************************
ok: [master_vm]

TASK [docker : Install prerequisites for Docker] *******************************************************************************************************************************
ok: [master_vm]

TASK [docker : Add Docker's official GPG key] **********************************************************************************************************************************
ok: [master_vm]

TASK [docker : Set up the Docker repository] ***********************************************************************************************************************************
ok: [master_vm]

TASK [docker : Install Docker CE] **********************************************************************************************************************************************
ok: [master_vm]

TASK [docker : Download Docker Compose] ****************************************************************************************************************************************
ok: [master_vm]

TASK [docker : Enable and start Docker] ****************************************************************************************************************************************
ok: [master_vm]

TASK [docker : Add user to docker group] ***************************************************************************************************************************************
ok: [master_vm]

TASK [docker : Install prerequisites for Docker] *******************************************************************************************************************************
ok: [master_vm]

TASK [docker : Add Docker's official GPG key] **********************************************************************************************************************************
ok: [master_vm]

TASK [docker : Set up the Docker repository] ***********************************************************************************************************************************
ok: [master_vm]

TASK [docker : Install Docker CE] **********************************************************************************************************************************************
ok: [master_vm]

TASK [docker : Download Docker Compose] ****************************************************************************************************************************************
ok: [master_vm]

TASK [docker : Enable and start Docker] ****************************************************************************************************************************************
ok: [master_vm]

TASK [docker : Add user to docker group] ***************************************************************************************************************************************
ok: [master_vm]

TASK [web_app : Create application directory] **********************************************************************************************************************************
changed: [master_vm]

TASK [web_app : Deploy Docker Compose template] ********************************************************************************************************************************
changed: [master_vm]

TASK [web_app : Ensure Docker image is pulled] *********************************************************************************************************************************
ok: [master_vm]

TASK [web_app : Run Python application container] ******************************************************************************************************************************
ok: [master_vm]

PLAY RECAP *********************************************************************************************************************************************************************
master_vm                  : ok=19   changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

```