# Moscow time
simple web application shows current moscow time

## How to run

1. install python3 
2. clone this repo and
3. install all dependencies
4. run the app 
5. you can check and see that it is now running on localhost:5000

```
git clone https://github.com/dpttk/S25-core-course-labs.git
cd lab1/app_python
pip install -r requirements.txt
python main.py
```

## docker 
This application is containerized using Docker. Below are instructions for building, pulling, and running the Docker image.

### How to Build
`docker build -t iu-devops-lab2 .`
### How to Pull
`docker pull dpttk/iu-devops-lab2:latest`
### How to Run 
`docker run -p 5000:5000 dpttk/iu-devops-lab2:latest`
or if builded localy
`docker run -p 5000:5000 iu-devops-lab2`
