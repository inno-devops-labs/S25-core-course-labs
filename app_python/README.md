# Current Moscow time web application

## Overview

This web application displays the current time in Moscow. It supports two formats of the output:

- Web page containing current time in Moscow
- JSON with current time in Moscow

## Tools

- [FastAPI](https://fastapi.tiangolo.com/)
- [Jinja2](https://pypi.org/project/Jinja2/)
- [Pydantic](https://docs.pydantic.dev/latest/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [Pylint](https://docs.pylint.org/)
- [Black](https://black.readthedocs.io/en/stable/)

## Installation

```bash
# 1. Clone the repository
git clone https://github.com/danmaninc/S25-core-course-labs

# 2. Change directory
cd S25-core-course-labs/app_python

# 3. Install the dependencies
pip install -r requirements.txt

# 4. Run the production server
fastapi run
```

## Testing

To test the application, you can compare the outputted time with the actual Moscow time ([resource](https://time100.ru)).
