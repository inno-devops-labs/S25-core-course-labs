# Python web-application

### Run application with the command
```python
python3 app.py
```

### Install dependencies
```bash
pip install -r requirements.txt
```

This application uses `Flask` as the framework.

### Project structure
```
app_python/
│
├── app.py
├── static/
    └── index.css
├── templates/
│   └── home.html
```

Using this web-application, you can check current time in Moscow.

# Docker

### Building the Docker image
```
docker build -t python-msk-time .
```

### Run the container
```
docker run -p 5000:5000 python-msk-time
```

### Pull from Docker Hub
```
docker pull nickolaus899/python-msk-time:latest
```

#### For the distroless one:
```
docker build -t py-distroless -f distroless.Dockerfile .

docker run -p 5000:5000 py-distroless

docker pull nickolaus899/py-distroless:latest
```


#### Working directory: `/app`

### Verification and testing
Manuaaly tested the container and pulling for the DockerHub.

