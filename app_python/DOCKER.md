# Best practices, employed in this docker image

1. **`.dockerignore` file**
    Helps ignore irrelevant for image files 
2. **Fixed base image version**
    Helps avoid sudden issues with compatibility and unexpected updates
3. **Slim base image**
    Helps speed up build time and decrease image size
4. **Disabling unnecessary caching**
    Since it won't survive image rebuilding, it wastes space
5. **Image layering**
    Less frequently updated parts are place at the top of the `Dockerfile` to employ layer caching
6. **Non-root image**
    Increases security of an app