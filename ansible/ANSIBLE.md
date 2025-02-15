ansible-playbook playbooks/dev/main.yaml --check

PLAY [Deploying docker] ************************************************************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************************************************************
[WARNING]: Platform linux on host localhost is using the discovered Python interpreter at /usr/bin/python3.10, but future installation of another Python interpreter could change
the meaning of that path. See https://docs.ansible.com/ansible-core/2.17/reference_appendices/interpreter_discovery.html for more information.
ok: [localhost]

TASK [docker : Install docker] *****************************************************************************************************************************************************
included: /home/devops/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for localhost

TASK [docker : Install prerequisites] **********************************************************************************************************************************************
changed: [localhost]

TASK [docker : Add Docker GPG key] *************************************************************************************************************************************************
changed: [localhost]

TASK [docker : Add Docker repository] **********************************************************************************************************************************************
changed: [localhost]

TASK [docker : Install Docker] *****************************************************************************************************************************************************
ok: [localhost]

TASK [docker : Ensure Docker service is enabled and running] ***********************************************************************************************************************
ok: [localhost]

TASK [docker : Add users to the Docker group] **************************************************************************************************************************************
skipping: [localhost]

TASK [docker : Verify Docker installation] *****************************************************************************************************************************************
skipping: [localhost]

TASK [docker : Display Docker version] *********************************************************************************************************************************************
ok: [localhost] => {
    "msg": ""
}

TASK [docker : Install docker compose] *********************************************************************************************************************************************
included: /home/devops/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for localhost

TASK [docker : Download Docker Compose] ********************************************************************************************************************************************
changed: [localhost]

TASK [docker : Verify Docker Compose installation] *********************************************************************************************************************************
skipping: [localhost]

TASK [docker : Display Docker Compose version] *************************************************************************************************************************************
ok: [localhost] => {
    "msg": ""
}

PLAY RECAP *************************************************************************************************************************************************************************
localhost                  : ok=11   changed=4    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0


ansible-inventory -i inventory/default_aws_ec2.yml --list
{
    "_meta": {
        "hostvars": {
            "localhost": {
                "ansible_connection": "local"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "local"
        ]
    },
    "local": {
        "hosts": [
            "localhost"
        ]
    }
}


ansible-inventory -i inventory/default_aws_ec2.yml --graph
@all:
  |--@ungrouped:
  |--@local:
  |  |--localhost
