# Github CI best practices

[![CI Status](https://github.com/Raleksan/S25-core-course-labs/actions/workflows/app_rust.yaml/badge.svg)](https://github.com/Raleksan/S25-core-course-labs/actions/workflows/app_rust.yaml?event=push)

## 1. Set timeouts for each jobs

In order to prevent endless jobs that can be caused by misconfiguration,
deadlocks, etc.

## 2. Use actions with fixed versions

To improve stability & security of the pipeline.

## 3. Use Github Secrets with limited scopes

It's obvious that secrets must not be exposed. Moreover, it's generally more secure to use minimal required access rights as well.

## 4. Trigger workflow only in case when files are changed in a specific path

Obviously, there is no need to re-run the workflow if somebody changes markdown file or something in other folder (i.e. `app_python`).

## 5. Job dependencies

In case, for example, tests are failed - there is no need to push broken image onto Dockerhub. This let the workflow finish after fail faster.

## 6. Use caches

It's used for example, in `build_push` job in order to optimize future pipelines.
