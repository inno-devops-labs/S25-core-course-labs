# Best practices used

- **Use a minimal base image:** A lightweight and minimal base image was used to reduce the image size and the attack surface

- **Create and use a non-root user:** A non-root user was created to avoid running the container as root increasing the security

- **Switch to the non-root user:** Switching to the non-root user created to ensure all commands are executed through that user

- **Set a dedicated working directory:** Setting a work directory to organize the files within the container

- **Copy files with the correct ownership:** Giving permissions to the right user, ensuring that the user can access and modify certain files

- **Copy necessary files only:** Imporves layers sanity

- **Install dependencies efficiently:** Installing dependencies while ensuring that no caching is being done to reduce the size of the final image

- **Set environment variables:** Setting enviroment variables to ensure that the flask app runs correctly

- **Expose only the necessary ports**
