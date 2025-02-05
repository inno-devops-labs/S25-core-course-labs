FROM alpine:3.19
WORKDIR /app
COPY app.cpp ./
RUN apk add --no-cache \
    g++ \
    make \
    wget \
    linux-headers
RUN mkdir /usr/local/include && wget https://raw.githubusercontent.com/yhirose/cpp-httplib/master/httplib.h -O /usr/local/include/httplib.h
RUN g++ app.cpp -o app 
EXPOSE 8080
CMD ["./app"]
