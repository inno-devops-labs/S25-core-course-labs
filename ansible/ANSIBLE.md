# Ansible automation

## Best practices used

- Kept simple.
- Used lists rather than loops where possible (apt packages, users) to have better performance and reporting
- Used a handler for a potentially repeating task
- Ansible-lint was used to check the playbook for errors and improve it
- Dynamic inventory!

## Test run of the Docker installation playbook

```sh
devops-labs ❯ ansible-playbook playbooks/dev/main.yaml -i inventory/yacloud_compute.yml --diff --check
iam token used

PLAY [Install and configure Docker] *****************************************************************************************************

TASK [Gathering Facts] ******************************************************************************************************************
[WARNING]: Platform linux on host terraform1 is using the discovered Python interpreter at /usr/bin/python3.11, but future installation
of another Python interpreter could change the meaning of that path. See https://docs.ansible.com/ansible-
core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [terraform1]

TASK [docker : Remove old versions] *****************************************************************************************************
included: /Users/fallenchromium/University/maga/Innopolis/devops/S25-core-course-labs/ansible/roles/docker/tasks/remove_old_versions.yml for terraform1

TASK [docker : Remove conflicting packages] *********************************************************************************************
ok: [terraform1]

TASK [docker : Add repo] ****************************************************************************************************************
included: /Users/fallenchromium/University/maga/Innopolis/devops/S25-core-course-labs/ansible/roles/docker/tasks/add_repo.yml for terraform1

TASK [docker : Update apt] **************************************************************************************************************
changed: [terraform1]

TASK [docker : Install prerequisites for key addition] **********************************************************************************
ok: [terraform1] => (item=apt-transport-https)
ok: [terraform1] => (item=ca-certificates)
ok: [terraform1] => (item=curl)

TASK [docker : Add Docker apt repository key.] ******************************************************************************************
changed: [terraform1]

TASK [docker : Add Docker's official apt repository] ************************************************************************************
ok: [terraform1]

TASK [docker : Install Docker] **********************************************************************************************************
included: /Users/fallenchromium/University/maga/Innopolis/devops/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for terraform1

TASK [docker : Install Docker and dependencies] *****************************************************************************************
ok: [terraform1]

TASK [docker : Add user(s) to Docker group] *********************************************************************************************
included: /Users/fallenchromium/University/maga/Innopolis/devops/S25-core-course-labs/ansible/roles/docker/tasks/add_to_group.yml for terraform1

TASK [docker : Add user to docker group] ************************************************************************************************
ok: [terraform1] => (item=fallenchromium)

TASK [docker : Start docker on startup] *************************************************************************************************
included: /Users/fallenchromium/University/maga/Innopolis/devops/S25-core-course-labs/ansible/roles/docker/tasks/enable_on_boot.yml for terraform1

TASK [docker : Enable Docker service on boot] *******************************************************************************************
ok: [terraform1]

PLAY RECAP ******************************************************************************************************************************
terraform1                 : ok=14   changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

## Dynamic inventory

```json
devops-labs ❯ ansible-inventory -i inventory/yacloud_compute.yml --list
iam token used
{
    "_meta": {
        "hostvars": {
            "terraform1": {
                "ansible_host": "xx.xx.xx.xx"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "yacloud"
        ]
    },
    "yacloud": {
        "hosts": [
            "terraform1"
        ]
    }
}
```

## Inventory graph

```sh
devops-labs ❯ ansible-inventory -i inventory/yacloud_compute.yml --graph   
@all:
  |--@ungrouped:
  |--@yacloud:
  |  |--terraform1
```

