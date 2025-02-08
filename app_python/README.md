# Moscow Time App

Simple Flask web application for displaying the exact current time in Moscow.

## 🐋 Docker

### Build from source

```shell 
docker build -t innoenjoyer/moscow-time-app .
```

### Pull from DockerHub

```shell
docker pull innoenjoyer/moscow-time-app
```

### Run

```shell
docker run -it -p 5000:5000 innoenjoyer/moscow-time-app
```

## ⬇️ Clone & Setup

1. Download and install the latest version of [Python 3](https://www.python.org/downloads/)
2. Ensure that you have pip installed:

    ```shell
    python -m ensurepip --upgrade
    ```

3. Clone this project:

    ```shell
    git clone https://github.com/innoenjoyer/S25-core-course-labs.git
    ```

4. Go to `app_python` directory
5. Set up virtual environment (optional):

    ```shell
    pip install virtualenv
    python -m venv venv
    ```

   On Windows, run:

    ```shell
    .\venv\Scripts\activate.bat
    ```

   On Unix or MacOS, run:

    ```shell
    source venv/bin/activate
    ```

6. Install the requirements:

    ```shell
    pip install -r requirements.txt
    ```

## 🚀 Run

```shell
python app.py
```

Access the application running on `http://127.0.0.1:5000`

## ✔️ Code linting & formatting

```shell
ruff check --fix
```

```shell
ruff format
```

## ✨ Features

- [x] Display current Moscow time
- [ ] Dockerize application
- [ ] Code Testing
- [ ] CI workflows
