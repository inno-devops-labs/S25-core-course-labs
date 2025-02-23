# Helm

## Lab 10: Introduction to Helm

## Task 1: Helm Setup and Chart Creation

The following screenshots demonstrate that I successfully installed Helm, configured Helm Chart for `moscow-time-app`
and installed Helm Chart on my Minikube cluster:

![helm_chart_installed.png](screenshots/helm_chart_installed.png)

![app_python_workloads.png](screenshots/app_python_workloads.png)

![app_python_accessible.png](screenshots/app_python_accessible.png)

![app_python_kubectl.png](screenshots/app_python_kubectl.png)

## Task 2: Helm Chart Hooks

The following screenshots demonstate that I successfully implemented
pre-install and post-install Helm Chart Hooks for `moscow-time-app`:

- Linter:

![lint.png](screenshots/lint.png)

- Install dry-run (the start of the output):
  ![dry_run.png](screenshots/dry_run.png)

- pre-install pod description (captured when the pod was alive):
  ![pre_describe.png](screenshots/pre_describe.png)

- post-install pod description (captured when the pod was alive):
  ![post_describe.png](screenshots/post_describe.png)

- pre-install, post-install and main applications pods lifecycle:
  ![pre_and_post.png](screenshots/pre_and_post.png)
  ![post_post_install.png](screenshots/post_post_install.png)
  We can see that firstly pre-install-hook pod was created.
  After 20s main app and post-install-hook pods were created,
  and pre-install-hook pod was deleted.
  After 20s more post-install-hook pod also deleted,
  and only main application pod left

- Final output after all hooks:
  ![final_output.png](screenshots/final_output.png)
