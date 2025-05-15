# Ansible

- Installing the existing Ansible docker role:

```bash
ansible-galaxy role install geerlingguy.docker
Starting galaxy role install process
- downloading role 'docker', owned by geerlingguy
- downloading role from https://github.com/geerlingguy/ansible-role-docker/archive/7.4.7.tar.gz
- extracting geerlingguy.docker to /Users/daniilzimin/.ansible/roles/geerlingguy.docker
- geerlingguy.docker (7.4.7) was installed successfully
```

- Running the playbook

```bash
ansible-playbook playbooks/dev/main.yaml

PLAY [Install and Configure Docker] ************************************************************************************

TASK [Gathering Facts] *************************************************************************************************
ok: [my_server]

TASK [docker : Install prerequisites for Docker] ***********************************************************************
ok: [my_server]

TASK [docker : Add Docker's official GPG key] **************************************************************************
ok: [my_server]

TASK [docker : Set up the Docker repository] ***************************************************************************
ok: [my_server]

TASK [docker : Install Docker CE] **************************************************************************************
ok: [my_server]

TASK [docker : Download Docker Compose] ********************************************************************************
ok: [my_server]

TASK [docker : Enable and start Docker] ********************************************************************************
ok: [my_server]

TASK [docker : Add user to docker group] *******************************************************************************
ok: [my_server]

PLAY RECAP *************************************************************************************************************
my_server                  : ok=8    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

- Inventory

```bash
ansible-inventory -i inventory/default_aws_ec2.yml --list
{
    "_meta": {
        "hostvars": {
            "master_vm": {
                "ansible_host": "92.118.169.53",
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
            "my_server"
        ]
    }
}
```

- Inventory graph

```bash
ansible-inventory -i inventory/default_aws_ec2.yml --graph
@all:
  |--@ungrouped:
  |  |--my_server
```