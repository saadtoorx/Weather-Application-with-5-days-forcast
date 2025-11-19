# Weather App

### Tech Stack
- Python (Flask)
- HTML + CSS + JavaScript
- OpenWeatherMap API
 - python-dotenv (to load `.env` values)

### Features
- Search weather using any location text (city, zipcode, landmark)
- Get current weather with icons, temperature, humidity, and wind info
- **5-day forecast**
- **Get weather using current GPS location**
- Very simple, clean, beginner-friendly code structure

### How to Run
1. Install dependencies:
Create and activate a virtual environment (recommended), then install dependencies:

Windows PowerShell:
```
python -m venv venv
; .\venv\Scripts\Activate.ps1
; pip install -r requirements.txt
```

Or install packages directly:
```
pip install flask requests python-dotenv
```

2. Add your OpenWeatherMap API key inside `.env`:
Create a `.env` file in the project root containing:

```
OPEN_WEATHER_API_KEY=YOUR_KEY
```

Do NOT commit your actual API key to the repository. Add `.env` to `.gitignore`.

3. Run server:
Run the server (development mode):

```
python app.py
```

4. Open browser:  
http://127.0.0.1:5000

### Notes
- The UI is intentionally simple.
- All weather data is fetched live from OpenWeatherMap API.
Notes & small changes
- This project requires an OpenWeatherMap API key. Free tier works for basic use.
- Geolocation ("Use Current Location") works on `localhost` or HTTPS contexts in browsers.
- I fixed a small front-end issue so the weather card becomes visible after a successful lookup (file: `static/script.js`).
- Recommended extras: add `requirements.txt` and `.gitignore` (see repo files).