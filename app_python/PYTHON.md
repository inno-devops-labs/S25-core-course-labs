# Report

## Framework

I chose Flask web framework because it is a widely used minimalistic framework (microframework) with open source, quality support, detailed documentation. An important factor in choosing it is the fact that I have minimal experience with this framework, which will allow me to complete tasks on time, quickly make changes to the code if necessary, due to a better understanding of it.


## Best practices

The small size of the application does not allow for many practices. I have endeavored to keep the code readable and the comments comprehensive. This was accomplished by splitting the code into functions, adding comments, and checking for standards compliance. I also tried to keep it minimalistic. I also use `requirements.txt` with specified versions of packages. Finally, I use configuration file for more flexibility and better maintaining.


## Coding standards, testing, code quality

To check compliance with code writing standards and evaluate its quality, pep8 (and pycodestyle) was used. At this stage, no automation of thesiting was performed. Everything is checked manually by sending additional requests (page refresh) and comparing the results. There were also tests with editing configuration file to ensure in correct configuration work.


## Unit Tests

There are 7 unit tests for application:
    - Response code and template test;
    - Test reading config file with:
        - Valid time zone;
        - Invalis timezone;
        - Empty timezone;
    - No configuration file test;
    - Test time format in response;
    - Test full response

I used next best practices:
    - Naming:
        - Each unit test (function) has comprehensive name, which allows to understand test's goal without description
    - AAA pattern (Arrange, Act and Assert)
    - Single component testing
    - One move
    - Fast tests
    - No "magic strings"