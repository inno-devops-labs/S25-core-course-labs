# Ansible

## Best practices

* **Modularity**: everything is splitted into modules and 
inporting neccessary files in `main.yml`
* **Handlers**: prevents from unnecessary restarts
* **Extra checks and validations**: I have added extra
printings and tasks to ensure that docker is 
running, for instance
* **Added user to Docker group**
* **Usage of roles**
* **Dynamic inventory**: using Yandex Cloud compute
* **Non-root user**

## Commands output


# Docker role
#### ```ansible-playbook -i inventory/default_yandex.yml playbooks/dev/main.yaml```

```
PLAY [Docker Deploying] ****************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************
ok: [yandex_machine]

TASK [docker : Update apt package index] ***********************************************************************************
changed: [yandex_machine]

TASK [docker : Install packages] *******************************************************************************************
ok: [yandex_machine]

TASK [docker : Add Docker GPG key] *****************************************************************************************
ok: [yandex_machine]

TASK [docker : Add Docker repository] **************************************************************************************
ok: [yandex_machine]

TASK [docker : Install Docker] *********************************************************************************************
ok: [yandex_machine]

TASK [docker : Ensure /usr/local/bin exists] *******************************************************************************
ok: [yandex_machine]

TASK [docker : Docker compose Install] *************************************************************************************
ok: [yandex_machine]

TASK [docker : Ensure Docker service is running] ***************************************************************************
ok: [yandex_machine]

TASK [docker : Add cur user to docker group] *******************************************************************************
ok: [yandex_machine]

TASK [docker : Verify Docker installation] *********************************************************************************
ok: [yandex_machine]

TASK [docker : Print Docker version] ***************************************************************************************
ok: [yandex_machine] => {
    "msg": "Docker version 27.5.1, build 9f9e405"
}

TASK [docker : Verify Docker Compose installation] *************************************************************************
ok: [yandex_machine]

TASK [docker : Print Docker Compose version] *******************************************************************************
ok: [yandex_machine] => {
    "msg": "docker-compose version 1.29.2, build 5becea4c"
}

PLAY RECAP *****************************************************************************************************************
yandex_machine             : ok=14   changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

```


### Check (dry run)
#### ```ansible-playbook playbooks/dev/main.yaml --check```

```
PLAY [Docker Deploying] ****************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************
ok: [yandex_machine]

TASK [docker : Update apt package index] ***********************************************************************************
changed: [yandex_machine]

TASK [docker : Install packages] *******************************************************************************************
ok: [yandex_machine]

TASK [docker : Add Docker GPG key] *****************************************************************************************
ok: [yandex_machine]

TASK [docker : Add Docker repository] **************************************************************************************
ok: [yandex_machine]

TASK [docker : Install Docker] *********************************************************************************************
ok: [yandex_machine]

TASK [docker : Ensure /usr/local/bin exists] *******************************************************************************
ok: [yandex_machine]

TASK [docker : Docker compose Install] *************************************************************************************
ok: [yandex_machine]

TASK [docker : Ensure Docker service is running] ***************************************************************************
ok: [yandex_machine]

TASK [docker : Add cur user to docker group] *******************************************************************************
ok: [yandex_machine]

TASK [docker : Verify Docker installation] *********************************************************************************
skipping: [yandex_machine]

TASK [docker : Print Docker version] ***************************************************************************************
ok: [yandex_machine] => {
    "msg": ""
}

TASK [docker : Verify Docker Compose installation] *************************************************************************
skipping: [yandex_machine]

TASK [docker : Print Docker Compose version] *******************************************************************************
ok: [yandex_machine] => {
    "msg": ""
}

PLAY RECAP *****************************************************************************************************************
yandex_machine             : ok=12   changed=1    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   

```


Also, executed with ```--diff``` flag - was the same output

## Inventory details

#### 1. ```ansible-inventory -i inventory/default_yandex.yml --list```


```
{
    "_meta": {
        "hostvars": {
            "yandex_machine": {
                "ansible_host": "89.169.134.171",
                "ansible_python_interpreter": "/usr/bin/python3",
                "ansible_ssh_private_key_file": "~/.ssh/id_rsa",
                "ansible_user": "ubuntu"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "virtual_machines"
        ]
    },
    "virtual_machines": {
        "hosts": [
            "yandex_machine"
        ]
    }
}
```


#### 2. ```ansible-inventory -i inventory/default_yandex.yml --graph```

```
@all:
  |--@ungrouped:
  |--@virtual_machines:
  |  |--yandex_machine
```



# Bonus Tasks

### 1. Yandex Cloud plugin for the dynamic inventory


#### ```ansible-inventory -i inventory/yacloud_compute.yml --list```

```
{
    "_meta": {
        "hostvars": {
            "terraform1": {
                "ansible_host": "89.169.134.171"
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
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
E0000 00:00:1739454282.219996   93470 init.cc:232] grpc_wait_for_shutdown_with_timeout() timed out.

```


### 2. Secure Docker

```
...


TASK [docker : Secure Docker Daemon] **************************************************************************************************************************
ok: [yandex_machine]

...
```

#### Full code with the command ```ansible-playbook -i inventory/default_yandex.yml playbooks/dev/main.yaml```


```
PLAY [Docker Deploying] ***************************************************************************************************************************************

TASK [Gathering Facts] ****************************************************************************************************************************************
ok: [yandex_machine]

TASK [docker : Update apt package index] **********************************************************************************************************************
changed: [yandex_machine]

TASK [docker : Install packages] ******************************************************************************************************************************
ok: [yandex_machine]

TASK [docker : Add Docker GPG key] ****************************************************************************************************************************
ok: [yandex_machine]

TASK [docker : Add Docker repository] *************************************************************************************************************************
ok: [yandex_machine]

TASK [docker : Install Docker] ********************************************************************************************************************************
ok: [yandex_machine]

TASK [docker : Ensure /usr/local/bin exists] ******************************************************************************************************************
ok: [yandex_machine]

TASK [docker : Docker compose Install] ************************************************************************************************************************
ok: [yandex_machine]

TASK [docker : Ensure Docker service is running] **************************************************************************************************************
ok: [yandex_machine]

TASK [docker : Add cur user to docker group] ******************************************************************************************************************
ok: [yandex_machine]

TASK [docker : Secure Docker Daemon] **************************************************************************************************************************
ok: [yandex_machine]

TASK [docker : Verify Docker installation] ********************************************************************************************************************
ok: [yandex_machine]

TASK [docker : Print Docker version] **************************************************************************************************************************
ok: [yandex_machine] => {
    "msg": "Docker version 27.5.1, build 9f9e405"
}

TASK [docker : Verify Docker Compose installation] ************************************************************************************************************
ok: [yandex_machine]

TASK [docker : Print Docker Compose version] ******************************************************************************************************************
ok: [yandex_machine] => {
    "msg": "docker-compose version 1.29.2, build 5becea4c"
}

PLAY RECAP ****************************************************************************************************************************************************
yandex_machine             : ok=15   changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

```
