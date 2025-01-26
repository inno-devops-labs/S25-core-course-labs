# Scala Web App

-----

## Language and technologies
I chose **Scala** programming language to implement web application because I have a little experience in such projects on Scala. I used Akka - a toolkit and runtime for building concurrent, distributed, and resilient message-driven applications on the JVM. This is fully enough for this application, and it is relatively easy to write and build such small application using Akka and standard Scala libraries.

-----

## Best Practices
- **Build Automation**: The project uses SBT (Scala Build Tool) to automate building, dependency management, compilation, and packaging;
- **Graceful Shutdown**: The application includes a shutdown hook (sys.addShutdownHook) to gracefully stop the server when it is terminated;
- **Time Zone Awareness**: The use of the java.time.ZonedDateTime to handle time zones avoids issues with local system time (actually, it is incorporated to the task condition);
- **Testing**: All application features (time showing, updating the time while web page refreshing) were tested locally.

-----

## Coding Standards
- Meaningful names for variables;
- Comments where needed.