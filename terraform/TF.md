# Terrafom lab4 
## Best practice for Terraform'irovanie 
1. Structuring code into directories (docker, github, yandex).
2. Using environment variables in .tf files.
3. Separating configuration from secrets, improving the security of token storage.
4. Enabling branch protection in GitHub.

## Docker terraform
1. All the work to install Terraform and the infrastructure for Docker Terraform was completed. A `docker_terraform` directory was created, containing the necessary files to run Terraform.
2. Output of the commands specified in the task:

    **terraform state list**
    ```
    docker_container.golang_app
    docker_container.python_app
    docker_image.golang_app
    docker_image.python_app
    ```
    **terraform state show docker_container.golang_app**
    ```
    # docker_container.golang_app:
    resource "docker_container" "golang_app" {
        attach                                      = false
        bridge                                      = null
        command                                     = [
            "./main",
        ]
        container_read_refresh_timeout_milliseconds = 15000
        cpu_set                                     = null
        cpu_shares                                  = 0
        domainname                                  = null
        entrypoint                                  = []
        env                                         = []
        hostname                                    = "c8a87f61c567"
        id                                          = "c8a87f61c5676a652af09bd0d6b70cd57f58132da2ec8dacba7e192a6e0ba326"
        image                                       = "sha256:bcc873f47aa43d96bc26ff7905e9af1060a654d8ea6a24bd1f86cc72058f6cc3"
        init                                        = false
        ipc_mode                                    = "private"
        log_driver                                  = "json-file"
        logs                                        = false
        max_retry_count                             = 0
        memory                                      = 0
        memory_swap                                 = 0
        must_run                                    = true
        name                                        = "new-golang-name"
        network_data                                = [
            {
                gateway                   = "172.17.0.1"
                global_ipv6_address       = null
                global_ipv6_prefix_length = 0
                ip_address                = "172.17.0.2"
                ip_prefix_length          = 16
                ipv6_gateway              = null
                mac_address               = "02:42:ac:11:00:02"
                network_name              = "bridge"
            },
        ]
        network_mode                                = "bridge"
        pid_mode                                    = null
        privileged                                  = false
        publish_all_ports                           = false
        read_only                                   = false
        remove_volumes                              = true
        restart                                     = "no"
        rm                                          = false
        runtime                                     = "runc"
        security_opts                               = []
        shm_size                                    = 64
        start                                       = true
        stdin_open                                  = false
        stop_signal                                 = null
        stop_timeout                                = 0
        tty                                         = false
        user                                        = "user"
        userns_mode                                 = null
        wait                                        = false
        wait_timeout                                = 60
        working_dir                                 = "/app_go"

        ports {
            external = 8001
            internal = 8000
            ip       = "0.0.0.0"
            protocol = "tcp"
        }
    }
    ```
    **terraform state show docker_container.python_app**
    ```
    # docker_container.python_app:
    resource "docker_container" "python_app" {
        attach                                      = false
        bridge                                      = null
        command                                     = [
            "uvicorn",
            "app:app",
            "--host",
            "0.0.0.0",
            "--port",
            "8000",
        ]
        container_read_refresh_timeout_milliseconds = 15000
        cpu_set                                     = null
        cpu_shares                                  = 0
        domainname                                  = null
        entrypoint                                  = []
        env                                         = []
        hostname                                    = "04286bcd7186"
        id                                          = "04286bcd718692d2b623d3c9c23dba2255cf5a2086574c780e8cb27ee42bc1f2"
        image                                       = "sha256:36868c695488228643e0b3594e3c841dacb2d0f2b9dc8e7db5e0fb8363d9f418"
        init                                        = false
        ipc_mode                                    = "private"
        log_driver                                  = "json-file"
        logs                                        = false
        max_retry_count                             = 0
        memory                                      = 0
        memory_swap                                 = 0
        must_run                                    = true
        name                                        = "new-python-name"
        network_data                                = [
            {
                gateway                   = "172.17.0.1"
                global_ipv6_address       = null
                global_ipv6_prefix_length = 0
                ip_address                = "172.17.0.3"
                ip_prefix_length          = 16
                ipv6_gateway              = null
                mac_address               = "02:42:ac:11:00:03"
                network_name              = "bridge"
            },
        ]
        network_mode                                = "bridge"
        pid_mode                                    = null
        privileged                                  = false
        publish_all_ports                           = false
        read_only                                   = false
        remove_volumes                              = true
        restart                                     = "no"
        rm                                          = false
        runtime                                     = "runc"
        security_opts                               = []
        shm_size                                    = 64
        start                                       = true
        stdin_open                                  = false
        stop_signal                                 = null
        stop_timeout                                = 0
        tty                                         = false
        user                                        = "user"
        userns_mode                                 = null
        wait                                        = false
        wait_timeout                                = 60
        working_dir                                 = "/app_python"

        ports {
            external = 8000
            internal = 8000
            ip       = "0.0.0.0"
            protocol = "tcp"
        }
    }
    ```
    **terraform state show docker_image.golang_app**
    ```
    # docker_image.golang_app:
    resource "docker_image" "golang_app" {
        id           = "sha256:bcc873f47aa43d96bc26ff7905e9af1060a654d8ea6a24bd1f86cc72058f6cc3lekski/golang-web-app:latest"
        image_id     = "sha256:bcc873f47aa43d96bc26ff7905e9af1060a654d8ea6a24bd1f86cc72058f6cc3"
        keep_locally = false
        name         = "lekski/golang-web-app:latest"
        repo_digest  = "lekski/golang-web-app@sha256:a8ccd47783b072f41dc5a8c385af1c5e6f1d8b39b8d0c7f2490d96564f570bc9"
    }
    ```

    **terraform state show docker_image.python_app**
    ```
    # docker_image.python_app:
    resource "docker_image" "python_app" {
        id           = "sha256:36868c695488228643e0b3594e3c841dacb2d0f2b9dc8e7db5e0fb8363d9f418lekski/python-web-app:latest"
        image_id     = "sha256:36868c695488228643e0b3594e3c841dacb2d0f2b9dc8e7db5e0fb8363d9f418"
        keep_locally = false
        name         = "lekski/python-web-app:latest"
        repo_digest  = "lekski/python-web-app@sha256:ee003098d1672bebf820f6dcfb7b70502e5cda62f5669d905ae01e5d6871fa30"
    }
    ```

    **terraform output**
    ```
    golang_container_info = {
    "ip_address" = "172.17.0.2"
    "name" = "new-golang-name"
    "ports" = tolist([
        {
        "external" = 8001
        "internal" = 8000
        "ip" = "0.0.0.0"
        "protocol" = "tcp"
        },
    ])
    }
    python_container_info = {
    "ip_address" = "172.17.0.3"
    "name" = "new-python-name"
    "ports" = tolist([
        {
        "external" = 8000
        "internal" = 8000
        "ip" = "0.0.0.0"
        "protocol" = "tcp"
        },
    ])
    }
    ```
3. Result: Looking at the obtained results and accessing the web-app applications through the browser, everything was configured correctly.

## Github terraform

1. I configured the infrastructure for GitHub as specified in the link in the lab assignment and then applied it.
2. Below are the commands I applied.
   **terraform plan -out deploy.tfplan**
   ```
    lekski@LAPTOP-EA8M0FT5:/mnt/c/Users/Honor/Desktop/S25-core-course-labs/terraform/github_terraform$ terraform plan -out deploy.tfplan

    Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
    + create

    Terraform will perform the following actions:

    # github_branch_default.master will be created
    + resource "github_branch_default" "master" {
        + branch     = "master"
        + etag       = (known after apply)
        + id         = (known after apply)
        + rename     = false
        + repository = "S25-core-course-labs-github-terraform"
        }

    # github_branch_protection.default will be created
    + resource "github_branch_protection" "default" {
        + allows_deletions                = false
        + allows_force_pushes             = false
        + enforce_admins                  = true
        + id                              = (known after apply)
        + lock_branch                     = false
        + pattern                         = "master"
        + repository_id                   = (known after apply)
        + require_conversation_resolution = true
        + require_signed_commits          = false
        + required_linear_history         = false

        + required_pull_request_reviews {
            + require_last_push_approval      = false
            + required_approving_review_count = 1
            }
        }

    # github_repository.repo will be created
    + resource "github_repository" "repo" {
        + allow_auto_merge            = false
        + allow_merge_commit          = true
        + allow_rebase_merge          = true
        + allow_squash_merge          = true
        + archived                    = false
        + auto_init                   = true
        + default_branch              = (known after apply)
        + delete_branch_on_merge      = false
        + description                 = "devops course repository "
        + etag                        = (known after apply)
        + full_name                   = (known after apply)
        + git_clone_url               = (known after apply)
        + gitignore_template          = "VisualStudio"
        + has_issues                  = true
        + has_wiki                    = true
        + html_url                    = (known after apply)
        + http_clone_url              = (known after apply)
        + id                          = (known after apply)
        + merge_commit_message        = "PR_TITLE"
        + merge_commit_title          = "MERGE_MESSAGE"
        + name                        = "S25-core-course-labs-github-terraform"
        + node_id                     = (known after apply)
        + primary_language            = (known after apply)
        + private                     = (known after apply)
        + repo_id                     = (known after apply)
        + squash_merge_commit_message = "COMMIT_MESSAGES"
        + squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
        + ssh_clone_url               = (known after apply)
        + svn_url                     = (known after apply)
        + topics                      = (known after apply)
        + visibility                  = "public"
        + web_commit_signoff_required = false

        + security_and_analysis (known after apply)
        }

    Plan: 3 to add, 0 to change, 0 to destroy.
    ```
3. Specify the PAT token in `config.auto.tfvars`
4. Run `terraform import github_repository.repo Lekski1/S25-core-course-labs`
    ```
    lekski@LAPTOP-EA8M0FT5:/mnt/c/Users/Honor/Desktop/S25-core-course-labs/terraform/github_terraform$ terraform import github_repository.repo S25-core-course-labs
    github_repository.repo: Importing from ID "S25-core-course-labs"...
    github_repository.repo: Import prepared!
    Prepared github_repository for import
    github_repository.repo: Refreshing state... [id=S25-core-course-labs]

    Import successful!

    The resources that were imported are shown above. These resources are now in
    your Terraform state and will henceforth be managed by Terraform.
    ```
    **terraform apply**
    ```
    lekski@LAPTOP-EA8M0FT5:/mnt/c/Users/Honor/Desktop/S25-core-course-labs/terraform/github_terraform$ terraform apply
    github_repository.repo: Refreshing state... [id=S25-core-course-labs]

    Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
    + create

    Terraform will perform the following actions:

    # github_branch_default.master will be created
    + resource "github_branch_default" "master" {
        + branch     = "master"
        + etag       = (known after apply)
        + id         = (known after apply)
        + rename     = false
        + repository = "S25-core-course-labs"
        }

    # github_branch_protection.default will be created
    + resource "github_branch_protection" "default" {
        + allows_deletions                = false
        + allows_force_pushes             = false
        + enforce_admins                  = true
        + id                              = (known after apply)
        + lock_branch                     = false
        + pattern                         = "master"
        + repository_id                   = "S25-core-course-labs"
        + require_conversation_resolution = true
        + require_signed_commits          = false
        + required_linear_history         = false

        + required_pull_request_reviews {
            + require_last_push_approval      = false
            + required_approving_review_count = 1
            }
        }

    Plan: 2 to add, 0 to change, 0 to destroy.

    Do you want to perform these actions?
    Terraform will perform the actions described above.
    Only 'yes' will be accepted to approve.

    Enter a value: yes

    github_branch_default.master: Creating...
    github_branch_default.master: Creation complete after 2s [id=S25-core-course-labs]
    github_branch_protection.default: Creating...
    github_branch_protection.default: Creation complete after 5s [id=BPR_kwDONu8XLs4DiUdV]

    Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
    ```

## Github-team terraform 
1. I created a test organization and a new directory for the .tf files for this task, and then followed the instructions for creating the infrastructure for GitHub teams for Terraform that were found online.
2. The commands I used are listed below.
    **terraform plan**
    ```

    Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
    + create

    Terraform will perform the following actions:

    # github_branch_default.master will be created
    + resource "github_branch_default" "master" {
        + branch     = "master"
        + etag       = (known after apply)
        + id         = (known after apply)
        + rename     = false
        + repository = "github_teams_test"
        }

    # github_branch_protection.default will be created
    + resource "github_branch_protection" "default" {
        + allows_deletions                = false
        + allows_force_pushes             = false
        + enforce_admins                  = true
        + id                              = (known after apply)
        + lock_branch                     = false
        + pattern                         = "master"
        + repository_id                   = (known after apply)
        + require_conversation_resolution = true
        + require_signed_commits          = false
        + required_linear_history         = false

        + required_pull_request_reviews {
            + require_last_push_approval      = false
            + required_approving_review_count = 1
            }
        }

    # github_repository.repo will be created
    + resource "github_repository" "repo" {
        + allow_auto_merge            = false
        + allow_merge_commit          = true
        + allow_rebase_merge          = true
        + allow_squash_merge          = true
        + archived                    = false
        + auto_init                   = true
        + default_branch              = (known after apply)
        + delete_branch_on_merge      = false
        + description                 = "repo for devops course lab4"
        + etag                        = (known after apply)
        + full_name                   = (known after apply)
        + git_clone_url               = (known after apply)
        + gitignore_template          = "VisualStudio"
        + has_issues                  = true
        + has_wiki                    = true
        + html_url                    = (known after apply)
        + http_clone_url              = (known after apply)
        + id                          = (known after apply)
        + merge_commit_message        = "PR_TITLE"
        + merge_commit_title          = "MERGE_MESSAGE"
        + name                        = "github_teams_test"
        + node_id                     = (known after apply)
        + primary_language            = (known after apply)
        + private                     = (known after apply)
        + repo_id                     = (known after apply)
        + squash_merge_commit_message = "COMMIT_MESSAGES"
        + squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
        + ssh_clone_url               = (known after apply)
        + svn_url                     = (known after apply)
        + topics                      = (known after apply)
        + visibility                  = "public"
        + web_commit_signoff_required = false

        + security_and_analysis (known after apply)
        }

    # github_team.dev will be created
    + resource "github_team" "dev" {
        + create_default_maintainer = false
        + description               = "Team responsible for development"
        + etag                      = (known after apply)
        + id                        = (known after apply)
        + members_count             = (known after apply)
        + name                      = "Developers"
        + node_id                   = (known after apply)
        + parent_team_read_id       = (known after apply)
        + parent_team_read_slug     = (known after apply)
        + privacy                   = "closed"
        + slug                      = (known after apply)
        }

    # github_team.qa will be created
    + resource "github_team" "qa" {
        + create_default_maintainer = false
        + description               = "Quality Assurance team"
        + etag                      = (known after apply)
        + id                        = (known after apply)
        + members_count             = (known after apply)
        + name                      = "QA"
        + node_id                   = (known after apply)
        + parent_team_read_id       = (known after apply)
        + parent_team_read_slug     = (known after apply)
        + privacy                   = "closed"
        + slug                      = (known after apply)
        }

    # github_team_repository.dev_access will be created
    + resource "github_team_repository" "dev_access" {
        + etag       = (known after apply)
        + id         = (known after apply)
        + permission = "push"
        + repository = "github_teams_test"
        + team_id    = (known after apply)
        }

    # github_team_repository.qa_access will be created
    + resource "github_team_repository" "qa_access" {
        + etag       = (known after apply)
        + id         = (known after apply)
        + permission = "pull"
        + repository = "github_teams_test"
        + team_id    = (known after apply)
        }

    Plan: 7 to add, 0 to change, 0 to destroy.
    ```
3. Then I ran `terraform apply`, and below in the screenshot, you can see confirmation that it worked.
    ![alt text](bonus_task_image.png)