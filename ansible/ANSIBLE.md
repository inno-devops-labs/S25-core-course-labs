ansible-playbook playbooks/dev/main.yaml --diff

```
PLAY [Deploy Docker on Cloud VM] ***********************************************

TASK [Gathering Facts] *********************************************************
ok: [my_cloud_vm]

TASK [docker : Install required packages] **************************************
ok: [my_cloud_vm]

TASK [docker : Add Docker GPG key] *********************************************
ok: [my_cloud_vm]

TASK [docker : Add Docker repository] ******************************************
ok: [my_cloud_vm]

TASK [docker : Update apt cache again] *****************************************
changed: [my_cloud_vm]

TASK [docker : Install Docker CE] **********************************************
ok: [my_cloud_vm]

TASK [docker : Download Docker Compose] ****************************************
ok: [my_cloud_vm]

PLAY RECAP *********************************************************************
my_cloud_vm                : ok=7    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

```



ansible-inventory -i playbooks/inventory/default_aws_ec2.yml.yaml --list | tee -a ANSIBLE.md

```
{
    "_meta": {
        "hostvars": {
            "my_cloud_vm": {
                "ansible_host": "89.169.173.97",
                "ansible_ssh_private_key_file": "/home/a/.ssh/id_rsa",
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
            "my_cloud_vm"
        ]
    }
}

```
