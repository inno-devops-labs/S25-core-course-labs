# web_app role

Deploys and manages a web app. Uses Docker.

Requirements:

- ubuntu 22+
- python 3.8+
- pip, apt
- ansible 2.10+

The web_app role depends on the docker role.

The playbook with the role can be ran inside the ansible folder with the following command:
```
ansible-playbook playbooks/dev/main.yml
```