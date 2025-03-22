# Why Flask Was Chosen for This Web Application

Flask is a lightweight and flexible Python web framework, and I believe it is the best choice for this web application. Below are the reasons why Flask is suitable for this project:

## Advantages of Flask

1. **Simplicity and Minimalism**  
   Flask provides a basic set of web development tools, making it ideal for beginners. In this case, the task was to deploy the web application as quickly and simply as possible.

2. **Flexibility and Extensibility**  
   Flask offers the ability to easily integrate with other libraries and services. This ensures that the application is scalable and allows for future improvements without complications.

3. **The "Microframework" Approach**  
   Flask follows a microframework philosophy, giving developers control over their project by allowing them to include only the necessary tools and libraries. This approach ensures the application remains lightweight and productive without unnecessary overhead.

4. **Large Community and Support**  
   Flask’s popularity means there is a large community of developers and abundant resources available. This makes learning, troubleshooting, and building applications with Flask much easier.

## Conclusion

Flask’s simplicity, flexibility, and extensive support make it an excellent choice for this web application.

## Best practices

1. Splitting HTML, CSS, and JS code into different files for ease of development and readability 
2. Creating the correct project structure with static and templates folders, correct naming of files
3. Variables and functions are given descriptive names for greater clarity.
4. Proper use of inputs

The Flask application was tested by running it locally (`debug=True`).

Dynamic time updates have been tested both at boot time and during continuous intervals. (using `setInterval`).

## Unit tests

I wrote unit tests for my flask application usin `unittest` framework. 

1. **setUp function**
   It creates a test client for the application and enables testing mode

2. **test_home function**
   He sent a GET request to the homepage and compared the returned status code. If the status code is `200`, it means that everything is in order and the test is passed.

I used several best practices when writing the unit tests:

1. Test are easy and readable
2. Using proper naming for tests
3. Tests are fast
4. Using a popular and reliable framework for unit tests