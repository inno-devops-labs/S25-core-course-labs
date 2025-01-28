# Distroless Stage (Use Nginx-based image to serve static files)
FROM nginx:alpine AS distroless-stage

WORKDIR /app

# Copy the package files if you have any dependencies to install
COPY package*.json ./

# Install any dependencies (if you have any, like for minification or transpiling)
RUN npm install

# Copy the app files (myapp.js, index.html, comic_style.css, etc.)
COPY index.html myapp.js style_comic.css /app/


# Copy the app files from the build stage to Nginx's default directory for serving static files
COPY --from=build-stage /app /usr/share/nginx/html

# Expose the port Nginx will use to serve the app
EXPOSE 80

# Nginx is already set up to run by default, so no need to specify CMD
