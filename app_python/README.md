# Python Web Application: Display Current Time in Moscow

![example workflow](https://github.com/Magel0n/S25-core-course-labs/actions/workflows/python-app.yml/badge.svg)

## Framework Chosen: 
- **Flask**: The web framework used to build the application.

As the title says, this application uses python, specifically ``Python 3`` and html for rendering.

**Flask** was chosen for this project 
because it is a lightweight framework that is ideal for small applications, like this one.

## Web application

For the web application I use **Flask** functionality to render .html templates with a time parameter.

To get the correct time in Moscow I use **datetime** and to get the correct timezone I use 
```timezone(timedelta(hours=3))```
since the Moscow's timezone is *UTC+3*, so we need to have a ```timedelta``` that is 3 hours more than *UTC+0*

I also use `%Y-%m-%d %H:%M:%S` to format the time using `strftime` to follow the most common time formats.

## Installation

To run the application locally:

1. **Clone the repository:**
```bash
git clone https://your-repository-url.git
cd app_python
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the app:**
```bash 
python app.py
```

4. **Follow the browser link:**
    
The link will be in the terminal, or simply go to ``http://127.0.0.1:5000/`` to view the application.
You may also go to ``http://127.0.0.1:5000/visits`` to check the number of visits (it counts the visits to the visits page, too)

# Dedicated Docker section

If you wish to simplify your downloading experience and you have `Docker`, then you may do the following:

1. **Move to the application folder (app_python)**
2. **Build the Docker container:**
```bash
docker build -t magel0n/moscowtimeimagepython:latest .
```
Feel free to change the name from my username to yours and change the name of the image.

Also, if you wish not to download this repository at all, you may pull my image using this:
```bash
docker pull magel0n/moscowtimeimagepython
```
Please note that your image will default to ```docker.io/magel0n/moscowtimeimagepython:latest```,
input that name for the next step if you chose this approach.
3. **Run the docker container:**
```bash
docker run -p 5000:5000 magel0n/moscowtimeimagepython:latest 
```
# Distroless Image Version
To run the disroless image, whilst following the same steps as the building option, use this:
```bash
docker build -t magel0n/moscowtimeimagepython:latest -f distroless.Dockerfile .
```
The ```-f distroless.Dockerfile``` will signal `Docker` to use the other image creation.
Then, proceed as with the other example.

# Unit Tests
To run the **unit tests** for this project you need to go to \app_python, install the testing libraries using this command:
```bash
pip install pytest coverage
```
and then you can use the following command to run all the tests (use -v to see more):
```bash
pytest
```
Also you can run the following command to see the coverage:
```bash
coverage run -m pytest
```
Then you can use the following command to see the result:
```bash
coverage report
```
The coverage of 90% of [app.py](app.py) is due to the ``if name == __main__: ...`` part.

# CI/CD

This project contains a **Github actions workflow** that allows for automatic testing, building and pushing to Dockerhub.
The workflow configuration file can be accessed at [.github/workflows/python-app.yml](../.github/workflows/python-app.yml).

In the workflow, all the necessary dependencies are downloaded and tests are conducted. Additionally, the code is linted
using **flake8**.

In another job there is the automatic aquizition of **DockerHub** credentials from **Github** secrets and subsequent build and push of the image.

There is also a security job using **SNYK** to test the application against vulnerabilities.

The status of the workflow can be viewed at the top of this file in a badge, 
or at [Github actions](https://github.com/Magel0n/S25-core-course-labs/actions).