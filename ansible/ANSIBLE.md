# Ansible automation

## Best practices used

- Kept simple.
- Used lists rather than loops where possible (apt packages, users) to have better performance and reporting
- Used a handler for a potentially repeating task
- Ansible-lint was used to check the playbook for errors and improve it
- Dynamic inventory!
- Both tags and `when` were used to conditionally run tasks
  - `when` for wiping task rather than ignoring errors about non-existent directory for idempotency
- Using modules rather than shell, even in complicated scenarios (docker package and externally-managed dependencies)

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

## Test run of the web app playbook

```txt
devops-labs ❯ ansible-playbook playbooks/dev/main.yaml -i inven
tory/yacloud_compute.yml
iam token used

PLAY [Install and configure Docker] ********************************************

TASK [Gathering Facts] *********************************************************
[WARNING]: Platform linux on host terraform1 is using the discovered Python
interpreter at /usr/bin/python3.11, but future installation of another Python
interpreter could change the meaning of that path. See
https://docs.ansible.com/ansible-
core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [terraform1]

TASK [docker : Remove old versions] ********************************************
included: /Users/fallenchromium/University/maga/Innopolis/devops/S25-core-course-labs/ansible/roles/docker/tasks/remove_old_versions.yml for terraform1

TASK [docker : Remove conflicting packages] ************************************
ok: [terraform1]

TASK [docker : Add repo] *******************************************************
included: /Users/fallenchromium/University/maga/Innopolis/devops/S25-core-course-labs/ansible/roles/docker/tasks/add_repo.yml for terraform1

TASK [docker : Update apt] *****************************************************
ok: [terraform1]

TASK [docker : Install prerequisites for key addition] *************************
ok: [terraform1]

TASK [docker : Add Docker apt repository key.] *********************************
ok: [terraform1]

TASK [docker : Add Docker's official apt repository] ***************************
ok: [terraform1]

TASK [docker : Install Docker] *************************************************
included: /Users/fallenchromium/University/maga/Innopolis/devops/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for terraform1

TASK [docker : Install Docker and dependencies] ********************************
ok: [terraform1]

TASK [docker : Add user(s) to Docker group] ************************************
included: /Users/fallenchromium/University/maga/Innopolis/devops/S25-core-course-labs/ansible/roles/docker/tasks/add_to_group.yml for terraform1

TASK [docker : Add user to docker group] ***************************************
ok: [terraform1] => (item=fallenchromium)

TASK [docker : Start docker on startup] ****************************************
included: /Users/fallenchromium/University/maga/Innopolis/devops/S25-core-course-labs/ansible/roles/docker/tasks/enable_on_boot.yml for terraform1

TASK [docker : Enable Docker service on boot] **********************************
ok: [terraform1]

TASK [docker : Configure Docker security settings] *****************************
included: /Users/fallenchromium/University/maga/Innopolis/devops/S25-core-course-labs/ansible/roles/docker/tasks/secure_docker.yml for terraform1

TASK [docker : Create docker config directory] *********************************
ok: [terraform1]

TASK [docker : Configure Docker daemon security settings] **********************
ok: [terraform1]

TASK [docker : Install Docker Python module] ***********************************
included: /Users/fallenchromium/University/maga/Innopolis/devops/S25-core-course-labs/ansible/roles/docker/tasks/ansible_docker.yml for terraform1

TASK [docker : Install pip] ****************************************************
ok: [terraform1]

TASK [docker : Install Docker pip module] **************************************
ok: [terraform1]

TASK [web_app : Create application directory] **********************************
ok: [terraform1]

TASK [web_app : Deploy Docker Compose template] ********************************
changed: [terraform1]

TASK [web_app : Pull Docker image] *********************************************
ok: [terraform1]

TASK [web_app : Deploy with Docker Compose] ************************************

changed: [terraform1]

PLAY RECAP *********************************************************************
terraform1                 : ok=24   changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

## Test run of the wipe

```txt
devops-labs ❯ ansible-playbook playbooks/dev/main.yaml -i inven
tory/yacloud_compute.yml --tags wipe
iam token used

PLAY [Install and configure Docker] ********************************************

TASK [Gathering Facts] *********************************************************
ok: [terraform1]

TASK [web_app : Stop and remove Docker containers using docker-compose] ********
skipping: [terraform1]

TASK [web_app : Remove Docker compose directory] *******************************
ok: [terraform1]

TASK [web_app : Remove Docker image] *******************************************
ok: [terraform1]

PLAY RECAP *********************************************************************
terraform1                 : ok=3    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
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

