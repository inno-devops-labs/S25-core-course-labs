FROM cirrusci/flutter:3.10 AS build

WORKDIR /app_dart/nothern_lights_app

COPY pubspec.yaml pubspec.lock /app_dart/nothern_lights_app/
RUN flutter pub get

COPY . /app_dart/nothern_lights_app

RUN flutter build web

FROM nginx:alpine

RUN adduser -D -g 'flutter' flutter

WORKDIR /usr/share/nginx/html

COPY --from=build /app/build/web /usr/share/nginx/html

USER flutter

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
