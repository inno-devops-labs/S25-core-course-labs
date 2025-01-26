# Scala Web App

## Description

This is a Scala web application that shows the current time in Moscow.

![Web page](images/web_page.png)

-----

## How to install it locally?

### Requirements

The project requires:

- Scala 2.13.10
- SBT
- Java

All of it can be installed by requirements.sh bash file (included into the Installation steps). If Scala, Java and SBT are installed on your machine, skip the step of requirements installation.

### Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/BugaevGleb/S25-core-course-labs
   cd S25-core-course-labs
   git checkout lab1
   cd app_scala
   ```

2. Install the requirements:

   ```bash
   chmod +x requirements.sh
   ./requirements.sh
   ```

3. Run the application:

   ```bash
   cd time_application_project
   sbt assembly
   java -jar target/scala-2.13/MoscowTimeApp-assembly-0.1.jar
   ```

   OR (just another way):

   ```bashV
   cd time_application_project
   sbt reload
   sbt update
   sbt run
   ```

4. Go to <http://localhost:9090/> and see the current Moscow time.