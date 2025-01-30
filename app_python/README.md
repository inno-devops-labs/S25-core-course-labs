# How to run

## Please follow this steps to run this application

1. run command **pip install -r requirements.txt**
2. run command **python app.py**
3. follow **<http://127.0.0.1:5000>** on your web browser

# Docker Section

## Steps for running app using docker

1. run next command in application folder:  **docker build -t docker-app .** (use **sudo** for this and next commands if it necessary)

2. run command **docker run --rm --network="host" -p 5000:5000 --name docker-app docker-app**

3. or you can skip above steps andjust type **sudo docker run --rm --network="host" -p 5000:5000 matveyplat/docker-app\:latest** to retrieve and run image from DockerHub.

## Report part

- **Linting** Dockerfile:

![Alt text](images/lint.png)

- **Testing**:

![Alt text](images/testing.png)

- **Pushing** and **Pulling** from DockerHub:

![Alt text](images/pushingAndPulling.png)
