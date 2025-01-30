# App Title
**Moscow Time Web Application**

# Description
This is a simple Go web application that fetches the current time in Moscow using TimeAPI and displays it in a visually appealing HTML interface.

# Features
- Fetches the current time in Moscow via an external API.
- Displays the time in a clean and responsive web interface.
- Handles errors gracefully and provides fallback behavior in case of issues.

# Installation:

## 1. Normal Installation:

### Requirements
- Linux OS
- Go >= 1.23
- Web browser

1. Clone the repository

2. Run the application:
   ```bash
   go run app.go
   ```

3. Open your browser and navigate to:
   ```
   http://127.0.0.1:8000
   ```

4. To exit the app, press ```(Ctrl + C)```

## Installation Using a Docker Image

### Requirements
- Docker
- Web browser

1. Pull the dockerized image from docker hub
   ```bash
   docker pull spaghettic0der/moscow-time:v2.0.0
   ```

2. Run the image on any free port (e.g. 8000)
   ```bash
   docker run -p<Your-Selected-Port>:8000 spaghettic0der/moscow-time:v2.0.0
   ```

3. Open your browser and navigate to:
   ```bash
   http://127.0.0.1:<Your-Selected-Port>
   ```

4. To stop the app, press ```Ctrl + C```

## Installation Using a Distroless Docker Image

### Requirements
- Docker
- Web browser

1. Pull the dockerized image from docker hub
   ```bash
   docker pull spaghettic0der/distro-moscow-time:v2.0.0
   ```

2. Run the image on any free port (e.g. 8000)
   ```bash
   docker run -p<Your-Selected-Port>:8000 spaghettic0der/distro-moscow-time:v2.0.0
   ```

3. Open your browser and navigate to:
   ```bash
   http://127.0.0.1:<Your-Selected-Port>
   ```

4. To stop the app, press ```Ctrl + C```