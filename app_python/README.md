# Python Web Application

A simple web application built with Flask that displays the current time timezone (Moscow time by default).


## Usage

#### Installation

To prepare virtual environment run:
 
`virtualenv venv` or `python3 -m venv venv`

`source venv/bin/activate`

To install dependencies file `requirements.txt` file run:

`pip install -r requirements.txt`


#### Settings

Edit the `config.txt` file to set the time zone of interest. To do this, delete everything from it and type in your sona. To find out all possible options, perform 

`>>> import pytz`  
`>>> pytz.all_timezones`

Using the python interpreter in the console.
In case of a configuration error, Moscow time is displayed.

To enable debugging mode change the last line in `app.py`:

use `debug=True` instead `debug=False`.

## Using

To use this application run `python app.py`.
