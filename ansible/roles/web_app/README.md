web_app Ansible Role
=========

An Ansible Role deploying python webapp showing Moscow time.

Requirements
------------

- Docker
- Docker Compose V2
- Ansible 2.10+
- Python 3.x

Role Variables
--------------

| Variable | Description | Default |
|----------|-------------|---------|
| app_name | Application name | python-app |
| app_image | Docker image | tjann7/moscow_time:latest |
| app_port | External port | 5005 |
| deploy_user | Deployment user | tjann |
| web_app_full_wipe | Enable full cleanup | false |

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Quick Start
-------

### Standard deployment
```bash
ansible-playbook playbook.yml
```

### Deploy only
```bash
ansible-playbook playbook.yml --tags deploy
```

### Check application - via VM terminal
```bash
curl http://localhost:5005
```

### Cleanup
```bash
ansible-playbook playbook.yml --tags wipe -e "web_app_full_wipe=true"
```

Execution Examples
------------------



Afterwards, the user can request the port in VM's terminal:

```bash
tjann@fhmm5i5qjoo0bl0si2gd:~$ curl localhost:5005
<!DOCTYPE html>
<h1>Moscow Time: 23:12:00 Moscow</h1>
<h2>Your Timezone: 20:12:00 </h2>
```

License
-------

BSD
