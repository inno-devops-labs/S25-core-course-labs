# The JS application to calculate distance between two cities

*Enter names of any two cities and get know the distance between them*

### Run server
```
node server.js
```

### Installing dependencies
You can install it using

```
npm install
```

or with a command:
```
cat requirements.txt | xargs npm install
```

### Project structure
```
app_js/
│
├── server.js
├── public/
│   └── index.html
|   └── script.js
|   └── styles.js
├── package.json
├── package-lock.json
├── .env
... other files
```

# Docker

### Building
```
docker build -t js-cities-dist .

```

### Run
```
docker run -p 3000:3000 js-cities-dist

```
