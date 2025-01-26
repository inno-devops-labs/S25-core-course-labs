# MSK Time application

## Overview

Simple web application for showing current MSK time. Time is returned as a JSON.

## Local installation

First, create virtual environment, example on pwsh:

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### With Task

> Taskfile is not required for this project to work properly, but it may increase performance of setup and runs by reducing and gathering routine commands. See how to [install](https://taskfile.dev/installation/).

Setup requirements and run:

```bash
task reqs-install run
```

On further reruns use only `task run`

See all available task commands by `task -l` (python specific ones). You can find original cmds in `Taskfile.yml`.

### Without Task

Install packages from requirements.txt

```bash
pip install -r app_python/requirements.txt
```

Run application

```bash
uvicorn app_python.main:app --port 8080 --reload
```

Run `curl http://127.0.0.1:8080/time/` to see that everything works (or go to this address in browser)
