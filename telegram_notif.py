
import requests
import pandas as pd

def send_telegram_message(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML"
    }
    requests.post(url, data=payload)

def compose_message_from_csv(csv_path):
    df = pd.read_csv(csv_path)
    distance = df['distance_km'].iloc[0]
    duration = df['duration_min'].iloc[0]
    return f"🚗 <b>Rute Hari Ini</b>\nJarak: {distance:.2f} km\nEstimasi Waktu: {duration:.1f} menit"
