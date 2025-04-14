# Comic Fetcher

## Overview

This web application fetches the latest comic from **XKCD** and displays it on the page. Upon clicking the "Do you wanna see a comic?" button, the app fetches the latest comic's details (title, image, date, and description) and shows them in the HTML.

The app is powered by a **Node.js** backend using **Express** to serve static files, including the HTML, CSS, and JavaScript for the frontend.

## Setup and Installation

### Prerequisites

- **Node.js** installed on your machine.
- **Web browser** (Google Chrome, Firefox, etc.)

### Steps to Run the App

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Kazan-Strelnikova/S25-core-course-labs.git
   cd S25-core-course-labs/app_javascript
   ```

2. **Install Node.js dependencies**:

   Navigate to the project folder and install the required dependencies:

   ```bash
   npm install
   ```

3. **Ensure that the required files are present**:
   - `server.js` - The Express server that serves the app.
   - `public/index.html` - The main HTML page.
   - `public/style_comic.css` - The styling for the comic container.
   - `public/myapp.js` - JavaScript file to fetch and display the comic.

4. **Run the server**:

   Start the server by running:

   ```bash
   node server.js
   ```

   The server will start running at `http://localhost:3000`.

5. **Open the app in your browser**:

   Go to `http://localhost:3000` in your web browser to view the application.

6. **Click the button**:
   - When you click the "Do you wanna see a comic?" button, the app will fetch the latest comic and display its title, image, release date, and description below the button.

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
docker run -p 3000:3000 js-app
```

Visit `http://localhost:3000` in your browser to access the application.

## **Distroless Image Version**

### **How to Build the Distroless Image**

```bash
docker build -f distroless.Dockerfile -t kira354/app-javascript-distroless .
```

### **How to Pull the Distroless Image**

```bash
docker pull kira354/app-javascript-distroless
```

### **How to Run the Distroless Image**

```bash
docker run -p 3000:3000 kira354/app-javascript-distroless
```