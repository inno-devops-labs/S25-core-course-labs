# XKCD Comic Fetcher

## Overview

This web application fetches the latest comic from **XKCD** and displays it on the page. Upon clicking the "Do you wanna see a comic?" button, the app fetches the latest comic's details (title, image, date, and description) and shows them in the HTML.

## Setup and Installation

### Prerequisites

- Web browser (Google Chrome, Firefox, etc.)

### Steps to Run the App

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Kazan-Strelnikova/S25-core-course-labs.git
   cd S25-core-course-labs/app_javascript
   ```

2. **Ensure that the required files are present**:
   - `index.html` - The main HTML page.
   - `style_comic.css` - The styling for the comic container.
   - `myapp.js` - JavaScript file to fetch and display the comic.

3. **Open `index.html` in your web browser**:
   Simply open the `index.html` file in a browser to interact with the app.

4. **Click the button**:
   The button will fetch the latest comic and display it below.

# Docker Usage

### How to Build
To build the Docker image for this application, run:
```bash
docker build -t js-app .
```

### How to Pull
To pull the pre-built image from Docker Hub, run:
```bash
docker pull kira354/js-app:latest
```

### How to Run
To run the Docker container and serve the application, use the following command:
```bash
docker run -p 80:80 js-app
```

Visit `http://localhost` in your browser to access the application.