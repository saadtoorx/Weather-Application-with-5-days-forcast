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