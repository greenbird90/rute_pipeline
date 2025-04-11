from ors_request import fetch_rute_info
from visualize_map import create_map
from save_to_sheets import save_to_google_sheets
from telegram_notif import send_telegram_message, compose_message_from_csv
import pandas as pd
import os

def run():
    print("🚀 Menjalankan pipeline ETL rute harian...")
    coords, jalan = fetch_rute_info()
    create_map(coords)
    df = pd.read_csv("rute_pipeline/output/rute.csv")
    save_to_google_sheets(df, os.getenv("SHEET_NAME"))
    message = compose_message_from_csv("rute_pipeline/output/rute.csv", jalan)
    send_telegram_message(os.getenv("BOT_TOKEN"), os.getenv("CHANNEL_ID"), message)

if __name__ == "__main__":
    run()
