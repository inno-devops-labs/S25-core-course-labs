# Ansible related work

During this stage of homework I fully followed task requirements about project's structure, files' names and the idea in general.

Also to work with Ansible I had to install WSL, thus there were some errors related to the fact that all the previous steps were done on my Windows machine, including authorization in services and all te settings.

Here are some commands I used.

## Executing playbook to deploy the Docker role

```bash
liza@LAPTOP-T7RS5DP1:/mnt/c/Users/Elizoveta/Desktop/S25-core-course-labs/ansible$ ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yml

[WARNING]: Ansible is being run in a world writable directory (/mnt/c/Users/Elizoveta/Desktop/S25-core-course-
labs/ansible), ignoring it as an ansible.cfg source. For more information see
https://docs.ansible.com/ansible/devel/reference_appendices/config.html#cfg-in-world-writable-dir

PLAY [Docker VM] *******************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************
fatal: [host_01]: UNREACHABLE! => {"changed": false, "msg": "Failed to connect to the host via ssh: no such identity: /home/liza/.ssh/id_ed25519_neww.pub: No such file or directory\r\nubuntu@158.160.57.28: Permission denied (publickey,password).", "unreachable": true}

PLAY RECAP *************************************************************************************************************
host_01                    : ok=0    changed=0    unreachable=1    failed=0    skipped=0    rescued=0    ignored=0
```

I could not manage to resolve this error because I followed lecture slides and lectures' ideas, so my guess is that there is some problem with transfering from Windows to WSL. When I tried to connect to VM from WSL I was asked for the password but I did not set any passwords. I tried to reset the password but it did not help: the command was performing for so long with no result.

## Inventory Details

```bash
liza@LAPTOP-T7RS5DP1:/mnt/c/Users/Elizoveta/Desktop/S25-core-course-labs/ansible$ ansible-inventory -i inventory/default_aws_ec2.yml --list
[WARNING]: Ansible is being run in a world writable directory (/mnt/c/Users/Elizoveta/Desktop/S25-core-course-
labs/ansible), ignoring it as an ansible.cfg source. For more information see
https://docs.ansible.com/ansible/devel/reference_appendices/config.html#cfg-in-world-writable-dir
{
    "_meta": {
        "hostvars": {
            "host_01": {
                "ansible_host": "158.160.57.28",
                "ansible_ssh_private_key_file": "~/.ssh/id_ed25519_neww.pub",
                "ansible_user": "ubuntu"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "myhosts"
        ]
    },
    "myhosts": {
        "hosts": [
            "host_01"
        ]
    }
}

liza@LAPTOP-T7RS5DP1:/mnt/c/Users/Elizoveta/Desktop/S25-core-course-labs/ansible$ ansible-inventory -i inventory/default_aws_ec2.yml --graph
[WARNING]: Ansible is being run in a world writable directory (/mnt/c/Users/Elizoveta/Desktop/S25-core-course-
labs/ansible), ignoring it as an ansible.cfg source. For more information see
https://docs.ansible.com/ansible/devel/reference_appendices/config.html#cfg-in-world-writable-dir
@all:
  |--@ungrouped:
  |--@myhosts:
  |  |--host_01
```
