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
docker pull .../python-msk-time:latest
```


#### Working directory: `/app`

