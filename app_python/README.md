# Moscow Time Display 🕰️

![CI Status](https://github.com/ArturLukianov/S25-core-course-labs/actions/workflows/app_python.yaml/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
![Flask Version](https://img.shields.io/badge/flask-3.1.0-lightgrey)

A production-ready web application displaying current Moscow time with retro pixel styling and automatic refresh.

![Moscow Time Screenshot](docs/screenshot.png)

## Features ✨

- 🌑 Dark theme with retro CRT aesthetic
- 🖥️ Pixel-styled display using VT323 font
- ⚡ Real-time updates (1-second refresh)
- 🌍 Timezone-aware calculations (pytz)
- 📈 Production-ready configuration
- 📊 Comprehensive logging
- 🛡️ Error handling with graceful degradation
- 📱 Responsive design

## Installation 💻

### Prerequisites

- Python 3.9+
- pip 23.0+

### Quick Start

```bash
# Clone repository
git clone https://github.com/ArturLukianov/S25-core-course-labs.git
cd moscow-time-app

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py
```

### Using Docker

You can build the image locally:

```bash
docker build -t moscow-time-app .
```

Or pull it from Dockerhub:

```bash
docker pull pr0ventu5/moscow-time-app
```

To run the container, use the following command (PORT environment variable can be specified, by default it is 8080):

```bash
docker run -p 8080:8080 moscow-time-app:latest
```

### Running the Tests

The tests are in the tests/ directory, you can run them using:

```bash
python -m unittest discover
```
