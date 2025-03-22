import os
import json
import gspread

from src.api.models import Zimmer

from oauth2client.service_account import ServiceAccountCredentials as SAC

# Get the absolute path to the project root directory by going two levels up
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))


def save_google_sheet(result: str):

    keyfile = file_path = os.path.join(project_root, "env", "wg-gesucht-454420-78dfeac6dc8a.json")

    url = ["https://spreadsheets.google.com/feeds"]

    connect = SAC.from_json_keyfile_name(keyfile, url)
    google_sheets = gspread.authorize(connect)

    sheet = google_sheets.open_by_key("1rwCK6hguccdolB5atTgDu5o5he8804Cv0TKCn4cnCO8")
    sheets = sheet.sheet1

    # data_title = ["title", "rooms", "district", "rent", "availability", "online", "link"]
    # sheets.append_row(data_title)

    for room in result:
        data = [room.title, room.rooms, room.district, room.rent, room.availability, room.online, room.link]
        sheets.append_row(data)

    
    # city = 'Koln'

    # # Construct the full file path to the city JSON file inside the static folder
    # file_path = os.path.join(project_root, 'static', 'json', f"{city}.json")
    

    # if os.path.exists(file_path):
    #     with open(file_path, 'r') as json_file:
            




