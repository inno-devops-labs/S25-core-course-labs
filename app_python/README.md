# Python Web Application

## Overview
This web application displays the current time in Moscow using Flask.

## Installation
1. Clone the repository.
2. Navigate to the app_python directory.
3. Install dependencies:
   
bash
   ```pip install -r requirements.txt```
   
4. Run the application:
   
bash
   ```python app.py```
   

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
           
      ### bash
      docker build -t yourusername/app_python:latest .
     
### Pull the Image
   To pull the image from Docker Hub, run:
     
      bash
     docker pull yourusername/app_python:latest
     
### Run the Image
To run the Docker container, execute:
     
      bash
     docker run --rm yourusername/app_python:latest
     
     

## License
This project is licensed under the MIT License.

