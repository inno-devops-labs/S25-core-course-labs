# Ansible

I used Yandex Cloud VM. It was not pleasant.

## Best Practices

* Properly structured Ansible project
* Usage of Dynamic Inventory for Cloud Environments using the plugin 
* Usage of `ansible-playbook --check`

# Executions:

```bash
ansible-playbook -i inventory/yacloud_compute.yaml playbooks/dev/main.yaml
```

```nothing
vboxuser@sdafdghkj:~/DevOps/ansible$ ansible-playbook -i inventory/default_yandex.yml playbooks/dev/main_docker_role.yaml | tail -n 50
[WARNING]: Platform linux on host 158.160.147.187 is using the discovered
Python interpreter at /usr/bin/python3.12, but future installation of another
Python interpreter could change the meaning of that path. See
https://docs.ansible.com/ansible-
core/2.18/reference_appendices/interpreter_discovery.html for more information.
TASK [geerlingguy.docker : Add Docker apt key.] ********************************
ok: [158.160.147.187]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] ***
skipping: [158.160.147.187]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] ***
skipping: [158.160.147.187]

TASK [geerlingguy.docker : Add Docker repository.] *****************************
ok: [158.160.147.187]

TASK [geerlingguy.docker : Install Docker packages.] ***************************
skipping: [158.160.147.187]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] ***
ok: [158.160.147.187]

TASK [geerlingguy.docker : Install docker-compose plugin.] *********************
skipping: [158.160.147.187]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] ***
ok: [158.160.147.187]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] **************
skipping: [158.160.147.187]

TASK [geerlingguy.docker : Configure Docker daemon options.] *******************
skipping: [158.160.147.187]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] ******
ok: [158.160.147.187]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] ***

TASK [geerlingguy.docker : include_tasks] **************************************
skipping: [158.160.147.187]

TASK [geerlingguy.docker : Get docker group info using getent.] ****************
skipping: [158.160.147.187]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] ***
skipping: [158.160.147.187]

TASK [geerlingguy.docker : include_tasks] **************************************
skipping: [158.160.147.187]

PLAY RECAP *********************************************************************
158.160.147.187            : ok=14   changed=0    unreachable=0    failed=0    skipped=11   rescued=0    ignored=0   


```

```nothing
vboxuser@sdafdghkj:~/DevOps/ansible$ ansible-inventory -i inventory/default_yandex.yml --list | tail -n 50
{
    "_meta": {
        "hostvars": {
            "158.160.147.187": {
                "ansible_ssh_private_key_file": "~/.ssh/id_ed25519",
                "ansible_user": "maggie"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "ec2"
        ]
    },
    "ec2": {
        "hosts": [
            "158.160.147.187"
        ]
    }
}
```

```nothing
vboxuser@sdafdghkj:~/DevOps/ansible$ ansible-inventory -i inventory/default_yandex.yml --graph
@all:
  |--@ungrouped:
  |--@ec2:
  |  |--158.160.147.187
```