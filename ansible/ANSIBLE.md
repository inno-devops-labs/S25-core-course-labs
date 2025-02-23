# Execute Playbook

$ ansible-playbook playbooks/dev/main.yaml --diff 
```

PLAY [Install Docker on VМ] ***************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************
ok: [yc_instance]

TASK [docker : include_tasks] *************************************************************************************************************
included: /home/akvadevka/PycharmProjects/pythonProject2/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for yc_instance

TASK [docker : Update apt packages] *******************************************************************************************************
ok: [yc_instance]

TASK [docker : Install required apt packages] *********************************************************************************************
ok: [yc_instance]

TASK [docker : Add Docker's official GPG key] *********************************************************************************************
ok: [yc_instance]

TASK [docker : Add Docker's official apt repository] **************************************************************************************
[WARNING]: Skipping plugin (/usr/lib/python3/dist-packages/ansible/plugins/filter/core.py) as it seems to be invalid: cannot import name
'environmentfilter' from 'jinja2.filters' (/home/akvadevka/.local/lib/python3.10/site-packages/jinja2/filters.py)
[WARNING]: Skipping plugin (/usr/lib/python3/dist-packages/ansible/plugins/filter/mathstuff.py) as it seems to be invalid: cannot import
name 'environmentfilter' from 'jinja2.filters' (/home/akvadevka/.local/lib/python3.10/site-packages/jinja2/filters.py)
ok: [yc_instance]

TASK [docker : Install Docker] ************************************************************************************************************
ok: [yc_instance]

TASK [docker : Add Docker group] **********************************************************************************************************
ok: [yc_instance]

TASK [docker : Add user to Docker group] **************************************************************************************************
[WARNING]: Skipping plugin (/usr/lib/python3/dist-packages/ansible/plugins/filter/core.py) as it seems to be invalid: cannot import name
'environmentfilter' from 'jinja2.filters' (/home/akvadevka/.local/lib/python3.10/site-packages/jinja2/filters.py)
[WARNING]: Skipping plugin (/usr/lib/python3/dist-packages/ansible/plugins/filter/mathstuff.py) as it seems to be invalid: cannot import
name 'environmentfilter' from 'jinja2.filters' (/home/akvadevka/.local/lib/python3.10/site-packages/jinja2/filters.py)
ok: [yc_instance]

TASK [docker : Configure Docker security settings] ****************************************************************************************
ok: [yc_instance]

TASK [docker : Enable and start Docker services] ******************************************************************************************
[WARNING]: Skipping plugin (/usr/lib/python3/dist-packages/ansible/plugins/filter/core.py) as it seems to be invalid: cannot import name
'environmentfilter' from 'jinja2.filters' (/home/akvadevka/.local/lib/python3.10/site-packages/jinja2/filters.py)
[WARNING]: Skipping plugin (/usr/lib/python3/dist-packages/ansible/plugins/filter/mathstuff.py) as it seems to be invalid: cannot import
name 'environmentfilter' from 'jinja2.filters' (/home/akvadevka/.local/lib/python3.10/site-packages/jinja2/filters.py)
ok: [yc_instance] => (item=docker.service)
ok: [yc_instance] => (item=containerd.service)

TASK [docker : include_tasks] *************************************************************************************************************
included: /home/akvadevka/PycharmProjects/pythonProject2/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for yc_instance

TASK [docker : Install Docker Compose] ****************************************************************************************************
changed: [yc_instance]

PLAY RECAP ********************************************************************************************************************************
yc_instance                : ok=13   changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

```

# Inventory Details
```` bash
ansible-inventory -i inventory/default_aws_ec2.yml --list
````
````
(.venv) akvadevka@akvadevka-VirtualBox:~/PycharmProjects/pythonProject2/S25-core-course-labs/ansible$ ansible-inventory -i inventory/default_aws_ec2.yml --list
{
    "_meta": {
        "hostvars": {
            "yc_instance": {
                "ansible_host": "51.250.19.210",
                "ansible_ssh_private_key_file": "~/.ssh/id_rsa",
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
            "yc_instance"
        ]
    }
}

````
## inventory structure
```bash
ansible-inventory -i inventory/default_aws_ec2.yml --graph
```
```
@all:
  |--@ungrouped:
  |  |--yc_instance
```

# Deployment Output for web app 

## last 50 lines

TASK [docker : Install required apt packages] **********************************
ok: [yc_instance]

TASK [docker : Add Docker's official GPG key] **********************************
ok: [yc_instance]

TASK [docker : Add Docker's official apt repository] ***************************
ok: [yc_instance]

TASK [docker : Install Docker] *************************************************
ok: [yc_instance]

TASK [docker : Add Docker group] ***********************************************
ok: [yc_instance]

TASK [docker : Add user to Docker group] ***************************************
ok: [yc_instance]

TASK [docker : Configure Docker security settings] *****************************
ok: [yc_instance]

TASK [docker : Enable and start Docker services] *******************************
ok: [yc_instance] => (item=docker.service)
ok: [yc_instance] => (item=containerd.service)

TASK [docker : include_tasks] **************************************************
included: /home/akvadevka/PycharmProjects/pythonProject2/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for yc_instance

TASK [docker : Install Docker Compose] *****************************************
ok: [yc_instance]

TASK [web_app : Remove web application container] ******************************
skipping: [yc_instance]

TASK [web_app : Remove image] **************************************************
skipping: [yc_instance]

TASK [web_app : Fetch latest Docker image] *************************************
changed: [yc_instance]

TASK [web_app : Generate Docker Compose configuration] *************************
changed: [yc_instance]

TASK [web_app : Launch application container via Docker Compose] ***************
changed: [yc_instance]

PLAY RECAP *********************************************************************
yc_instance                : ok=16   changed=3    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   

