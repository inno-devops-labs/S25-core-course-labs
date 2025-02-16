# Web App Role - Ansible

## Overview

This Ansible role **deploys a web application** using **Docker and Docker Compose**. It supports deploying both **Python** and **Node.js applications**, ensuring they run concurrently without conflicts.

## Requirements

- **Ansible 2.9+**
- **Ubuntu 22.04+**
- **Docker and Docker Compose installed**

## Role Variables

This role uses the following variables, which are defined in `defaults/main.yml`:

```yaml
docker_image_python: "em1999jay/python-app"
docker_image_node: "em1999jay/moscow-time-app-node:v1"

app_python_port: "5000"
app_node_port: "7000"

web_app_full_wipe: false  # Can be set to true for wipe logic
```

### **Custom Variables Passed by Playbooks**

- **Python Playbook (`app_python/main.yaml`)**
  - Uses `docker_image_python` and `app_python_port`
- **Node.js Playbook (`app_node/main.yaml`)**
  - Uses `docker_image_node` and `app_node_port`

## Tasks

This role performs the following tasks:

1. **Pulls the Docker images** for Python and Node.js.
2. **Creates separate directories** for Python and Node.js applications (`/home/ubuntu/python_app` and `/home/ubuntu/node_app`).
3. **Deploys the correct `docker-compose.yml` file** based on the playbook.
4. **Starts the application using Docker Compose v2**.

## Usage

This role is used in three different playbooks:

### **1️⃣ `main.yaml` (Docker Setup Only)**

```yaml
- name: Setup Docker Environment
  hosts: all
  become: true
  roles:
    - docker
```

### **2️⃣ `app_python/main.yaml` (Deploys Python + Docker)**

```yaml
- name: Setup Docker and Deploy Python Application
  hosts: all
  become: true
  roles:
    - docker
    - web_app
  vars:
    app_port: "{{ app_python_port }}"
```

### **3️⃣ `app_node/main.yaml` (Deploys Node.js + Docker)**

```yaml
- name: Deploy Node.js Application
  hosts: all
  become: true
  roles:
    - docker
    - web_app
  vars:
    app_port: "{{ app_node_port }}"
```

## Example Playbook

Example usage in a custom playbook:

```yaml
- name: Deploy Web Applications
  hosts: all
  become: true
  roles:
    - web_app
```

## Dependencies

This role depends on:

```yaml
dependencies:
  - role: docker
```

## Verification

After running the playbooks, verify deployment using:

```sh
docker ps
```

Expected Output:

```sh
CONTAINER ID   IMAGE                  PORTS                   STATUS
4f0b6c5fb044   em1999jay/python-app  0.0.0.0:5000->5000/tcp   Up 5 minutes
7g9a3x1cb072   em1999jay/moscow-time-app-node:v1  0.0.0.0:7000->7000/tcp   Up 5 minutes
```
