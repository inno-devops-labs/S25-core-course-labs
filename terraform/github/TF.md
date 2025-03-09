```commandline
demanzverev@MacBook-Pro-Deman github % terraform import "github_repository.terraform-example" "terraform-example" 
var.token
  Specifies the GitHub token

  Enter a value: 

github_repository.terraform-example: Importing from ID "terraform-example"...
github_repository.terraform-example: Import prepared!
  Prepared github_repository for import
github_repository.terraform-example: Refreshing state... [id=terraform-example]

Import successful!

The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.

demanzverev@MacBook-Pro-Deman github % terraform apply
var.token
  Specifies the GitHub token

  Enter a value: 

github_repository.terraform-example: Refreshing state... [id=terraform-example]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
  ~ update in-place

Terraform will perform the following actions:

  # github_branch_default.main will be created
  + resource "github_branch_default" "main" {
      + branch     = "main"
      + etag       = (known after apply)
      + id         = (known after apply)
      + rename     = false
      + repository = "terraform-example"
    }

  # github_branch_protection.default will be created
  + resource "github_branch_protection" "default" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + blocks_creations                = false
      + enforce_admins                  = true
      + id                              = (known after apply)
      + lock_branch                     = false
      + pattern                         = "main"
      + repository_id                   = "terraform-example"
      + require_conversation_resolution = true
      + require_signed_commits          = false
      + required_linear_history         = false

      + required_pull_request_reviews {
          + require_last_push_approval      = false
          + required_approving_review_count = 1
        }
    }

  # github_repository.terraform-example will be updated in-place
  ~ resource "github_repository" "terraform-example" {
      ~ auto_init                   = false -> true
      + description                 = "Test terraform for creating repository"
      - has_downloads               = true -> null
      - has_projects                = true -> null
        id                          = "terraform-example"
      + license_template            = "mit"
        name                        = "terraform-example"
        # (32 unchanged attributes hidden)

        # (1 unchanged block hidden)
    }

Plan: 2 to add, 1 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_repository.terraform-example: Modifying... [id=terraform-example]
github_repository.terraform-example: Modifications complete after 1s [id=terraform-example]
github_branch_default.main: Creating...
github_branch_default.main: Creation complete after 1s [id=terraform-example]
github_branch_protection.default: Creating...
github_branch_protection.default: Creation complete after 4s [id=BPR_kwDON6d9IM4Dj2yX]

Apply complete! Resources: 2 added, 1 changed, 0 destroyed.

```