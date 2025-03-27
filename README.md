# WG-Gesucht API

A Python-based project that scrapes search results from the [WG-Gesucht](https://www.wg-gesucht.de/) website and creates APIs for further use, such as saving search results to Google Sheets. This helps users find the latest shared apartments and accommodation in Germany.

## Prerequisite

```bash
$ git clone https://github.com/yunyunyang/wg-gesucht-api.git
$ cd wg-gesucht-api
$ pip install -r requirements.txt
```

## Features

- Scrapes listed rooms from WG-Gesucht by providing a location and relevant data
- Filters partner ads and retrieves room data such as location, price, and availability
- Uses the FastAPI framework to provide APIs
- Provides the feature to store data in Google Sheets

## How to enable Google Sheets API

- Follow the steps to enable APIs https://support.google.com/googleapi/answer/6158841?hl=en

- After enabling the APIs, create the credentials by choosing Service Accounts, which enable server-to-server, app-level authentication using robot accounts.
- Create a new key, then save the JSON file for future use
- Create a new Google Sheet and add the email listed under Service Accounts, granting access as an editor
- The following is a code snippet to read the JSON file and save the data to Google Sheets

```python
import gspread

from oauth2client.service_account import ServiceAccountCredentials as SAC

# The credentials.json is the JSON file generated when you create a new key
keyfile = os.path.join(project_root, "env", "credentials.json")

# Define the scope of the API access
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

connect = SAC.from_json_keyfile_name(keyfile, scope)
google_sheets = gspread.authorize(connect)

# The spreadsheet_key is the identifier for the Google Sheet you created
worksheet = google_sheets.open_by_key("spreadsheets_key")
sheet = worksheet.sheet1

data_title = ["title", "rooms", "district", "rent", "availability", "online", "link"]
sheet.append_row(data_title)
sheet.append_row(data)
```

## Docker

```bas
# Build the Docker Image
docker build -t wg-gesucht:1.0 .

# Run the Docker Container
docker run -p 8000:8000 wg-gesucht:1.0
```

## Demos

![Google Sheets](static/images/google-sheets.png)
