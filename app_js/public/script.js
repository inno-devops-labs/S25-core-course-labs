const DIST_URL = (city) => `/get-coordinates?city=${encodeURIComponent(city)}`

// function to get coordinates of a city using Yandex Geocoder API
// returns { longitude latitude } of the given city or an error
async function getCoordinates (city) {
  const response = await fetch(DIST_URL(city))
  if (!response.ok) {
    return null
  }

  const data = await response.json()

  return data
}

// function to calculate distance between two coordinates using the Haversine formula
// (https://en.wikipedia.org/wiki/Haversine_formula)
function haversineDistance (coords1, coords2) {
  const toRad = (value) => (value * Math.PI) / 180
  const R = 6371 // radius of the Earth in kilometers

  const latDiff = toRad(coords2.lat - coords1.lat)
  const lonDiff = toRad(coords2.lng - coords1.lng)

  // math formula
  const a =
        Math.sin(latDiff / 2) ** 2 +
        Math.cos(toRad(coords1.lat)) *
            Math.cos(toRad(coords2.lat)) *
            Math.sin(lonDiff / 2) ** 2

  const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a))
  return R * c // distance in kilometers
}

// main function to calculate distance
async function calculateDistance () {
  console.log('Button was clicked')

  const city1 = document.getElementById('city1').value.trim()
  const city2 = document.getElementById('city2').value.trim()
  const resultField = document.getElementById('result')

  resultField.textContent = 'Waiting...'

  if (!city1 || !city2) {
    resultField.textContent = 'Please enter both city names.'
    return
  }

  try {
    const coords1 = await getCoordinates(city1)
    const coords2 = await getCoordinates(city2)

    if (!coords1) {
      resultField.textContent = 'Invalid name of the first city'
      return
    }
    if (!coords2) {
      resultField.textContent = 'Invalid name of the second city'
      return
    }

    const distance = haversineDistance(coords1, coords2)
    resultField.textContent = `The distance between ${city1} and ${city2} is ${distance.toFixed(2)} km.`
  } catch (error) {
    resultField.textContent = error.message
  }
}

document.getElementById('calculate_button').addEventListener('click', calculateDistance)
module.exports = { getCoordinates, haversineDistance }
