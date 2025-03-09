# Overview

# **Best Practices Implemented in Ansible Playbook**

## **1️ Rigorous Syntax Validation & Dry-Run Testing**  
Before deployment, the playbook undergoes **strict syntax validation** using the `--syntax-check` flag. This ensures error-free execution.  
Additionally, a **dry-run simulation** (`--check` flag) is performed to preview changes **without modifying the system**, providing confidence in the expected behavior.

---

## **2Efficient Service Management with Handlers**  
Handlers are implemented to **restart services only when necessary**, particularly for **Docker**.  
This approach:
- **Minimizes downtime**
- **Optimizes resource usage**
- **Ensures smooth playbook execution without unnecessary restarts**  

---

## **3️ Improved Readability & Maintainability**  
Each task includes a **clear and descriptive name**, making the playbook:  
 **Easier to read and understand**  
 **More maintainable for future modifications**  
 **Simpler to debug**, as errors and progress can be quickly identified  

---

## **4️ Secure Docker Configuration**  
The playbook enhances security by **restricting root access** to Docker.  
This is achieved by:  
 **Modifying the `daemon.json` file** with Ansible’s `copy` module.  
 **Ensuring a more secure and controlled Docker environment.**  

---

## **5️ Robust Pre-Deployment Validation**  
To prevent issues in production, the playbook undergoes **comprehensive pre-deployment checks**, including:  
 **Syntax validation** (`--syntax-check`)  
 **Dry-run execution** (`--check`)  
 **Configuration testing** before applying changes  

This proactive approach **reduces deployment risks and ensures reliability**.

## **`roles/docker` (Docker Installation & Management)**

### **🔹 `defaults/main.yml` (Configuration)**

Defines key Docker settings:

-   **Docker edition**: `ce` (Community) or `ee` (Enterprise).
-   **Package management**: Lists required Docker packages.
-   **Service management**: Ensures Docker starts automatically.
-   **Docker Compose**: Handles both **plugin** and **standalone installation**.
-   **Repositories**: Sets up Docker APT/YUM repositories based on the system.
-   **User management**: Adds specified users to the `docker` group.
-   **Daemon settings**: Configures Docker's runtime behavior.

### **🔹 `handlers/main.yml`**

Defines a **single handler**:

-   **`Restart docker`** → Restarts Docker service when changes occur.

### **🔹 `tasks/install_compose.yml`**

-   Installs **Docker Compose** using `pip3`, ensuring the latest version.

### **🔹 `tasks/install_docker.yml`**

-   Installs **Docker** using `apt` (for Debian-based systems).

### **🔹 `tasks/main.yml`**

-   Updates package cache.
-   Installs **Python 3 + pip3** (required for Ansible Docker modules).
-   Calls `install_docker.yml` and `install_compose.yml`.

* * *

## **🚀 `roles/web_app` (Web App Deployment & Management)**

### **🔹 `defaults/main.yml` (Configuration)**

Defines web app settings:

-   **Docker Image** → `suleimankrimeddin/app_python:latest`
-   **Container Name** → `web_app`
-   **Port Mapping** → Exposes container port `80` to host `3000`.

### **🔹 `handlers/main.yml`**

-   **`Restart web_app container`** → Restarts the container when needed.

### **🔹 `meta/main.yml`**

-   Defines **role dependencies** (`docker` must be installed before `web_app` runs).

### **🔹 `tasks/wipe.yml`**

-   **Stops and removes** the web app container.
-   Runs only if `web_app_wipe: true`.

### **🔹 `tasks/main.yml`**

Manages the **Dockerized web app**:

1.  **Pulls the latest Docker image**.
2.  **Ensures the container is running** with correct ports.
3.  **Handles full cleanup** (if requested).

### **🔹 `templates/docker-compose.yml.j2`**

Docker Compose template for managing the app container:

-   Uses `docker_image` and `docker_image_tag`.
-   Maps ports dynamically.
## Outputs

```shell


```shell
~/Desktop/S25-core-course-labs/ansible  ‹lab5*› $ ansible-playbook playbooks/dev/main.yaml --diff --check

PLAY [all] *********************************************************************

TASK [Gathering Facts] *********************************************************
Enter passphrase for key '/home/suleimankrimeddin/.ssh/lab/id_ed25519': 
ok: [host1]

TASK [docker : Update apt] *****************************************************
changed: [host1]

TASK [docker : Python3 and pip3 installation] **********************************
changed: [host1]

TASK [docker : Install docker] *************************************************
changed: [host1]

TASK [docker : Install docker compose] *****************************************
changed: [host1]

PLAY RECAP *********************************************************************
host1                      : ok=5    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```
~/Desktop/S25-core-course-labs/ansible  ‹lab6*› $ ansible-playbook playbooks/dev/main.yaml
PLAY [all] *********************************************************************
TASK [Gathering Facts] *********************************************************
Enter passphrase for key '/home/suleimankrimeddin/.ssh/lab/id_ed25519': 
ok: [host1]
TASK [docker : Update apt] *****************************************************
ok: [host1]
TASK [docker : Python3 and pip3 installation] **********************************
ok: [host1]
TASK [docker : Install docker] *************************************************
ok: [host1]
TASK [docker : Install docker compose] *****************************************
ok: [host1]
TASK [web_app : Pull Docker image] *********************************************
changed: [host1]
TASK [web_app : Run Docker container] ******************************************
changed: [host1]
PLAY RECAP *********************************************************************
host1                      : ok=7    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0    
```


```shell
~/Desktop/S25-core-course-labs/ansible  ‹lab5*› $ ansible-inventory -i inventory/default_lab.yml --list
{
    "_meta": {
        "hostvars": {
            "host1": {
                "ansible_host": "89.150.34.19",
                "ansible_user": "ubuntu"
            }
        }
    },
    "all": {
        "hosts": [
            "host1"
        ]
    }
}
~/Desktop/S25-core-course-labs/ansible  ‹lab5*› $ ansible-inventory -i inventory/default_lab.yml --graph
@all
 |--host1