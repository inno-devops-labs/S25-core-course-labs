# Ansible

I use Yandex Cloud Compute VM for this lab.

## Best Practices

* Properly structured Ansible project
* Usage of Dynamic Inventory for Cloud Environments
* Usage of `fact_caching`
* Usage of `ansible-playbook --check`

## Execute Playbook

`ansible-playbook -i inventory/yacloud_compute.yaml playbooks/dev/app_typescript/main.yml`

```
root@dmhd6219-laptop:~/S25-core-course-labs/ansible# ansible-playbook -i inventory/yacloud_compute.yaml playbooks/dev/app_typescript/main.yml

PLAY [Deploy app_python] *******************************************************************************************************************

TASK [Gathering Facts] *********************************************************************************************************************
ok: [compute-vm-2-1-10-hdd-1739646628373]

TASK [docker : Install Docker] *************************************************************************************************************
included: /root/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for compute-vm-2-1-10-hdd-1739646628373

TASK [docker : Update apt packages] ********************************************************************************************************
changed: [compute-vm-2-1-10-hdd-1739646628373]

TASK [docker : Install apt packages] *******************************************************************************************************
ok: [compute-vm-2-1-10-hdd-1739646628373]

TASK [docker : Add Docker's official GPG key] **********************************************************************************************
ok: [compute-vm-2-1-10-hdd-1739646628373]

TASK [docker : Add Docker's official apt repository] ***************************************************************************************
ok: [compute-vm-2-1-10-hdd-1739646628373]

TASK [docker : Install Docker and Docker Compose] ******************************************************************************************
ok: [compute-vm-2-1-10-hdd-1739646628373] => (item=docker-ce)
ok: [compute-vm-2-1-10-hdd-1739646628373] => (item=docker-ce-cli)
ok: [compute-vm-2-1-10-hdd-1739646628373] => (item=containerd.io)
ok: [compute-vm-2-1-10-hdd-1739646628373] => (item=docker-buildx-plugin)

TASK [docker : Add Docker group] ***********************************************************************************************************
ok: [compute-vm-2-1-10-hdd-1739646628373]

TASK [docker : Add user to Docker group] ***************************************************************************************************
ok: [compute-vm-2-1-10-hdd-1739646628373]

TASK [docker : Configure Docker security settings] *****************************************************************************************
ok: [compute-vm-2-1-10-hdd-1739646628373]

TASK [docker : Enable and start Docker services] *******************************************************************************************
ok: [compute-vm-2-1-10-hdd-1739646628373] => (item=docker.service)
ok: [compute-vm-2-1-10-hdd-1739646628373] => (item=containerd.service)

TASK [docker : Install Docker Compose] *****************************************************************************************************
included: /root/S25-core-course-labs/ansible/roles/docker/tasks/install_docker_compose.yml for compute-vm-2-1-10-hdd-1739646628373

TASK [docker : Install Docker Compose] *****************************************************************************************************
ok: [compute-vm-2-1-10-hdd-1739646628373]

TASK [web_app : Remove container] **********************************************************************************************************
skipping: [compute-vm-2-1-10-hdd-1739646628373]

TASK [web_app : Remove docker-compose file] ************************************************************************************************
skipping: [compute-vm-2-1-10-hdd-1739646628373]

TASK [web_app : Pull Docker image] *********************************************************************************************************
changed: [compute-vm-2-1-10-hdd-1739646628373]

TASK [web_app : Start container] ***********************************************************************************************************
changed: [compute-vm-2-1-10-hdd-1739646628373]

TASK [web_app : Create directory for docker-compose file] **********************************************************************************
changed: [compute-vm-2-1-10-hdd-1739646628373]

TASK [web_app : Deploy docker-compose file] ************************************************************************************************
changed: [compute-vm-2-1-10-hdd-1739646628373]

PLAY RECAP *********************************************************************************************************************************
compute-vm-2-1-10-hdd-1739646628373 : ok=17   changed=5    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0

WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
E0000 00:00:1739647290.968013  185493 init.cc:232] grpc_wait_for_shutdown_with_timeout() timed out.
```

## Inventory Details

`ansible-inventory -i inventory/yacloud_compute.yaml --list | tail -n 50`

```
root@dmhd6219-laptop:~/S25-core-course-labs/ansible# ansible-inventory -i inventory/yacloud_compute.yaml --list | tail -n 50
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
E0000 00:00:1739648322.105744  195428 init.cc:232] grpc_wait_for_shutdown_with_timeout() timed out.
                                "__ansible_unsafe": "64"
                            },
                            "scope": {
                                "__ansible_unsafe": "link"
                            }
                        }
                    ],
                    "macaddress": {
                        "__ansible_unsafe": "22:19:f7:fd:e6:cc"
                    },
                    "mtu": 1500,
                    "promisc": true,
                    "speed": 10000,
                    "timestamping": [],
                    "type": {
                        "__ansible_unsafe": "ether"
                    }
                },
                "ansible_virtualization_role": {
                    "__ansible_unsafe": "NA"
                },
                "ansible_virtualization_tech_guest": [],
                "ansible_virtualization_tech_host": [],
                "ansible_virtualization_type": {
                    "__ansible_unsafe": "NA"
                },
                "discovered_interpreter_python": {
                    "__ansible_unsafe": "/usr/bin/python3.12"
                },
                "gather_subset": [
                    {
                        "__ansible_unsafe": "all"
                    }
                ],
                "module_setup": true
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
            "compute-vm-2-1-10-hdd-1739646628373"
        ]
    }
}
```