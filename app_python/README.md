# Python Time Display Application

This application shows current time in the provided timezone at endpoint `/`.

Timezone, host and port by default are `Europe/Moscow`, `0.0.0.0` and `8080` respectively, but they can be changed
with command line arguments.

## Usage

```shell
git clone https://github.com/UniLeonid/S25-core-course-labs
cd S25-core-course-labs
git checkout origin/lab1
cd app_python
```

It is highly recommended to [use venv](https://docs.python.org/3/library/venv.html) to avoid any possible problem
with package versions.

```shell
pip install -r requirements.txt
python app_start.py
```

You can run `python app_start.py -h` to get information about all available arguments.

## Docker

### Build

```shell
git clone https://github.com/UniLeonid/S25-core-course-labs
cd S25-core-course-labs
git checkout origin/lab1
cd app_python

docker build . --tag 'unileonid/time-app-py:latest'
```

### Pull

Also, you can get image from [Docker Hub](https://hub.docker.com/r/unileonid/time-app-py):

```shell
docker pull unileonid/time-app-py:latest
```

### Run

```shell
docker run -p 8080:8080 unileonid/time-app-py:latest
```

Timezone for the app can be changed via `APP_TIMEZONE` environment variable (it is `Europe/Moscow` by default).
