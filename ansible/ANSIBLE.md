# Ansible

## Best Practices

1. Name tasks

## Deployment

```text
$ ansible-playbook -i inventory/yacloud_compute.yaml playbooks/dev/main.yaml

PLAY [Playbook] *****************************************************************************************

TASK [Gathering Facts] *****************************************************************************
ok: [virtual-machine]

TASK [docker : install `pip`] **********************************************************
ok: [virtual-machine]

TASK [docker : install required packages] ***************************************
ok: [virtual-machine]

TASK [docker : add gpg key] ***************************************************
ok: [virtual-machine]

TASK [docker : add docker repo] **************************************************
ok: [virtual-machine]

TASK [docker : install docker] *********************************************************
ok: [virtual-machine]

TASK [docker : ensure that group `docker` exists] *********************************************************
ok: [virtual-machine]

TASK [docker : adding ubuntu to docker group] *********************************************************
ok: [virtual-machine]

TASK [docker : install docker-compose] *************************************************
changed: [virtual-machine]

PLAY RECAP *****************************************************************************************
virtual-machine            : ok=9    changed=1    unreachable=0    failed=0    skipped=0    rescued=
0    ignored=0
```

```text
$ ansible-inventory -i inventory --list

{
    "_meta": {
        "hostvars": {
            "virtual-machine": {
                "ansible_user": "ubuntu"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "yandex_cloud"
        ]
    },
    "yandex_cloud": {
        "hosts": [
            "virtual-machine"
        ]
    }
}
```
