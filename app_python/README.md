# Python web application - the current time in Moscow
## Overview
This is a simple web application built on python with best practices.
The main purpose - to display the current time in Moscow
---
- Technologies: python + flask (backend), html + css (pages design and styles)
- How to get started:
    - Clone the repository
    - Navigate to the `app_python` folder
    - Install requirements: ```pip install -r requirements.txt```
    - Run the application: ```python -m flask --app main run``` from app_python directory
    - Finally, open the application by following the link: `http://127.0.0.1:5000`
---
## Docker
There is possibility to run the project using Docker.
Of course, Docker need to be installed on your machine. Here is step-by-step guide:
1. **Build** the image:
   ```docker build -t python-msk .``` <br> Or **pull** it from DockerHub: ```docker pull mirgasimovk/python-msk:latest``` 
3. Finally, run the application:
   - Locally ```docker run -p 5000:5000 python-msk```
   - Using pulled image ```docker run -p 5000:5000 mirgasimovk/python-msk``` <br> and follow to the http://localhost:5000/.
