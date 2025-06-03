import requests
import json

# Yr.no API endpoint:
url = "https://api.met.no/weatherapi/locationforecast/2.0/compact"

# Tallinna kordinaatid:
params = {
    'lat': 59.4370,
    'lon': 24.7535
}

# tuvastame kasutajaid:
headers = {
    'User-Agent': 'WeatherApp/1.0 (your_email@example.com)'  # Replace with your email
}

# saadame GET taotlus API-le:
response = requests.get(url, params=params, headers=headers)

# kontrollida: kas taotlus oli õnnestus
if response.status_code == 200:
    # parsi JSON vastus:
    data = response.json()

    # kirjutab pealkirja:
    print("Weather Forecast for Tallinn")
    print("-" * 40)
    print(f"{'Time':<20}{'Temperature (°C)'}")
    print("-" * 40)

    # tsüklit läbi ajaseeria ja kuvada andmed:
    for timeseries in data['properties']['timeseries']:
        # käivita kellaaeg ja temperatuur:
        time = timeseries['time']
        temperature = timeseries['data']['instant']['details']['air_temperature']

        # kirjutab välja formateeritud aeg ja temperatuur:
        print(f"{time:<20}{temperature:>5.1f}°C")

else:
    print(f"Error: {response.status_code}")
