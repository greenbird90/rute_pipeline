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

def compose_message_from_csv(csv_path, jalan_list=None):
    df = pd.read_csv(csv_path)
    distance_km = df['distance_km'].iloc[0]
    duration_min = df['duration_min'].iloc[0]

    total_seconds = int(duration_min * 60)
    jam = total_seconds // 3600
    menit = (total_seconds % 3600) // 60
    detik = total_seconds % 60

    jalur = "Kantor"
    if jalan_list:
        for j in jalan_list[:5]:  # batasi jumlah jalan agar pesan tidak terlalu panjang
            jalur += f" > {j}"
        jalur += " > Rumah"
    else:
        jalur += " > Jl. A > Jl. B > Rumah"

    message = (
        "🚗 <b>Rute Hari Ini</b>\n"
        "🧭 Dari: Telkomsel Smart Office\n"
        "🏡 Ke: Pamulang Barat\n"
        f"📏 Jarak: {distance_km:.2f} km\n"
        f"⏱️ Estimasi Waktu: {jam} jam {menit} menit {detik} detik\n"
        f"🛣️ Jalur: {jalur}"
    )
    return message
