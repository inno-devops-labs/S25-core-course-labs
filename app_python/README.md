# Python Web Application

A simple web application built with Flask that displays the current time timezone (Moscow time by default).


## Usage

#### Installation

To prepare virtual environment run:

```
virtualenv venv
source venv/bin/activate
```
or
```
python -m venv venv
source venv/bin/activate
```
To install dependencies file `requirements.txt` file run:
```
pip install -r requirements.txt
```

#### Settings

Edit the `config.txt` file to set the time zone of interest. To do this, delete everything from it and type in your sona. To find out all possible options, perform 
```
>>> import pytz
>>> pytz.all_timezones
```
Using the python interpreter in the console.
In case of a configuration error, Moscow time is displayed.
To disable debugging mode change the last line in `app.py` use `debug=False` instead `debug=True`.

## Using
```
pip install -r requirements.txt
```

To use this application run `python app.py`.


## Docker

There is an ability to use application in Docker. You may build it manually or use image from Docker Hub.
=======
```
>>> import pytz
>>> pytz.all_timezones
```

#### Building

To build image manually run:
```
docker build --no-cache -t <name> .
```

#### Pulling

To pull image from Docker Hub run:
```
docker pull voronm1522/devops:python-app
```

#### Running

To run image run:
```
docker run <name>
```
