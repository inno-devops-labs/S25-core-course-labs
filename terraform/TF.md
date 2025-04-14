# Terraform Documentation

---

## Overview

In this repo, we demonstrate **Infrastructure as Code (IaC)** using Terraform. The repository is organized into **three** distinct infrastructures:

1. **Docker** (local containers)
2. **Yandex Cloud** (remote VM infrastructure)
3. **GitHub** (repository management)

We use **input variables**, **Terraform state**, and consistent documentation to ensure reproducible infrastructure across different environments.

---

## 1. Project Structure

A recommended folder layout under your `terraform/` directory:

```
./
├── app_python/
├── app_node/
├── terraform/
│   ├── docker/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   ├── yandex/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── provider.tf
│   ├── github/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── provider.tf
│   └── TF.md
└── ...
```

- **`docker/`**: All Terraform files for local Docker containers.
- **`yandex/`**: Terraform files for Yandex Cloud.
- **`github/`**: Terraform files for GitHub repository and branch protection.
- **`TF.md`**: High-level documentation describing how to set up and use each.

---

## 2. Terraform Installation

1. **Download Terraform** from [Terraform Downloads](https://developer.hashicorp.com/terraform/downloads) or use a package manager.

   - **macOS (Homebrew)**:
     ```bash
     brew tap hashicorp/tap
     brew install hashicorp/tap/terraform
     ```
   - **Linux**:
     ```bash
     wget https://releases.hashicorp.com/terraform/<version>/terraform_<version>_linux_amd64.zip
     unzip terraform_<version>_linux_amd64.zip
     sudo mv terraform /usr/local/bin/
     ```
   - **Windows**:
     1. Download the `.exe` file.
     2. Place it in a folder in your `%PATH%`.

2. **Verify** installation:
   ```bash
   terraform -v
   ```
   You should see something like:
   ```
   Terraform v1.10.5
   on darwin_arm64
   ```

---

## 3. Docker Infrastructure with Terraform

In the **`terraform/docker/`** folder, we define local Docker resources.

### 3.1 Configuration Files

Example:

- **`main.tf`**: Defines Docker provider, containers, images.
- **`variables.tf`**: Container names, ports, etc.
- **`outputs.tf`**: Exports resource info (like container IDs).

### 3.2 Usage

1. **Change to the Docker folder**:
   ```bash
   cd terraform/docker
   ```
2. **Initialize Terraform**:
   ```bash
   terraform init
   ```
3. **Plan**:
   ```bash
   terraform plan
   ```
   This shows what changes Terraform will apply.
4. **Apply**:
   ```bash
   terraform apply
   ```
   Type `yes` when prompted. Docker images and containers will be created.
5. **Validate**:
   ```bash
   docker ps
   ```
   You should see the running containers.

### 3.3 Key Commands & Outputs

- **terraform state show**:
  ```bash
  terraform state show docker_container.python-moscow-time
  ```
- **terraform state list**:
  ```bash
  terraform state list
  ```
- **terraform output**:
  ```bash
  terraform output
  ```

---

## 4. Yandex Cloud Infrastructure with Terraform

In the **`terraform/yandex/`** folder, we define resources for **Yandex Cloud**.

### 4.1 Prerequisites

1. **Yandex Cloud account** (free-tier or trial credits).
2. **Yandex CLI** installed:
   ```bash
   curl https://storage.yandexcloud.net/yandexcloud-yc/install.sh | bash
   yc init
   ```
3. **Terraform** installed (already covered).

### 4.2 Usage & Outputs

1. **Move to the Yandex folder**:
   ```bash
   cd terraform/yandex
   ```
2. **Set environment variables** (or pass `-var` flags):
   ```bash
   export TF_VAR_yc_token="<YOUR_YANDEX_TOKEN>"
   export TF_VAR_cloud_id="<YOUR_CLOUD_ID>"
   export TF_VAR_folder_id="<YOUR_FOLDER_ID>"
   ```
3. **Initialize, Plan, and Apply**:
   ```bash
   terraform init
   terraform plan
   terraform apply
   ```
4. **Check logs**:
   ```
   yandex_vpc_network.default: Creating...
   yandex_compute_instance.vm: Creating...
   Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
   ```
5. **Verify** in the Yandex Cloud console that your VM is running.
6. **Inspect state**:
   ```bash
   terraform state list
   terraform state show yandex_compute_instance.vm
   ```

---

## 5. GitHub Infrastructure with Terraform

In the **`terraform/github/`** folder, manage your GitHub repositories.

### 5.1 Prerequisites

1. **GitHub Personal Access Token** with `repo`, `admin:repo_hook`, etc.
2. **Export** it as an environment variable:
   ```bash
   export TF_VAR_github_token="<TOKEN>"
   ```

### 5.2 Usage & Importing Existing Repos

1. **Go to the GitHub folder**:
   ```bash
   cd terraform/github
   ```
2. **Initialize**:
   ```bash
   terraform init
   ```
3. **(Optional) Import an existing repo**:
   ```bash
   terraform import github_repository.core_course_labs <REPO_NAME>
   ```
4. **Plan & Apply**:
   ```bash
   terraform plan
   terraform apply
   ```
5. **Verify** in GitHub that the repo settings/branch protection are correct.

---

## 6. Challenges & Best Practices

1. **Separate Environments**: Docker, Yandex, and GitHub each have their own subfolders.
2. **Security**:
   - Store tokens in environment variables (e.g., `TF_VAR_github_token`, `TF_VAR_yc_token`).
   - Never commit tokens or `.tfstate` with credentials.
3. **Version Pinning**: Pin providers with `version = "~> X.Y"` to avoid breaking changes.
4. **Import vs. New**: Use `terraform import` when you have existing resources.
5. **SSH Key**: If you need SSH access to your Yandex VM, ensure `metadata.ssh-keys` is correct. If you don’t need SSH, you can remove it.
6. **Branch Protection**: Provide explicit rules (admin enforcement, required reviews) so your default branch is safe.

---

## 7. Conclusion

We used **Terraform** to manage:

1. **Docker containers** locally for quick app deployment.
2. **Yandex Cloud** infrastructure (VPC network, subnet, and a compute instance).
3. **GitHub repositories** (creation, default branch, and branch protection).
