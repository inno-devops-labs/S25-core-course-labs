# Command 1

```bash
$ ansible-inventory -i ansible/inventory/default_aws_ec2.yml --list
{
    "_meta": {
        "hostvars": {
            "aws_ec2_instance": {
                "ansible_host": "16.170.163.135",
                "ansible_python_interpreter": "/usr/bin/python3",
                "ansible_ssh_private_key_file": "/workspaces/S25-core-course-labs/ansible-key.pem",
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
            "aws_ec2_instance"
        ]
    }
```

# Command 2

```bash
$ ansible-inventory -i ansible/inventory/default_aws_ec2.yml --graph
@all:
  |--@ungrouped:
  |  |--aws_ec2_instance
```


#Command 3

```bash
$ ansible-playbook -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/main.yaml --diff
PLAY [Install Docker using Ansible Role] **************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************
ok: [aws_instance]

TASK [docker : Install required packages] *************************************************************************************************
ok: [aws_instance]

TASK [docker : Add Docker GPG key] ********************************************************************************************************
ok: [aws_instance]

TASK [docker : Add Docker repository] *****************************************************************************************************
ok: [aws_instance]

TASK [docker : Install Docker] ************************************************************************************************************
changed: [aws_instance]

TASK [docker : Enable Docker service to start on boot] ************************************************************************************
ok: [aws_instance]

TASK [docker : Install Docker Compose] ****************************************************************************************************
changed: [aws_instance]

TASK [docker : Add user to Docker group] **************************************************************************************************
ok: [aws_instance]

PLAY RECAP ********************************************************************************************************************************
aws_instance               : ok=8    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```
