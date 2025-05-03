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
