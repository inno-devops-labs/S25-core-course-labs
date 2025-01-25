# Python Sample Application

## Overview

This is a simple python web application that shows current time in Moscow.

## Installation

0. _Optional:_ activate nix-shell environment for Nix-based systems

```bash
    nix-shell -p python312 python312Packages.pip
```

1. Clone this repository and navigate to the project directory:

```bash
git clone https://github.com/raleksan/S25-core-course-labs -b lab1
cd S25-core-course-labs/app_python
```

2. Install virtual environment and dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

3. Run the application:

```bash
python3 app.py
```

4. Application usage

```bash
curl 127.0.0.1:5000
```

or open link from console `http://127.0.0.1:5000`
