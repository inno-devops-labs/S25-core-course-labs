
# Service deployment

## Local installation and testing

Optional: you may wanna set up venv

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Beforehand, install the dependencies:

```bash
pip install -r reqiurements.txt
```

And starting the service is as easy as running one command (make sure project root is `service` folder)!

```bash
cd service
python3 -m uvicorn main:app
```

### Docker

To build the image:

```bash
docker build -t time_service .
```

To pull the image:

```bash
docker pull elonmaxx/time_service
```

To run image:

```bash
docker run time_service
```

To run distroless:

```bash
docker build -f distroless.dockerfile -t dless .
docker run dless
```
