# Python Web Application

## Overview
This web application displays the current time in Moscow using Flask.

## Installation
1. Clone the repository.
2. Navigate to the app_python directory.
3. Install dependencies:
   
           pip install -r requirements.txt
   
4. Run the application:
   
         python app.py
   

## Requirements
- Flask
- pytz

## Best Practices Applied
- Used virtual environments to manage dependencies.
- Followed coding standards for readability and maintainability.
- Implemented testing by ensuring that the time updates upon page refresh.

   ## Docker Instructions

     ### Build the Image
     To build the Docker image, run:
           

      docker build -t yourusername/app_python:latest 
     
### Pull the Image
   To pull the image from Docker Hub, run:
     

     docker pull yourusername/app_python:latest
     
### Run the Image
To run the Docker container, execute:
     

     docker run --rm yourusername/app_python:latest
     
    ## Distroless Image Version

###   To build and run the Distroless version of the application, use:
   

      docker build -t username/app_python:distroless -f distroless.Dockerfile_extra
      docker run --rm username/app_python:distroless    

## License
This project is licensed under the MIT License.

