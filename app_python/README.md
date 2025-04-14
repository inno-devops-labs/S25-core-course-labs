## How to Use

1. Install the required dependencies using the following command:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application using the following command:
   ```bash
   python app.py
   ```
3. Open your web browser and navigate to: `http://127.0.0.1:5000/`


# Docker Usage
The application can also be run inside a Docker container.

### 1. Building the Docker Image
To build the Docker image, run:

``docker build -t moscow-time-app .``

### 2. Running the Container
Run the application using Docker:

``docker run -d -p 5000:5000 moscow-time-app``

Now, open your web browser and go to:

``http://localhost:5000``

### 3. Pushing the Image to Docker Hub

1. Log in to Docker Hub: 
   ``docker login``
2. Tag the image: 
   ``docker tag moscow-time-app your-dockerhub-username/moscow-time-app``
3. Push the image: 
   ``docker push your-dockerhub-username/moscow-time-app``


### 4. Pulling and Running the Image from Docker Hub

To pull and run the image from Docker Hub, execute:

``
docker pull your-dockerhub-username/moscow-time-app
``

``
docker run -d -p 5000:5000 your-dockerhub-username/moscow-time-app
``