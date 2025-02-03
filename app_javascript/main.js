function main(latitude, longitude) {
    // Accessing the header, where the sunrise time will be located
    const timeText = document.getElementById('time');

    // Fetching sunrise time
    fetch(`https://api.sunrisesunset.io/json?lat=${latitude}&lng=${longitude}`).then(r => {
        return r.json();
    }).then(data => {
        let sunriseTime = data.results.sunrise;
        timeText.innerText = `Sunrise time for ${data.results.date} in Naberezhnye Chelny is ${sunriseTime}`;
    }).catch(err => {
        timeText.innerText = err.message;
    });
}

// The basic case: city is Naberezhnye Chelny
main('55.740280', '52.398109')