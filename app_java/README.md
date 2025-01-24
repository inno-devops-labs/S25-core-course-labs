# Vacation Payment Calculator

## Overview

Vacation... What can actually be better than this? However, alongside with the "chill" time, there is another
thing: vacation payments. And it is kinda hard to properly obtain the final payment during your vacation.
To get rid of such problems, this application gave you the opportunity to calculate the amount of money
you receive during the best time of a year!

## Application

To briefly explain about the application, I can say next:

* This is API that return you the amount of money you receive after the vacations. For now,
  there is a single handler for the GET request, and you can use it by opening
  the Swagger of the application (available upon the application start)

## Usage

To start your application, you need firstly to package your application into single executable `.jar` by the command:

```bash
mvn clean package
```

But to make your life even easier, I keep the `app_java-0.1.jar` in the root of the project. So, you need just to
type in the bash:

```bash
java -jar app_java-0.1.jar
```

### _Reminder: take in mind that you need installed JDK (ver. >= 21) on your PC_

Then, start the browser and type `localhost:8080`, and...
That's all! You are great, prepare for the weekends and calculate the width of your wallet

## Example

![img.png](res/swagger.png)

![swagger_step_1.png](res/swagger_step_1.png)

![swagger_result.png](res/swagger_result.png)
