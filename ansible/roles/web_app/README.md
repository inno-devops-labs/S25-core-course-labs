# Web App Role

Ansible role for deploying Python Flask application using Docker.

## Requirements

- Docker
- Docker Compose V2
- Ansible 2.9+
- Python 3.x

## Dependencies

- geerlingguy.docker

## Quick Start

1. Install role:
```bash
ansible-galaxy install -r requirements.yml
```

2. Run playbook:
```bash
ansible-playbook playbook.yml
```

3. Check application:
```bash
curl http://localhost:8000/time
```

## Variables

| Variable | Description | Default |
|----------|-------------|---------|
| app_name | Application name | python-app |
| app_image | Docker image | marketer7/flask-time:latest |
| app_port | Application port | 8000 |
| deploy_user | Deployment user | m7 |
| web_app_full_wipe | Enable full cleanup | false |

## Tags

- `setup`: Environment setup
- `docker`: Docker operations
- `auth`: Authentication setup
- `deploy`: Application deployment
- `wipe`: Cleanup

## Configuration

### Environment Variables
```yaml
app_env:
  PYTHONUNBUFFERED: "1"
```

### Docker Compose Template
```yaml
version: '3.8'
services:
  app:
    image: {{ app_image }}
    container_name: {{ app_name }}
    restart: unless-stopped
    ports:
      - "{{ app_port }}:8000"
```

## Usage

### Standard deployment
```bash
ansible-playbook playbook.yml
```

### Deploy only
```bash
ansible-playbook playbook.yml --tags deploy
```

### Cleanup
```bash
ansible-playbook playbook.yml --tags wipe -e "web_app_full_wipe=true"
```

## Execution Examples

### Full deployment
```bash
$ ansible-playbook ansible/playbooks/dev/main.yaml -i ansible/inventory/default_aws_ec2.yml -K

PLAY RECAP ******************************************************************************
localhost : ok=37 changed=0 unreachable=0 failed=0 skipped=22 rescued=0 ignored=0

$ docker ps | grep python-app
5b20fa706ec4   marketer7/flask-time:latest   "python app.py"   59 seconds ago   Up 59 seconds   0.0.0.0:8000->8000/tcp   python-app

$ docker logs python-app
 * Serving Flask app 'app'
 * Debug mode: off
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8000
 * Running on http://172.19.0.2:8000
```

### Deploy only
```bash
$ ansible-playbook ansible/playbooks/dev/main.yaml -i ansible/inventory/default_aws_ec2.yml -K --tags deploy

PLAY RECAP ******************************************************************************
localhost : ok=5 changed=0 unreachable=0 failed=0 skipped=0 rescued=0 ignored=0
```

### Cleanup
```bash
$ ansible-playbook ansible/playbooks/dev/main.yaml -i ansible/inventory/default_aws_ec2.yml -K --tags wipe -e "web_app_full_wipe=true"

PLAY RECAP ******************************************************************************
localhost : ok=6 changed=3 unreachable=0 failed=0 skipped=0 rescued=0 ignored=0

$ docker ps | grep python-app
# Container successfully removed
```

## Maintenance

### Logs
```bash
docker logs python-app
```

### Health Check
```bash
curl http://localhost:8000/health
```

### Monitoring
```bash
docker stats python-app
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

MIT