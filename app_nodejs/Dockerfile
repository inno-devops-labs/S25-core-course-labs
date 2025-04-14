# app_nodejs/Dockerfile

# 1) Use pinned version of Node.js on Alpine
FROM node:14-alpine AS build

# 2) Create a non-root user
RUN addgroup -S nodejs_group && adduser -S nodejs_user -G nodejs_group

# 3) Set working directory
WORKDIR /usr/src/app

# 4) Copy only essential files
COPY package.json /usr/src/app/

# 5) Install dependencies
RUN npm install --production

# 6) Copy the rest of the source code
COPY server.js /usr/src/app/

# 7) Switch user
USER nodejs_user

# 8) Expose port 3000
EXPOSE 3000

# 9) Default command
CMD ["node", "server.js"]



