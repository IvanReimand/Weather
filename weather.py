import requests
import json

# Yr.no API endpoint
url = "https://api.met.no/weatherapi/locationforecast/2.0/compact"

# Coordinates for Tallinn (Latitude, Longitude)
params = {
    'lat': 59.4370,
    'lon': 24.7535
}

# Headers to identify the user
headers = {
    'User-Agent': 'WeatherApp/1.0 (your_email@example.com)'  # Replace with your email
}

# Send GET request to the API
response = requests.get(url, params=params, headers=headers)

# kontrollida: kas taotlus oli õnnestus
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Print the header for clarity
    print("Weather Forecast for Tallinn")
    print("-" * 40)
    print(f"{'Time':<20}{'Temperature (°C)'}")
    print("-" * 40)

    # Loop through the timeseries and display the data
    for timeseries in data['properties']['timeseries']:
        # Extract the time and temperature
        time = timeseries['time']
        temperature = timeseries['data']['instant']['details']['air_temperature']

        # Print the time and temperature with formatting
        print(f"{time:<20}{temperature:>5.1f}°C")

else:
    print(f"Error: {response.status_code}")
