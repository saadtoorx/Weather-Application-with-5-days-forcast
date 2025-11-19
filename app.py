from flask import Flask, render_template, request, jsonify
import requests
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("OPEN_WEATHER_API_KEY")  # put your key here
BASE_URL = "https://api.openweathermap.org/data/2.5"


def get_weather_by_query(query):
    """Fetch weather using any location text (city, zipcode, landmark)."""
    url = f"{BASE_URL}/weather?q={query}&appid={API_KEY}&units=metric"
    return requests.get(url).json()


def get_weather_by_coordinates(lat, lon):
    """Fetch weather when user gives GPS coordinates."""
    url = f"{BASE_URL}/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    return requests.get(url).json()


def get_forecast_by_query(query):
    """Fetch 5-day forecast."""
    url = f"{BASE_URL}/forecast?q={query}&appid={API_KEY}&units=metric"
    return requests.get(url).json()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/weather", methods=["POST"])
def weather():
    data = request.json

    location = data.get("location")
    lat = data.get("lat")
    lon = data.get("lon")

    if lat and lon:
        # GPS mode
        weather = get_weather_by_coordinates(lat, lon)
        return jsonify({"weather": weather})

    # Text search mode
    weather = get_weather_by_query(location)
    forecast = get_forecast_by_query(location)

    return jsonify({
        "weather": weather,
        "forecast": forecast
    })


if __name__ == "__main__":
    app.run(debug=True)
