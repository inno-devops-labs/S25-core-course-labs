# Continuous Integration (CI) Best Practices

## Status Badge
A workflow status badge is added to the README for visibility:
[![Python package](https://github.com/RwKaLs/S25-core-course-labs/actions/workflows/python-ci.yml/badge.svg?branch=lab3)](https://github.com/RwKaLs/S25-core-course-labs/actions/workflows/python-ci.yml)

## CI Best Practices
- **Minimize Job Dependencies:** jobs are as independent as possible to speed up the workflow
- **Cache Dependencies:** caching is implemented to speed up repetitive tasks, like dependency installation
- **Use the Latest Actions:** ensure the usage of the latest versions to benefit from improvements

## Enhancements
- **Automatic Code Formatting:** `black` usage for code style
- **Static Code Analysis:** `bandit` usage to identify security issues

Refer to the `.github/workflows/python-ci.yml` file to see the configuration.
