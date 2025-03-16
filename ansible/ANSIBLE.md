# **Ansible Inventory Report**  

First, I used [`geerlingguy.docker`](https://github.com/geerlingguy/ansible-role-docker) role, then created my own.

## **Docker role**

To complete the task I set up a docker role:

1. I specified docker and docker-compose versions in defaults/main.yml
2. I set up installation tasks for docker and compose in tasks/install_*.yml files
3. I imported them in tasks/main.yml and added needed steps to:
    - Enable docker start on boot
    - Enable user to use docker without `sudo`
    - Copy docker daemon configuration
4. Configured a dynamic inventory on AWS.
5. Launched everything using `ansible-playbook playbooks/dev/main.yml -i inventory`, and got the output below

---

**PLAY [Deploy Docker on Cloud VM]**  
*Warning:* Found variable using reserved name: `tags`  

**TASK [Gathering Facts]**  
✔ ec2-13-60-234-13.eu-north-1.compute.amazonaws.com  

**TASK [docker : include_tasks]**  
→ Included: `/home/justcgh9/projects/pet/DevOps/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml`  
→ Target: ec2-13-60-234-13.eu-north-1.compute.amazonaws.com  

**TASK [docker : Install required packages]**  
✔ ec2-13-60-234-13.eu-north-1.compute.amazonaws.com  

**TASK [docker : Create Docker keyring directory]**  
✔ ec2-13-60-234-13.eu-north-1.compute.amazonaws.com  

**TASK [docker : Download Docker GPG key]**  
✔ ec2-13-60-234-13.eu-north-1.compute.amazonaws.com  

**TASK [docker : Add Docker repository]**  
✔ ec2-13-60-234-13.eu-north-1.compute.amazonaws.com  

**TASK [docker : Install Docker packages]**  
✔ ec2-13-60-234-13.eu-north-1.compute.amazonaws.com  

**TASK [docker : include_tasks]**  
→ Included: `/home/justcgh9/projects/pet/DevOps/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml`  
→ Target: ec2-13-60-234-13.eu-north-1.compute.amazonaws.com  

**TASK [docker : Download Docker Compose binary]**  
✔ ec2-13-60-234-13.eu-north-1.compute.amazonaws.com  

**TASK [docker : Enable Docker service to start on boot]**  
✔ ec2-13-60-234-13.eu-north-1.compute.amazonaws.com  

**TASK [docker : Add current user to docker group]**  
✔ ec2-13-60-234-13.eu-north-1.compute.amazonaws.com  

**TASK [docker : Copy secure Docker daemon configuration]**  
✔ ec2-13-60-234-13.eu-north-1.compute.amazonaws.com  

---

**PLAY RECAP**  

| Host | OK | Changed | Unreachable | Failed | ⏭️ Skipped | 🛠️ Rescued | Ignored |  
|------|----|---------|-------------|--------|---------|---------|---------|  
| ec2-13-60-234-13.eu-north-1.compute.amazonaws.com | **12** | **0** | **0** | **0** | **0** | **0** | **0** |  

Deployment completed successfully.  

## **EC2 Instances**  

Dynamic Inventory

A dynamic inventory is set up using the AWS EC2 plugin. Ensure that your AWS credentials are correctly configured in your environment, if you want to replicate the experiment.

### **Instance Details**  

Here is the output of the following command, that I trimmed and grouped as a table

```bash
ansible-inventory -i inventory/default_aws_ec2.yml --list
```

| Property                | Value |
|-------------------------|----------------------------------------------|
| **Instance Name**       | Ansible-ec2 |
| **State**               | Running |
| **Public DNS Name**     | ec2-13-60-234-13.eu-north-1.compute.amazonaws.com |
| **Public IP Address**   | 13.60.234.13 |
| **Private DNS Name**    | ip-172-31-38-99.eu-north-1.compute.internal |
| **Private IP Address**  | 172.31.38.99 |
| **VPC ID**             | vpc-0bf0d8e6a16710288 |
| **Subnet ID**           | subnet-03e7d364cba5e0a06 |
| **Root Device**         | /dev/sda1 (EBS) |
| **Security Group**      | launch-wizard-1 (sg-031e6ce09e9e8d830) |
| **Virtualization Type** | HVM |

---

## **Inventory Groups**  

Here is the output of `ansible-inventory -i inventory/default_aws_ec2.yml --list`:

```bash
@all
├── @ungrouped
├── @aws_ec2 
│   ├── ec2-13-60-234-13.eu-north-1.compute.amazonaws.com 
├── @_Ansible_ec2
│   ├── ec2-13-60-234-13.eu-north-1.compute.amazonaws.com
```

## **Web App Deployment**

### Configuring Ansible

I have started with the bonus task from the beginning. I have created two playbooks, they're almost identical. What I do, is I pull the image from dockerhub and run it in a container using docker-compose. It is essential that you wipe if you want to stop one application and run another (or you may change the vm's running port, which is 80 by default in the docker-compose template). 

So, what I did was:

1. Set up dependencies
2. Provide variables
3. Create wipe and main tasks
4. Set up the playbooks

---

Below is the output of running command `ansible-playbook playbooks/dev/app_go/main.yml -i inventory`. I will only show one output, since they're completely identical. 

---

**PLAY [Deploy Go Application]**  
*Warning:* Found variable using reserved name: `tags`  

**TASK [Gathering Facts]**  
✔ ec2-13-60-234-13.eu-north-1.compute.amazonaws.com  

**TASK [docker : include_tasks]**  
→ Included: `/home/justcgh9/projects/pet/DevOps/S25-core-course-labs/ansible/roles/docker/tasks/install_docker.yml`  
→ Target: ec2-13-60-234-13.eu-north-1.compute.amazonaws.com  

**TASK [docker : Install required packages]**  
✔ ec2-13-60-234-13.eu-north-1.compute.amazonaws.com  

**TASK [docker : Create Docker keyring directory]**  
✔ ec2-13-60-234-13.eu-north-1.compute.amazonaws.com  

**TASK [docker : Download Docker GPG key]**  
✔ ec2-13-60-234-13.eu-north-1.compute.amazonaws.com  

**TASK [docker : Add Docker repository]**  
✔ ec2-13-60-234-13.eu-north-1.compute.amazonaws.com  

**TASK [docker : Install Docker packages]**  
✔ ec2-13-60-234-13.eu-north-1.compute.amazonaws.com  

**TASK [docker : include_tasks]**  
→ Included: `/home/justcgh9/projects/pet/DevOps/S25-core-course-labs/ansible/roles/docker/tasks/install_compose.yml`  
→ Target: ec2-13-60-234-13.eu-north-1.compute.amazonaws.com  

**TASK [docker : Download Docker Compose binary]**  
✔ ec2-13-60-234-13.eu-north-1.compute.amazonaws.com  

**TASK [docker : Enable Docker service to start on boot]**  
✔ ec2-13-60-234-13.eu-north-1.compute.amazonaws.com  

**TASK [docker : Add current user to docker group]**  
✔ ec2-13-60-234-13.eu-north-1.compute.amazonaws.com  

**TASK [docker : Copy secure Docker daemon configuration]**  
✔ ec2-13-60-234-13.eu-north-1.compute.amazonaws.com  

---

**TASK [web_app : Pull Docker image for web application]**  
✔ ec2-13-60-234-13.eu-north-1.compute.amazonaws.com  

**TASK [web_app : Ensure deployment directory exists]**  
✔ ec2-13-60-234-13.eu-north-1.compute.amazonaws.com  

**TASK [web_app : Render docker-compose file for web application]**  
✔ ec2-13-60-234-13.eu-north-1.compute.amazonaws.com  

**TASK [web_app : Start web application container using docker-compose]**  
✱ Changed: ec2-13-60-234-13.eu-north-1.compute.amazonaws.com  

---

**PLAY RECAP**  
| Host | ✅ OK | 🔄 Changed | 🚫 Unreachable | ❌ Failed | ⏭️ Skipped | 🛠️ Rescued | 🔕 Ignored |  
|------|----|---------|-------------|--------|---------|---------|---------|  
| ec2-13-60-234-13.eu-north-1.compute.amazonaws.com | **16** | **1** | **0** | **0** | **0** | **0** | **0** |  

Deployment completed successfully.  

---

### AWS Configuration

After I did all the ansible work, I needed to adjust some inbound rules of the security group of the running instance, so that http port 80 would become available. Then, I was able to see my web app up and running completely fine. I am not sure when you will be checking this, but the [application](http://13.60.234.13/manage) may still be up. Below is the proof of work.

![url-shortener](/ansible/-2147483648_-231609.jpg)