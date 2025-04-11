
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

def save_to_google_sheets(dataframe, spreadsheet_name, worksheet_name="Sheet1"):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)

    sheet = client.open(spreadsheet_name)
    worksheet = sheet.worksheet(worksheet_name)
    worksheet.clear()
    worksheet.append_row(list(dataframe.columns))
    for row in dataframe.itertuples(index=False):
        worksheet.append_row(list(row))
