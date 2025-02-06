/* eslint-env jest */

const request = require('supertest')
const dotenv = require('dotenv')
const fetch = require('node-fetch')

// load API info from .env
dotenv.config()

const INVALID_CITY = 'InvalidCity'
const VALID_CITY = 'Moscow'

const LAT = 55.7558
const LNG = 37.6173
const CITY_COORDINATES = `${LNG} ${LAT}`

const app = require('../server') // get server.js

jest.mock('node-fetch', () => jest.fn())
const { Response } = jest.requireActual('node-fetch')

describe('GET /get-coordinates', () => {
  it('should return 400 if city is not provided', async () => {
    const res = await request(app).get('/get-coordinates')
    expect(res.status).toBe(400)
  })

  it('should return 404 if city is not found', async () => {
    fetch.mockResolvedValueOnce(new Response(JSON.stringify({
      response: {
        GeoObjectCollection: {
          featureMember: []
        }
      }
    })))

    const res = await request(app).get(`/get-coordinates?city=${INVALID_CITY}`)
    expect(res.status).toBe(404)
    expect(res.body.error).toContain(`"${INVALID_CITY}" not found`)
  })

  it(`should return coordinates if city ${VALID_CITY} was found`, async () => {
    fetch.mockResolvedValueOnce(new Response(JSON.stringify({
      response: {
        GeoObjectCollection: {
          featureMember: [{
            GeoObject: {
              Point: {
                pos: CITY_COORDINATES
              }
            }
          }]
        }
      }
    })))

    const res = await request(app).get(`/get-coordinates?city=${VALID_CITY}`)
    expect(res.status).toBe(200)
    expect(res.body.lat).toBe(LAT)
    expect(res.body.lng).toBe(LNG)
  })
})
