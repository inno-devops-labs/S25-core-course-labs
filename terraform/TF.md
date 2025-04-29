# Terraform

## Best practices

- **Secrets managed by terraform variables**

- **Directories created accordingly to their tasks for better readability**

## Docker

1. `terraform state list`

![](image.png)

2. `terraform state show docker_container.app_python`

![](image-2.png)


3. `terraform apply`

![](image-3.png)

5. `terraform output`

![](image-7.png)

## Yandex Cloud

Since YandexCloud unaccessible without payment terraform files were created by tutorials only and were not tested.

## Github

1. `terraform import github_repository.repo S25-core-course-labs`

![alt text](image-9.png)

2. `terraform apply`

![alt text](image-8.png)