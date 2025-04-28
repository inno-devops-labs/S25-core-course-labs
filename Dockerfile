FROM nginx

COPY ./app_python /usr/share/nginx/html

EXPOSE 80
