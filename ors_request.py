import requests
import pandas as pd
import os
from ors_config import API_KEY, COORDINATES

def fetch_rute_info():
    url = "https://api.openrouteservice.org/v2/directions/driving-car/geojson"
    headers = {
        "Authorization": API_KEY,
        "Content-Type": "application/json"
    }

    payload = {"coordinates": COORDINATES}
    response = requests.post(url, headers=headers, json=payload)

    try:
        data = response.json()
    except Exception as e:
        raise RuntimeError(f"❌ Failed to decode JSON: {e}")

    if "features" not in data:
        raise RuntimeError(f"❌ API response missing 'features'. Full response:\n{data}")

    try:
        segment = data['features'][0]['properties']['segments'][0]
        coords = data['features'][0]['geometry']['coordinates']
    except (IndexError, KeyError) as e:
        raise RuntimeError(f"❌ Error parsing route data: {e}\nFull response:\n{data}")

    df = pd.DataFrame({
        'distance_km': [segment['distance'] / 1000],
        'duration_min': [segment['duration'] / 60]
    })

    # ✅ Pastikan folder output ada
    output_dir = "rute_pipeline/output"
    os.makedirs(output_dir, exist_ok=True)

    # ✅ Simpan CSV ke folder yang sudah dipastikan ada
    df.to_csv(os.path.join(output_dir, "rute.csv"), index=False)

    return coords
