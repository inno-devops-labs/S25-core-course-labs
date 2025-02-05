# Use the official Node.js image from the Docker Hub
FROM node:20

# Set the working directory
WORKDIR /usr/local/app/frontend

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN yarn install

# Copy the rest of the application code
COPY . .

# Create a non-root user
RUN adduser --disabled-password --disabled-login myuser

# Change ownership of the application files
RUN chown -R myuser:myuser /usr/local/app/frontend

# Switch to the non-root user
USER myuser

# Expose the application port
EXPOSE 3000

# Command to run the application
CMD ["yarn", "start"]
