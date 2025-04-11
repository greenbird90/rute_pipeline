
import requests
import pandas as pd
from ors_config import API_KEY, COORDINATES

def fetch_rute_info():
    url = "https://api.openrouteservice.org/v2/directions/driving-car"
    headers = {
        "Authorization": API_KEY,
        "Content-Type": "application/json"
    }

    payload = {"coordinates": COORDINATES}
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    segment = data['features'][0]['properties']['segments'][0]
    coords = data['features'][0]['geometry']['coordinates']

    df = pd.DataFrame({
        'distance_km': [segment['distance'] / 1000],
        'duration_min': [segment['duration'] / 60]
    })
    df.to_csv("rute_pipeline/output/rute.csv", index=False)

    return coords
