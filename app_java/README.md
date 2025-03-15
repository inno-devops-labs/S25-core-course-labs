# Java Password Generator Application

This application generates new password and shows total number of visits of the website.

Host and port are `0.0.0.0` and `8080` respectively, but they can be changed with Spring configuration files or CLI
arguments *(choose whatever you want)*. Also, there is property `webapp.generated.chars` that contains all allowed
characters in password generator, with default configuration it also supports ranges such as `a-z` and `0-9`.

## Usage

```shell
git clone https://github.com/UniLeonid/S25-core-course-labs
cd S25-core-course-labs
git checkout origin/lab1
cd app_java
```

Make sure that you have installed `Java 17` and `Gradle` using it.

```shell
./gradlew bootRun
```
