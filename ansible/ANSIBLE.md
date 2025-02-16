# Ansible development report

```sh
tedor49@tedor49:~/S25-core-course-labs/ansible$ ansible-playbook playbooks/dev/main.yaml | tail -n 50

PLAY [all] *********************************************************************

TASK [Gathering Facts] *********************************************************
ok: [158.160.159.213]

TASK [docker : Install Docker] *************************************************
included: /home/tedor49/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for 158.160.159.213

TASK [docker : Add Docker GPG key] *********************************************
ok: [158.160.159.213]

TASK [docker : Add Docker apt repository] **************************************
ok: [158.160.159.213]

TASK [docker : Install Docker packages.] ***************************************
ok: [158.160.159.213]

TASK [docker : Start Docker service.] ******************************************
ok: [158.160.159.213]

TASK [docker : Add user to Docker group] ***************************************
ok: [158.160.159.213]

TASK [docker : Install Docker Compose] *****************************************
included: /home/tedor49/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for 158.160.159.213

TASK [docker : Install docker-compose plugin.] *********************************
ok: [158.160.159.213]

PLAY RECAP *********************************************************************
158.160.159.213            : ok=9    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

```


```sh
tedor49@tedor49:~/S25-core-course-labs/ansible$ ansible-inventory -i inventory/default_aws_ec2.yml --list
{
    "_meta": {
        "hostvars": {
            "158.160.159.213": {
                "ansible_ssh_private_key_file": "~/.ssh/id_rsa",
                "ansible_user": "admin"
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
            "158.160.159.213"
        ]
    }
}
```

```sh
tedor49@tedor49:~/S25-core-course-labs/ansible$ ansible-inventory -i inventory/default_aws_ec2.yml --graph
@all:
  |--@ungrouped:
  |--@ec2:
  |  |--158.160.159.213
```
