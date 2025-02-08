# Moscow Time Web Application

## About

This is simple application with small API,
that returns current time in Moscow and simple web page,
which interacts with this API and display current time in Moscow.

## Run the Application

### Manual

1. Enter the application directory `app_python`
2. Install virtual environment
3. Install dependencies using `requirements.txt`
4. Run application
5. Go to the browser and check address `http://0.0.0.0:5000/`

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

### Docker

#### How to build?

```bash
docker build -t darrpyy/devops .
```

#### How to pull?

```bash
docker pull darrpyy/devops
```

#### How to run?

```bash
docker run -p 5000:5000 darrpyy/devops
```
