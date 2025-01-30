# C++ Web Application

A simple web application built with cpp-httplib that displays random number. Probably, it will be changed. Now it is the simplest "Hello, world!" program with random number generator for testing. This simplicity is due to the lack of experience in writing such applications in languages other than python. This may be corrected in the future.


## Usage

#### Dependencies

You need to install  cpp-httplib on your system:
```
sudo wget https://raw.githubusercontent.com/yhirose/cpp-httplib/master/httplib.h -O /usr/local/include/httplib.h
```

#### Compiling

```
g++ app.cpp -o web_server
```

#### Usage

```
./web_server
```
It will be able in 0.0.0.0:8080

## Docker

There is an ability to use application in Docker. You may build it manually or use image from Docker Hub.

#### Building

To build image manually run:
```
docker build --no-cache -t <name> .
```

#### Pulling

To pull image from Docker Hub run:
```
docker pull voronm1522/devops:cpp-app
```

#### Running

To run image run:
```
docker run <name>
```