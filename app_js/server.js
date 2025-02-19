const express = require('express')
const dotenv = require('dotenv')
const fetch = require('node-fetch')
const path = require('path')
const client = require('prom-client')

dotenv.config()

const app = express()
const PORT = 3000

const register = new client.Registry()
client.collectDefaultMetrics({ register })

const httpRequestCounter = new client.Counter({
  name: 'http_requests_total',
  help: 'Total number of HTTP requests',
  labelNames: ['method', 'route', 'status_code']
})
register.registerMetric(httpRequestCounter)

// creating middleware
app.use((req, res, next) => {
  res.on('finish', () => {
    httpRequestCounter.inc({ method: req.method, route: req.path, status_code: res.statusCode })
  })
  next()
})

// load API info from .env
const API_KEY = process.env.YANDEX_API_KEY
const API_URL = (city) => `https://geocode-maps.yandex.ru/1.x/?apikey=${API_KEY}&geocode=${encodeURIComponent(city)}&format=json`

app.use(express.static(path.join(__dirname, 'public')))

// route to get coordinates for a city
app.get('/get-coordinates', async (req, res) => {
  const city = req.query.city
  if (!city) {
    return res.status(400).send({ error: 'City name is required' })
  }

  console.log(`Trying to get coordinates of a city ${city}`)

  try {
    const response = await fetch(API_URL(city))
    const data = await response.json()

    console.log(`Data from the API: ${data}`)

    if (data.response.GeoObjectCollection.featureMember.length > 0) {
      const coordinates = data.response.GeoObjectCollection.featureMember[0].GeoObject.Point.pos.split(' ')
      console.log(`Coordinates: ${coordinates}`)
      return res.send({ lat: parseFloat(coordinates[1]), lng: parseFloat(coordinates[0]) })
    } else {
      return res.status(404).send({ error: `City "${city}" not found` })
    }
  } catch (err) {
    console.error(err)
    res.status(500).send({ error: 'Internal server error' })
  }
})

app.get('/metrics', async (req, res) => {
  res.set('Content-Type', register.contentType)
  res.end(await register.metrics())
})

app.get('/health', (req, res) => {
  res.status(200).send('OK')
})

// route to get home page
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'))
})

// start the server
if (require.main === module) {
  app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`)
  })
}

module.exports = app
