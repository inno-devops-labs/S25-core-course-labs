# Lab 4: Infrastructure as Code Lab

## Overview

In this lab assignment, you will explore Infrastructure as Code (IAC) using Terraform. You'll build Docker and AWS infrastructures and dive into managing GitHub repositories through Terraform. Additionally, there are bonus tasks to enhance your Terraform skills. Follow the tasks below to complete the lab assignment.

## Task 1: Introduction to Terraform

**6 Points:**

0. You will need a VPN tool for this lab

1. Get Familiar with Terraform:
   - Begin by familiarizing yourself with Terraform by reading the [introduction](https://www.terraform.io/intro/index.html) and exploring [best practices](https://www.terraform.io/docs/cloud/guides/recommended-practices/index.html).

2. Set Up Terraform Workspace:
   - Create a `terraform` folder to organize your Terraform workspaces.
   - Inside the `terraform` folder, create a file named `TF.md`.

3. Docker Infrastructure Using Terraform:
   - Follow the [Docker tutorial](https://learn.hashicorp.com/collections/terraform/docker-get-started) for building a Docker infrastructure with Terraform.
   - Perform the following tasks as instructed in the tutorial:
      - Install Terraform.
      - Build the Infrastructure.
      - Provide the output of the following commands in the `TF.md` file:

        ```sh
            terraform state show
            terraform state list
        ```

      - Document a part of the log with the applied changes.
      - Utilize input variables to rename your Docker container.
      - Finish the tutorial and provide the output of the `terraform output` command in the `TF.md` file.

4. Yandex Cloud Infrastracture Using Terraform:
   - Create an account on [Yandex Cloud](https://cloud.yandex.com/).
   - Check for available free-tier options and select a free VM instance suitable for this lab.
   - Follow the [Yandex Quickstart Guide](https://yandex.cloud/en-ru/docs/tutorials/infrastructure-management/terraform-quickstart#linux_1) to set up and configure Terraform for managing Yandex Cloud resources.
   - Document the entire process, including setup steps, configurations, and any challenges encountered, in the `TF.md` file.

5. [Optioinal] AWS Infrastructure Using Terraform:
   - Follow the [AWS tutorial](https://learn.hashicorp.com/tutorials/terraform/aws-build?in=terraform/aws-get-started) alongside the instructions from the previous step.

## Task 2: Terraform for GitHub

**4 Points:**

1. GitHub Infrastructure Using Terraform:
   - Utilize the [GitHub provider for Terraform](https://registry.terraform.io/providers/integrations/github/latest/docs).
   - Create a directory inside the `terraform` folder specifically for managing your GitHub project infrastructure.
   - Build GitHub infrastructure following a reference like [this example](https://dev.to/pwd9000/manage-and-maintain-github-with-terraform-2k86). Prepare `.tf` files that include:
      - Repository name
      - Repository description
      - Visibility settings
      - Default branch
      - Branch protection rule for the default branch
   - Avoid placing your token as a variable in the code; instead, use an environment variable.

2. Import Existing Repository:
   - Use the `terraform import` command to import your current GitHub repository into your Terraform configuration. No need to create a new one. Example: `terraform import "github_repository.core-course-labs" "core-course-labs"`.

3. Apply Terraform Changes:
   - Apply changes from your Terraform configuration to your GitHub repository.

4. Document Best Practices:
   - Provide Terraform-related best practices that you applied in the `TF.md` file.

## Bonus Task: Adding Teams

**2.5 Points:**

1. GitHub Teams Using Terraform:
   - You need to upgrade your account to organization.
   - Extend your Terraform configuration to add several teams to your GitHub repository, each with different levels of access.
   - Apply the changes and ensure they take effect in your GitHub repository.

### Guidelines

- Use proper Markdown formatting and structure for documentation files.
- Organize files within the lab folder with suitable naming conventions.
- Create pull requests (PRs) as needed: from your fork to the main branch of this repository, and from your fork's branch to your fork's master branch.

> Note: Dive into Terraform to manage infrastructures efficiently. Explore the AWS and Docker tutorials, and don't forget to document your process and best practices in the `TF.md` file.
