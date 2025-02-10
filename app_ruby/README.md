# Ruby Web Application

[![CI for app_ruby](https://github.com/cuprum-acid/devops-labs/actions/workflows/app_ruby.yml/badge.svg)](https://github.com/cuprum-acid/devops-labs/actions/workflows/app_ruby.yml)

## Overview

This application shows current time in **Omsk**

## Requirements

* Ruby 3.4

## Installation

Clone this repository:

```bash
git clone https://github.com/cuprum-acid/devops-labs.git -b lab1
```

Open directory:

```bash
cd devops-labs/app_ruby
```

Install bundler:

```bash
gem install bundler
```

Install dependencies from `Gemfile`:

```bash
bundle install
```

Run the app:

```bash
ruby app.rb
```

Open `localhost:4567` in browser or run:

```bash
curl localhost:4567
```

## Test

To run auto-tests:

```bash
rspec spec/app_spec.rb
```

## Docker

### Build

```bash
cd devops-labs/app_ruby
```

```bash
docker build -t ebob/omsk-time:v1.0 .
```

### Pull and Run

```bash
docker pull ebob/omsk-time:v1.0
```

```bash
docker run -d --name omsk -p 4567:4567 ebob/omsk-time:v1.0
```

Now it is available on `localhost:4567`

## Distroless Docker Image

### Build

```bash
docker build -t ebob/omsk-time:v1.0-distroless -f distroless.Dockerfile .
```

### Pull and Run

```bash
docker pull ebob/omsk-time:v1.0-distroless
```

```bash
docker run -d --name omsk-distroless -p 4568:4567 ebob/omsk-time:v1.0-distroless
```

Now it is available on `localhost:4568`

## Continuous Integration

This repository contains a CI pipeline configuration for the python application. The CI pipeline is managed with `GitHub Actions` and includes multiple jobs to ensure the code quality, functionality, security, and successful deployment of the application.

The pipeline consists of these main jobs:

1. Lint and Format: Ensures the code follows linting and formatting standards.
2. Test: Runs tests to verify the correctness of the application.
3. Security Scan: Checks for security vulnerabilities in the codebase using `Snyk` tool.
4. Docker Build and Push: Builds and pushes a Docker image to the DockerHub and ghcr.
