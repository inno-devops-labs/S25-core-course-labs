# Ansible Documentation

## Overview
This documentation covers the Ansible configuration and deployment process for our Docker infrastructure.

## Directory Structure
```
ansible/
├── inventory/
│   └── default_aws_ec2.yml
├── playbooks/
│   └── dev/
│       └── main.yaml
├── roles/
│   └── docker/
└── ansible.cfg
```

## Inventory Configuration
To view the inventory structure, run:
```bash
ansible-inventory -i inventory/default_aws_ec2.yml --list
ansible-inventory -i inventory/default_aws_ec2.yml --graph
```

<details>
<summary>Run log</summary>

(venv) dante@dante-pc:~/PycharmProjects/fork-S25-core-course-labs/ansible$ ansible-inventory --list

```json
{
    "_meta": {
        "hostvars": {
            "ec2-instance": {
                "ansible_host": "ec2-13-51-69-92.eu-north-1.compute.amazonaws.com",
                "ansible_ssh_private_key_file": "./devops-homework.pem",
                "ansible_user": "admin"
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
            "ec2-instance"
        ]
    }
}
```

```bash
(venv) dante@dante-pc:~/PycharmProjects/fork-S25-core-course-labs/ansible$ ansible-inventory -i inventory/default_aws_ec2.yml --graph
@all:
  |--@ungrouped:
  |  |--ec2-instance
```
</details>

## Deployment Process
1. Verify your inventory file is correctly configured
2. Run a dry run first:
   ```bash
   ansible-playbook playbooks/dev/main.yaml --check
   ```
3. Deploy the changes:
   ```bash
   ansible-playbook playbooks/dev/main.yaml --diff
   ```
<details>
<summary>Run log</summary>

```bash
(venv) dante@dante-pc:~/PycharmProjects/fork-S25-core-course-labs/ansible$ ansible-playbook playbooks/dev/main.yaml

PLAY [Install and configure Docker] **************************************************************************************************************************************************

TASK [Gathering Facts] ***************************************************************************************************************************************************************
[WARNING]: Platform linux on host ec2-instance is using the discovered Python interpreter at /usr/bin/python3.11, but future installation of another Python interpreter could change
the meaning of that path. See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [ec2-instance]

TASK [docker : Remove old versions] **************************************************************************************************************************************************
included: /home/dante/PycharmProjects/fork-S25-core-course-labs/ansible/roles/docker/tasks/remove_old_versions.yml for ec2-instance

TASK [docker : Remove conflicting packages] ******************************************************************************************************************************************
ok: [ec2-instance]

TASK [docker : Add repo] *************************************************************************************************************************************************************
included: /home/dante/PycharmProjects/fork-S25-core-course-labs/ansible/roles/docker/tasks/add_repo.yml for ec2-instance

TASK [docker : Update apt] ***********************************************************************************************************************************************************
changed: [ec2-instance]

TASK [docker : Install prerequisites for key addition] *******************************************************************************************************************************
changed: [ec2-instance]

TASK [docker : Add Docker apt repository key.] ***************************************************************************************************************************************
changed: [ec2-instance]

TASK [docker : Add Docker's official apt repository] *********************************************************************************************************************************
changed: [ec2-instance]

TASK [docker : Install Docker] *******************************************************************************************************************************************************
included: /home/dante/PycharmProjects/fork-S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for ec2-instance

TASK [docker : Install Docker and dependencies] **************************************************************************************************************************************
changed: [ec2-instance]

TASK [docker : Add user(s) to Docker group] ******************************************************************************************************************************************
included: /home/dante/PycharmProjects/fork-S25-core-course-labs/ansible/roles/docker/tasks/add_to_group.yml for ec2-instance

TASK [docker : Add user to docker group] *********************************************************************************************************************************************
changed: [ec2-instance] => (item=dante)

TASK [docker : Start docker on startup] **********************************************************************************************************************************************
included: /home/dante/PycharmProjects/fork-S25-core-course-labs/ansible/roles/docker/tasks/enable_on_boot.yml for ec2-instance

TASK [docker : Enable Docker service on boot] ****************************************************************************************************************************************
ok: [ec2-instance]

TASK [docker : Configure Docker security settings] ***********************************************************************************************************************************
included: /home/dante/PycharmProjects/fork-S25-core-course-labs/ansible/roles/docker/tasks/secure_docker.yml for ec2-instance

TASK [docker : Create docker config directory] ***************************************************************************************************************************************
ok: [ec2-instance]

TASK [docker : Configure Docker daemon security settings] ****************************************************************************************************************************
changed: [ec2-instance]

RUNNING HANDLER [docker : Restart Docker service] ************************************************************************************************************************************
changed: [ec2-instance]

PLAY RECAP ***************************************************************************************************************************************************************************
ec2-instance               : ok=18   changed=8    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0    
```
</details>


## Security Features
The Docker role includes several security enhancements:
- User namespace remapping enabled
- No new privileges restriction
- Logging limits configured
- Non-root user configuration
- Secure daemon configuration

## Troubleshooting
If you encounter issues:
1. Verify SSH connectivity to hosts
2. Check host key verification
3. Ensure proper sudo privileges
4. Verify network connectivity