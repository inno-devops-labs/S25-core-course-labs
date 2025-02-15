# Ansible

I use Yandex Cloud Compute VM for this lab.

## Best Practices

* Properly structured Ansible project
* Usage of Dynamic Inventory for Cloud Environments
* Usage of `fact_caching`
* Usage of `ansible-playbook --check`

## Execute Playbook

`ansible-playbook -i inventory/yacloud_compute.yaml playbooks/dev/main.yaml`

```
root@dmhd6219-laptop:~/S25-core-course-labs/ansible# ansible-playbook -i inventory/yacloud_compute.yaml playbooks/dev/main.yaml

PLAY [Install and Configure Docker] ******************************************************************************

TASK [Gathering Facts] *******************************************************************************************
ok: [test]

TASK [docker : Install Docker] ***********************************************************************************
included: /root/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for test

TASK [docker : Update apt packages] ******************************************************************************
changed: [test]

TASK [docker : Install apt packages] *****************************************************************************
ok: [test]

TASK [docker : Add Docker's official GPG key] ********************************************************************
ok: [test]

TASK [docker : Add Docker's official apt repository] *************************************************************
ok: [test]

TASK [docker : Install Docker and Docker Compose] ****************************************************************
ok: [test] => (item=docker-ce)
ok: [test] => (item=docker-ce-cli)
ok: [test] => (item=containerd.io)
ok: [test] => (item=docker-buildx-plugin)

TASK [docker : Add Docker group] *********************************************************************************
ok: [test]

TASK [docker : Add user to Docker group] *************************************************************************
ok: [test]

TASK [docker : Enable and start Docker services] *****************************************************************
ok: [test] => (item=docker.service)
ok: [test] => (item=containerd.service)

TASK [docker : Install Docker Compose] ***************************************************************************
included: /root/S25-core-course-labs/ansible/roles/docker/tasks/install_docker_compose.yml for test

TASK [docker : Install Docker Compose] ***************************************************************************
changed: [test]

PLAY RECAP *******************************************************************************************************
test                       : ok=12   changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0


WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
```

## Inventory Details

`ansible-inventory -i inventory/yacloud_compute.yaml --list | tail -n 50`

```
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
E0000 00:00:1739627707.476908   65143 init.cc:232] grpc_wait_for_shutdown_with_timeout() timed out.
                "ansible_user_gecos": {
                    "__ansible_unsafe": "root"
                },
                "ansible_user_gid": 0,
                "ansible_user_id": {
                    "__ansible_unsafe": "root"
                },
                "ansible_user_shell": {
                    "__ansible_unsafe": "/bin/bash"
                },
                "ansible_user_uid": 0,
                "ansible_userspace_architecture": {
                    "__ansible_unsafe": "x86_64"
                },
                "ansible_userspace_bits": {
                    "__ansible_unsafe": "64"
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
            "test"
        ]
    }
}
```