# Documentation

```yaml
  > ansible-playbook playbooks/dev/main.yaml --diff

  PLAY [Install Docker] **********************************************************************************************************************************************************************************

  TASK [Gathering Facts] *********************************************************************************************************************************************************************************
  [WARNING]: Platform linux on host localhost is using the discovered Python interpreter at /usr/bin/python3.12, but future installation of another Python interpreter could change the meaning of that
  path. See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more information.
  ok: [localhost]

  TASK [docker : Enable Docker to start on boot] *********************************************************************************************************************************************************
  ok: [localhost]

  PLAY RECAP *********************************************************************************************************************************************************************************************
  localhost                  : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

```yaml
  > ansible-inventory -i inventory/default_aws_ec2.yml --list
  {
      "_meta": {
          "hostvars": {
              "localhost": {
                  "ansible_connection": "local"
              }
          }
      },
      "all": {
          "children": [
              "ungrouped",
              "local"
          ]
      },
      "local": {
          "hosts": [
              "localhost"
          ]
      }
  }
```

```yaml
  > ansible-inventory -i inventory/default_aws_ec2.yml --graph
  @all:
    |--@ungrouped:
    |--@local:
    |  |--localhost
```
