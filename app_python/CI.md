## Applied best practice

* **Trigger workflow only on relevant events**: Workflow will be started if and only if there are push or PR to the
  `master` branch and at least one file at `app_python` directory was changed, excluding Markdown files.

* **Restrict privilege access for security**: Value by key `permissions.contents` is set to `read`, that is minimal
  needed permission.

* **Set Python version to `3.9`:** This allows us to avoid compatibility issues at the future.

* **Cache Python dependencies:**
* **Lint and test:** It ensures code quality and code integration.

* **Secure login to Docker Hub**: Secrets are used to hide personal access token from Docker Hub.

* **Use variables**: Variables are used in workflow to increase maintainability by reducing duplication of data that
  probably can be changed later.
