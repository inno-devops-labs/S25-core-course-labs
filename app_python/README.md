# Python Moscow Time Web App

[![CI](https://github.com/dinaraparanid/devops/actions/workflows/python.yml/badge.svg?branch=lab3)](https://github.com/dinaraparanid/devops/actions/workflows/python.yml)

### Developer

[Arseny Savchenko](https://github.com/dinaraparanid)

### About App

Sample Flask web application that shows current time in Moscow.
Application utilizes [unittest](https://docs.python.org/3/library/unittest.html)
to ensure the accuracy of the results, regardless of network conditions.

### Preview

![preview.png](res/preview.png)

### Setup

* **Manual**

Build application with python interpreter:

1. Optional: create virtual environment:
   > python3 -m venv /path/to/venv

2. Install all necessary dependencies from the requirements.txt:
   > pip install -r requirements.txt

3. Run application on the localhost:
   > python3 app.py

* **Docker (Base Image)**

Build application with Docker (base image):

1. Pull image from DockerHub:
   > docker pull paranid5/app_piton

2. Run docker container:
   > docker run --rm -it -p <YOUR_PORT>:8080 paranid5/app_piton

3. Access web page:
   > curl http://127.0.0.1:<YOUR_PORT>

4. Optional: build image with Dockerfile:
   > docker build -t app_piton

* **Docker (Distroless Image)**

Build application with minimized Docker image:

1. Pull image from DockerHub:
   > docker pull paranid5/app_piton_dist

2. Run docker container:
   > docker run --rm -it -p <YOUR_PORT>:8080 paranid5/app_piton_dist

3. Access web page:
   > curl http://127.0.0.1:<YOUR_PORT>

4. Optional: build image with Dockerfile:
   > docker build -t app_piton_dist -f distroless.Dockerfile .

### Stack

<ul>
   <li>Python 3.9</li>
   <li>Flask 3.1.0</li>
   <li>Pytz 2024.2</li>
   <li>Unittest 3.9</li>
</ul>

## Unit tests

Two unit tests that check the correctness
of the primary web page can be found at `/tests` folder

Execute tests:
> python -m unittest app_python/tests/test_app.py

## CI

CI via GitHub Actions is established for the project (see /.github/workflows/python.yml):

1. Runner is observing changes in the app_python folder and in its own source code.
2. Runner utilizes *Python 3.9* and caches the dependencies from `requirements.txt`.
3. CI integrates *linter [flake8](https://flake8.pycqa.org/en/latest/)* to check the consistency of the code style.
4. Additionally, CI utilizes *Snyk* to check the project on known vulnerabilities
5. Finally, runner uses *DockerHub* to deploy a Docker image on each change
6. **Secrets** for DockerHub and Snyk are managed via GitHub Actions.
   See the documentation on the setup
   [here](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions).
