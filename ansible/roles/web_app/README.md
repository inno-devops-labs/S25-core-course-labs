# Web App Role

This Ansible role automates the **deployment** of a web application using **Docker and Docker Compose**. It pulls the specified **Docker image**, configures the container, and ensures the service is up and running.

## **Requirements**

- **Ansible 2.9+**
- **Docker & Docker Compose installed** (via `docker` role)
- **Target system**: Ubuntu 22.04 (or another Linux-based OS)

## **Role Variables**

The role includes configurable variables in `defaults/main.yml`:

| Variable                 | Description                                   | Default Value  |
| ------------------------ | --------------------------------------------- | -------------- |
| `web_app_image`          | Docker image to pull                          | `nginx:latest` |
| `web_app_container_name` | Name of the web application container         | `web_app`      |
| `web_app_port`           | Port mapping for the application              | `8080`         |
| `web_app_full_wipe`      | Whether to remove existing containers & files | `false`        |

You can override these values in your playbook or `group_vars`.

## **Tasks Breakdown**

This role consists of the following structured **tasks**:

### **1. Wipe Logic (`0-wipe.yml`)**

If `web_app_full_wipe: true`, it:

- Stops & removes the **existing container**.
- Deletes the **application directory**.
- Removes the **Docker Compose file**.

### **2. Deploy Web Application (`tasks/main.yml`)**

The main deployment process includes:

- **Ensuring required directories exist**.
- **Generating `docker-compose.yml`** from a **Jinja2 template**.
- **Pulling the latest image**.
- **Launching the application** with **Docker Compose**.

## **Jinja2 Template: `docker-compose.yml.j2`**

This role uses a **Jinja2 template** for **Docker Compose**:

```yaml
version: "3"
services:
  app:
    image: "{{ web_app_image }}"
    container_name: "{{ web_app_container_name }}"
    ports:
      - "{{ web_app_port }}:80"
    restart: "always"
```

It allows customization via Ansible variables.

## **Role Dependencies**

This role depends on **`docker`**, ensuring Docker & Compose are installed first.

Defined in **`meta/main.yml`**:

```yaml
dependencies:
  - role: docker
```

## **Example Playbook**

Here’s how to use this role in your playbook:

```yaml
- name: Deploy web application
  hosts: all
  roles:
    - role: web_app
      vars:
        web_app_image: "my-app-image:latest"
        web_app_container_name: "my_web_app"
        web_app_port: 5000
        web_app_full_wipe: true
```

## **Tags for Selective Execution**

This role includes **Ansible tags** for flexibility:

| Tag      | Purpose                                                |
| -------- | ------------------------------------------------------ |
| `docker` | Runs only **Docker-related** tasks.                    |
| `wipe`   | Runs **only the wipe logic** (removes old containers). |

To run **only wipe tasks**:

```bash
ansible-playbook site.yml --tags wipe
```

To run **only Docker-related tasks**:

```bash
ansible-playbook site.yml --tags docker
```

## **Deployment Execution**

Run the playbook to deploy the application:

```bash
ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml
```

## **Validation**

- Check running containers:
  ```bash
  docker ps
  ```
- Validate `docker-compose.yml`:
  ```bash
  docker-compose config
  ```
- Inspect logs:
  ```bash
  docker logs web_app
  ```
