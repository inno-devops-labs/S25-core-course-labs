# Ansible Implementation

## Playbook Output

```text
$ ansible-playbook playbooks/dev/main.yml --diff -K
BECOME password: 

PLAY [all] ***********************************************************************************

TASK [Gathering Facts] ***********************************************************************
[WARNING]: Platform linux on host my-vm is using the discovered Python interpreter at
/usr/bin/python3.12, but future installation of another Python interpreter could change the
meaning of that path. See https://docs.ansible.com/ansible-
core/2.18/reference_appendices/interpreter_discovery.html for more information.
ok: [my-vm]

TASK [docker : include_tasks] ****************************************************************
included: /home/ism/Projects/edu/S25-DevOps-labs/ansible/roles/docker/tasks/install_docker.yml for my-vm

TASK [docker : Install Docker dependencies] **************************************************
The following NEW packages will be installed:
  apt-transport-https
0 upgraded, 1 newly installed, 0 to remove and 111 not upgraded.
changed: [my-vm] => (item=apt-transport-https)
The following additional packages will be installed:
  openssl
The following NEW packages will be installed:
  ca-certificates openssl
0 upgraded, 2 newly installed, 0 to remove and 111 not upgraded.
changed: [my-vm] => (item=ca-certificates)
The following additional packages will be installed:
  appstream gir1.2-packagekitglib-1.0 libappstream5 libglib2.0-bin
  libgstreamer1.0-0 libpackagekit-glib2-18 libstemmer0d packagekit
  packagekit-tools python3-blinker python3-cryptography python3-httplib2
  python3-jwt python3-launchpadlib python3-lazr.restfulclient python3-lazr.uri
  python3-oauthlib python3-pyparsing python3-six python3-software-properties
  python3-wadllib
Suggested packages:
  apt-config-icons gstreamer1.0-tools python-blinker-doc
  python-cryptography-doc python3-cryptography-vectors python3-crypto
  python3-keyring python3-testresources python-pyparsing-doc
The following NEW packages will be installed:
  appstream gir1.2-packagekitglib-1.0 libappstream5 libglib2.0-bin
  libgstreamer1.0-0 libpackagekit-glib2-18 libstemmer0d packagekit
  packagekit-tools python3-blinker python3-cryptography python3-httplib2
  python3-jwt python3-launchpadlib python3-lazr.restfulclient python3-lazr.uri
  python3-oauthlib python3-pyparsing python3-six python3-software-properties
  python3-wadllib software-properties-common
0 upgraded, 22 newly installed, 0 to remove and 111 not upgraded.
changed: [my-vm] => (item=software-properties-common)

TASK [docker : Add Docker apt key.] **********************************************************
changed: [my-vm]

TASK [docker : Add Docker repository] ********************************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/docker.list
@@ -0,0 +1 @@
+deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu noble stable

changed: [my-vm]

TASK [docker : Install Docker] ***************************************************************
The following additional packages will be installed:
  libltdl7 pigz
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite
The following NEW packages will be installed:
  docker-ce libltdl7 pigz
0 upgraded, 3 newly installed, 0 to remove and 111 not upgraded.
changed: [my-vm]

TASK [docker : Start and enable Docker] ******************************************************
ok: [my-vm]

TASK [docker : Add user to docker group] *****************************************************
changed: [my-vm]

TASK [docker : Restart session to apply group changes] ***************************************

TASK [docker : include_tasks] ****************************************************************
included: /home/ism/Projects/edu/S25-DevOps-labs/ansible/roles/docker/tasks/install_compose.yml for my-vm

TASK [docker : Install Docker Compose Plugin] ************************************************
The following NEW packages will be installed:
  docker-compose-plugin
0 upgraded, 1 newly installed, 0 to remove and 111 not upgraded.
changed: [my-vm]

PLAY RECAP ***********************************************************************************
my-vm                      : ok=10   changed=6    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

## Inventory

The inventory is holding one virtual machine running Ubuntu Server set up with virtmanager.

```text
$ ansible-inventory -i inventory/my-vm.yml --list
{
    "_meta": {
        "hostvars": {
            "my-vm": {
                "ansible_host": "192.168.122.101",
                "ansible_port": 22,
                "ansible_ssh_private_key_file": "~/.ssh/id_ed25519",
                "ansible_user": "ism"
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
            "my-vm"
        ]
    }
}
```

```text
$ ansible-inventory -i inventory/my-vm.yml --graph
@all:
  |--@ungrouped:
  |  |--my-vm
```
