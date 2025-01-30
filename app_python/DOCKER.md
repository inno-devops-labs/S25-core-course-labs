# Best Docker practices description

* A slim version of python image is used to ensure minimum size without any redundant functionality.
* Copying only the specific files needed to run the application.
* `.dockerignore` file is used to prevent sensitive or redundant information from getting into the container.
* Rootless container is used to ensure better security.
* Exact version of the image used instead of latest.
