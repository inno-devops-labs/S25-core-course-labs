# App Title
**Moscow Time Web Application**

# Description
This is a simple Python Flask web application that fetches the current time in Moscow using TimeAPI and displays it in a visually appealing HTML interface.

# Features
- Fetches the current time in Moscow via an external API.
- Displays the time in a clean and responsive web interface.
- Handles errors gracefully and provides fallback behavior in case of issues.

# Installation

## 1. On Linux Environment

### Requirements
- Linux OS
- Python 3.x
- Web browser

1. Clone the repository

2. Create a virtual environment (Recommended)
   ```bash
   python3 -m venv venv
   ```

3. Activate the created virtual environment
   ```bash
   source venv/bin/activate
   ```

4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the application:
   ```bash
   python app.py
   ```

6. Open your browser and navigate to:
   ```
   http://127.0.0.1:8000
   ```

7. To exit the app, press ```Ctrl + C```

## 2. Using Docker

### Requirements
- Docker
- Web browser

1. Pull the dockerized image from docker hub
   ```bash
   docker pull spaghettic0der/moscow-time:v1.0.0
   ```

2. Run the image on any free port (e.g. 8000)
   ```bash
   docker run -p<Your-Selected-Port>:8000 spaghettic0der/moscow-time:v1.0.0
   ```

3. Open your browser and navigate to:
   ```bash
   http://127.0.0.1:<Your-Selected-Port>
   ```

3. To stop the app, press ```Ctrl + C```

## 3. Using Docker (Distroless Image)

### Requirements
- Docker
- Web browser

1. Pull the dockerized image from docker hub
   ```bash
   docker pull spaghettic0der/distro-moscow-time:v1.0.1
   ```

2. Run the image on any free port (e.g. 8000)
   ```bash
   docker run -p<Your-Selected-Port>:8000 spaghettic0der/distro-moscow-time:v1.0.1
   ```

3. Open your browser and navigate to:
   ```bash
   http://127.0.0.1:<Your-Selected-Port>
   ```

3. To stop the app, press ```Ctrl + C```