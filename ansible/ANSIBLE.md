# Ansible

 Output of `ansible-playbook -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/main.yaml -K`:

```bash
BECOME password:

PLAY [Deploy Docker] ***************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************
ok: [45.142.122.102]

TASK [docker : Install Docker dependencies] ****************************************************************************
ok: [45.142.122.102]

TASK [docker : Add Docker GPG key] *************************************************************************************
changed: [45.142.122.102]

TASK [docker : Add Docker repository] **********************************************************************************
changed: [45.142.122.102]

TASK [docker : Install Docker] *****************************************************************************************
changed: [45.142.122.102]

TASK [docker : Add user to Docker group] *******************************************************************************
changed: [45.142.122.102]

TASK [docker : Download Docker Compose] ********************************************************************************
changed: [45.142.122.102]

TASK [docker : Verify Docker Compose installation] *********************************************************************
changed: [45.142.122.102]

PLAY RECAP *************************************************************************************************************
45.142.122.102             : ok=8    changed=6    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

Output of `ansible-inventory -i ansible/inventory/default_aws_ec2.yml --list`:

```bash
{
    "_meta": {
        "hostvars": {
            "45.142.122.102": {
                "ansible_ssh_private_key_file": "/root/.ssh/authtorized_keys/id_rsa_devops",
                "ansible_user": "venom"
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
            "45.142.122.102"
        ]
    }
}
```

Output of `ansible-inventory -i ansible/inventory/default_aws_ec2.yml --graph`:

```bash
@all:
  |--@ungrouped:
  |  |--45.142.122.102
```

## Lab6

Output for command `ansible-playbook -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/main.yaml -K`

```bash
BECOME password:

PLAY [Deploy Docker] ***********************************************************

TASK [Gathering Facts] *********************************************************
ok: [45.142.122.102]

TASK [docker : Install Docker dependencies] ************************************
ok: [45.142.122.102]

TASK [docker : Add Docker GPG key] *********************************************
ok: [45.142.122.102]

TASK [docker : Add Docker repository] ******************************************
ok: [45.142.122.102]

TASK [docker : Install Docker] *************************************************
ok: [45.142.122.102]

TASK [docker : Add user to Docker group] ***************************************
ok: [45.142.122.102]

TASK [docker : Download Docker Compose] ****************************************
ok: [45.142.122.102]

TASK [docker : Verify Docker Compose installation] *****************************
changed: [45.142.122.102]

TASK [web_app : Pull Docker image] *********************************************
ok: [45.142.122.102]

TASK [web_app : Deploy Docker Compose file] ************************************
ok: [45.142.122.102]

TASK [web_app : Start Docker container] ****************************************
changed: [45.142.122.102]

TASK [web_app : Wipe Docker environment] ***************************************
included: /root/S25-core-course-labs/ansible/roles/web_app/tasks/0-wipe.yml for 45.142.122.102

TASK [web_app : Remove Docker container] ***************************************
skipping: [45.142.122.102]

TASK [web_app : Remove Docker image] *******************************************
skipping: [45.142.122.102]

PLAY RECAP *********************************************************************
45.142.122.102             : ok=12   changed=2    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0
```
