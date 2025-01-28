# Use an official Nginx image for the base
FROM nginx:alpine

# Set the working directory
WORKDIR /app

# Copy only the necessary files (index.html, JavaScript, CSS)
COPY index.html myapp.js style_comic.css /usr/share/nginx/html/

# Expose port 80 (default for Nginx)
EXPOSE 80

# Command to run the Nginx server
CMD ["nginx", "-g", "daemon off;"]
