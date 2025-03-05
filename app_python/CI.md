# CI Workflow best practices

## **1. Workflow Status Badge**

* Added a **GitHub Actions status badge** in `README.md`.
* Helps track **build status** at a glance.

## **2. Python Dependency Caching**

* Used `actions/cache` to **cache Python dependencies**.
* Significantly **reduces pipeline execution time**.

## **3. Docker Build Optimization**

* Enabled **Docker Layer Caching** to **reuse existing image layers**.
* Speeds up the build process and reduces resource usage.

## **4. Linting for Code Quality**

* Integrated `flake8` to **enforce Python coding standards**.
* Runs **before testing**, preventing formatting errors early.
* Uses `--max-line-length=100` for readable code.
