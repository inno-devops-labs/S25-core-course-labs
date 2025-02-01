# CI Practices

Here I will describe the practices I used to write my GitHub Actions CI workflow.

## 1. Dependency Installation
Using `requirements.txt` for easy installation of necessary libraries without needing to list them individually.
```yaml
    - name: install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
```

## 2. Using Lint
Using Pylint to check code style and identify potential issues.
```yaml
    - name: Linter
      run: |
        pip install pylint
        pylint app.py
```

## 3. Automated Unit Testing
The project uses pre-written unit tests, which allows automatically checking the correctness of the application when changes are made to the project.
```yaml
    - name: UnitTests
      run: |
        python -m unittest unit_test/app_test.py -v
```

## 4. Dockerization of Applications
Using Dockerization of the application for deployment in various environments.
```yaml
    - name: docker build and push
      uses: docker/build-push-action@v4
      with:
        push: true
        tags: ${{ secrets.DOCKER_USERNAME }}/python-web-app:latest
        cache-from: type=gha,scope=public
        cache-to: type=gha,scope=public
```

## 5. Using Secrets for Security
GitHub Actions secrets are used to enhance the security of web-app deployment and securely store Docker profile information.
```yaml
    - name: Login to Docker
      uses: docker/login-action@v2
      with:
        username: ${{ secrets.DOCKER_USERNAME }}
        password: ${{ secrets.DOCKER_PASSWORD }}
```

## 6. Separation of deployment phases 
Instead of one common deployment phase, there are three different ones related to build, security and docker, which better helps to manage project deployment.  

## 7. Caching
Caching of `pip` and `docker build` is used in workflows to speed up builds and save resources.