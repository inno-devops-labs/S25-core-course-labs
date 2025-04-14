# Web application to display current time in Moscow

## Overview

This application uses [C](https://en.wikipedia.org/wiki/C_(programming_language)) and
[Mongoose](https://github.com/cesanta/mongoose) to host a web page to shown the current
time in Moscow. The app serves a single webpage, which contains the current time and date
in Moscow, along with some minimalistic formatting. You can find the source code in
[app.c](app.c), the [HTML](resources/templates) and [CSS](resources/static) files in
[resources](resources). The framework files are in [mongoose](mongoose)
and some implementation justifications are in [C.md](C.md).

## Setup

### GCC

Download GCC compiler from any distribution suitable for your system, and make sure to add it to PATH.

I have built this application using [MinGW-W64](https://github.com/niXman/mingw-builds-binaries/releases)
on Windows 11 and default GCC installation on Ubuntu 22.04

### Compiling the application

From the command line, inside the repository directory, run

#### Windows

```batch
gcc -I./mongoose mongoose/mongoose.c app.c -o app.exe -lwsock32
```

app.exe can be replaced by any other name, just make sure to keep the exe extension.

#### Linux

```bash
gcc -I./mongoose mongoose/mongoose.c app.c -o app
```

app in output can be replaced by any other name.

### Running the web application

Run your built application from the command line by using:

#### Windows

```batch
app.exe your_ip:your_port
```

#### Linux

```bash
./app your_ip:your_port
```

your_ip and your_port have to be replaced by the ip you wish to host on
and the port number respectively, for example:

#### Windows

```batch
app.exe 127.0.0.1:8080
```

#### Linux

```bash
./app 127.0.0.1:8080
```

The app.exe/app will be the name of your built binary file, if you changed it
in building, make sure to change it here too.

After hosting, you can connect to the web app from any browser using
the provided ip and port, which will also be shown in the terminal.

### Distroless Docker

### Building the image

From the command line, inside the repository directory, run

```batch
docker build -f distroless.Dockerfile -t c_msk_time_distroless:latest .
```

Running the image is the same as with regular Docker, just replace the image name
