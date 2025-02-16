# Ansible

I am using Yandex Cloud virtual machine, so in order to complete
this lab fully, I used

## Best practices

1. Before playbook execution I've been running it in dry-run
mode using `--check` flag. I also was checking the syntax with `--syntax-check`.

1. Use of `handlers` to be sure that, e.g., Docker is running.

1. Locally I used `ansible-lint` to fix issues in playbooks. 

### Checks

I checked docker installation with `ansible-galaxy`, it worked, so I did the same with
hand-written tasks.

The output of commands may be not full because I have already been running Dev playbook before
writing this `.md` file.

## `ansible-playbook playbooks/dev/main.yml --diff`

```
╰─➤  ansible-playbook playbooks/dev/main.yml --diff                                 

PLAY [Dev] ***************************************************************************************************************************************************

TASK [Gathering Facts] ***************************************************************************************************************************************
[WARNING]: Platform linux on host devops-vm is using the discovered Python interpreter at /usr/bin/python3.10, but future installation of another Python
interpreter could change the meaning of that path. See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more
information.
ok: [devops-vm]

TASK [docker : Install Docker] *******************************************************************************************************************************
included: /Users/matveykorinenko/Documents/Inno/BS3/Spring/DevOps/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for devops-vm

TASK [docker : Update apt package index] *********************************************************************************************************************
changed: [devops-vm]

TASK [docker : Install dependencies] *************************************************************************************************************************
ok: [devops-vm] => (item=apt-transport-https)
ok: [devops-vm] => (item=ca-certificates)
ok: [devops-vm] => (item=curl)
ok: [devops-vm] => (item=gnupg-agent)
ok: [devops-vm] => (item=software-properties-common)

TASK [docker : Add Docker GPG key] ***************************************************************************************************************************
ok: [devops-vm]

TASK [docker : Add Docker apt repository] ********************************************************************************************************************
ok: [devops-vm]

TASK [docker : Install Docker with dependencies] *************************************************************************************************************
ok: [devops-vm]

TASK [docker : Start Docker service] *************************************************************************************************************************
ok: [devops-vm]

TASK [docker : Secure Docker configuration] ******************************************************************************************************************
included: /Users/matveykorinenko/Documents/Inno/BS3/Spring/DevOps/S25-core-course-labs/ansible/roles/docker/tasks/secure_configure_docker.yml for devops-vm

TASK [docker : Add user to Docker group] *********************************************************************************************************************
ok: [devops-vm]

TASK [docker : Disable root access] **************************************************************************************************************************
ok: [devops-vm]

TASK [docker : Install Docker Compose] ***********************************************************************************************************************
included: /Users/matveykorinenko/Documents/Inno/BS3/Spring/DevOps/S25-core-course-labs/ansible/roles/docker/tasks/install_docker_compose.yml for devops-vm

TASK [docker : Install Docker Compose] ***********************************************************************************************************************
ok: [devops-vm]

PLAY RECAP ***************************************************************************************************************************************************
devops-vm                  : ok=13   changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
E0000 00:00:1739207132.405013 74388315 init.cc:232] grpc_wait_for_shutdown_with_timeout() timed out.
```

## `ansible-inventory -i inventory/yacloud_compute.yml --list`

```
╰─➤  ansible-inventory -i inventory/yacloud_compute.yml --list             
{
    "_meta": {
        "hostvars": {
            "devops-vm": {
                "ansible_host": "89.169.144.195"
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
            "devops-vm"
        ]
    }
}
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
E0000 00:00:1739120849.267506 71915415 init.cc:232] grpc_wait_for_shutdown_with_timeout() timed out.
```
