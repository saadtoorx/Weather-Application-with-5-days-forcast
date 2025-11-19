function getWeather() {
    const location = document.getElementById("locationInput").value;
    if (!location) return alert("Enter a location");

    fetch("/weather", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ location })
    })
    .then(res => res.json())
    .then(showWeatherData);
}


function getCurrentLocationWeather() {
    navigator.geolocation.getCurrentPosition(position => {
        fetch("/weather", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({
                lat: position.coords.latitude,
                lon: position.coords.longitude
            })
        })
        .then(res => res.json())
        .then(showWeatherData);
    });
}


function showWeatherData(data) {
    const weather = data.weather;
    if (!weather || weather.cod !== 200) {
        document.getElementById("weatherResult").innerHTML = "<p>Location not found.</p>";
        document.getElementById("weatherResult").classList.add("show")
        return;
    }

    document.getElementById("weatherResult").innerHTML = `
        <h2>${weather.name}</h2>
        <img src="https://openweathermap.org/img/wn/${weather.weather[0].icon}@2x.png" />
        <p>${weather.weather[0].description}</p>
        <p>Temperature: ${weather.main.temp}°C</p>
        <p>Humidity: ${weather.main.humidity}%</p>
        <p>Wind: ${weather.wind.speed} m/s</p>
    `;

    if (data.forecast) showForecast(data.forecast);
}

function showForecast(forecastData) {
    let html = "<h3>5-Day Forecast</h3><div class='forecast-grid'>";

    forecastData.list.forEach(item => {
        html += `
            <div class="forecast-card">
                <p>${item.dt_txt}</p>
                <img src="https://openweathermap.org/img/wn/${item.weather[0].icon}.png" />
                <p>${item.main.temp}°C</p>
            </div>
        `;
    });

    html += "</div>";

    document.getElementById("forecastResult").innerHTML = html;
}
