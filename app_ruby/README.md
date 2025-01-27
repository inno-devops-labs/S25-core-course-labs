# Ruby Web Application

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
