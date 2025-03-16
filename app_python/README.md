# ![GitHub Workflow Status](https://github.com/oth33r/S25-core-course-labs/actions/workflows/app_python.yml/badge.svg)

## Steps

1. Clone repository using `git clone https://github.com/oth33r/S25-core-course-labs.git`
2. Checkout branch lab1 `git checkout lab1`
3. Go to `app_python` folder using `cd app_python`
4. Install all the requirements `pip install -r requirements.txt`
5. Start `uvicorn app:app --reload`

## Docker

First we need to go to folder with app `cd app_python`

### How to build?

docker build -t dsaee/lab2:v1.0 .

### How to pull?

docker pull dsaee/lab2:v1.0

### How to run?

docker run -d -p 8000:8000 dsaee/lab2:v1.0

## Unit Tests

1. Test for response status code, if code 200 - everything is fine
2. Test for html validity, if `<html>`, `<head>` and title "Текущее Московское время" in response html - everything is fine
3. Test for time validity, check if current time hours and minutes are in html, if so - everything is fine

## CI

1. First we run `test` job, where we check our code with tests using `pytest` lib
2. Next, we run `linter` job which checks files using `flake8` checker, this step requires `test` job to finish successfully
3. We run `snyk` job in order to identify and address vulnerabilities in my project. This job requires both `test` and `linter` jobs to finish successfully
4. Finally we run `docker` job which do login, build and push steps. It's the very last step which requires all the previous steps to be done: `test`, `linter` and `snyk` successfully

## Visits

```bash
$ curl http://localhost:8000/

  <html>
      <head>
          <title>Текущее Московское время</title>
      </head>
      <body style="display: flex; justify-content: center; background: #222">
          <div style="display: inline-flex; justify-content: center;">
            <p style="font-size: 154px; color: #fbcb40; margin: 0;">
              15:05
            </p>
            <p style="color: white; font-size: 72px; margin: 15px 0 0 0;">
              53
            </p>
          </div>
      </body>
  </html>
```

```bash
$ curl http://localhost:8000/visits
"Total Visits: 1"
```

```bash
$ curl http://localhost:8000/

  <html>
      <head>
          <title>Текущее Московское время</title>
      </head>
      <body style="display: flex; justify-content: center; background: #222">
          <div style="display: inline-flex; justify-content: center;">
            <p style="font-size: 154px; color: #fbcb40; margin: 0;">
              15:05
            </p>
            <p style="color: white; font-size: 72px; margin: 15px 0 0 0;">
              53
            </p>
          </div>
      </body>
  </html>
```

```bash
$ curl http://localhost:8000/visits
"Total Visits: 2"
```
