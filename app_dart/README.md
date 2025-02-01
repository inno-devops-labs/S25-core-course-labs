# Flutter Yekaterinburg Time Web App

[![CI (Flutter)](https://github.com/dinaraparanid/devops/actions/workflows/flutter.yml/badge.svg)](https://github.com/dinaraparanid/devops/actions/workflows/flutter.yml)

### Developer

[Arseny Savchenko](https://github.com/dinaraparanid)

### About App

Sample Flutter application that shows current time in Yekaterinburg

### Preview

![preview.png](assets/preview.gif)

### Setup

* **Manual**

Build application with Flutter CLI:

1. Install Flutter for [your platform](https://docs.flutter.dev/get-started/install).

2. Install all necessary dependencies:
   > flutter pub get

3. Run application with Chrome:
   > flutter run -d chrome

4. Launch widget tests:
   > flutter test --platform chrome

* **Docker (Base Image)**

Build application with Docker:

1. Pull image from DockerHub:
   > docker pull paranid5/app_flutter

2. Run docker container:
   > docker run --rm -it -p <YOUR_PORT>:80 paranid5/app_flutter

3. Access web page:
   > curl http://127.0.0.1:<YOUR_PORT>

4. Optional: build image with Dockerfile:
   > docker build -t app_flutter

### Stack

<ul>
   <li>Flutter 3.27.1</li>
   <li>Dart 3.6.0</li>
   <li>Timezone 0.10.0</li>
</ul>

## Unit tests

Comprehensive integration test is provided to check the correctness
of the primary web page: content and styles of each widget.
Source code can be found at `/test` folder

Execute tests:
> flutter test --platform chrome

## CI

CI via GitHub Actions is established for the project (see /.github/workflows/flutter.yml):

1. Runner is observing changes in the app_flutter folder and in its own source code.
2. Runner utilizes *Flutter 3.27.3* (env) and caches the setup process with all dependencies.
3. CI integrates *flutter analyze* to check the consistency of the code style according to dart format.
4. Finally, runner uses *DockerHub* to deploy a Docker image of a web app on each change
5. **Secrets and environment variables** for DockerHub and Flutter are managed via GitHub Actions.
   See the documentation on the setup
   [here](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions).
