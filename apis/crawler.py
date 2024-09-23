import sys
import os
import requests
import json

from bs4 import BeautifulSoup
# from datetime import datetime
# import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from apis.models import Zimmer

# date_format = '%d%m%Y'

def get_html(url):
    
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Connection': 'keep-alive'
    }

    try:
        response = requests.get(url, headers=headers)
        # Check if the request was successful
        response.raise_for_status()
        return response.text
    
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch {url}: {e}")
        return


def extract_data(raw):
    
    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(raw, 'html.parser')

    divs = soup.find_all("div", {"class": "wgg_card offer_list_item"})
    
    ads = []

    for div in divs:
        
        # Title
        title = div.h3.text.strip()

        # Rooms, District, Street
        rooms, district, street = div.find("div", {"class": "col-xs-11"}).span.text.strip().replace('\n', '').split('|')
        rooms = rooms.replace('er WG', '').strip()
        # district = district.strip()
        district = ' '.join(district.split())
        street = street.strip()

        # Rent
        rent = div.b.text

        # Availability
        availability = div.find("div", {"class": "col-xs-5"}).text.strip()

        # Size
        size = div.find("div", {"class": "col-xs-3 text-right"}).b
        size = size.text.strip() if size else size

        # Author, Online
        author, online = div.find("div", {"class": "col-sm-12 flex_space_between", "style": "min-height: 18px;"}).text.strip().split('\n')
        online = online.replace('Online: ', '')

        # Link
        link = div.find("a", href=True)
        link = 'https://www.wg-gesucht.de/en' + link['href']

        zimmer = Zimmer(title, rooms, district, street, rent, availability, size, author, online, link)
        ads.append(zimmer)
    
    return ads


def serialize(zimmer):
    return {
        'title': zimmer.title,
        'rooms': zimmer.rooms,
        'district': zimmer.district,
        'street': zimmer.street,
        'rent': zimmer.rent,
        'availability': zimmer.availability,
        'size': zimmer.size,
        'author': zimmer.author,
        'online': zimmer.online,
        'link': zimmer.link
    }

def deserialize(file_name):

    with open(file_name, 'r') as json_file:
        zimmers_data = json.load(json_file)

    # Convert the JSON data into a list of Apartment objects
    ads = [Zimmer(**data) for data in zimmers_data]

    return ads


def export_json():

    dusseldorf = 'https://www.wg-gesucht.de/wg-zimmer-in-Duesseldorf.30.0.1.0.html'
    
    raw = get_html(dusseldorf)
    ads = extract_data(raw)

    ads_dict = [serialize(ad) for ad in ads]

    file_name = './wg-gesucht-api/static/json/dusseldorf.json'

    with open(file_name, 'w') as json_file:
        json.dump(ads_dict, json_file, indent=4)

    print(f"Data exported to {file_name}")



export_json()
# dusseldorf = 'https://www.wg-gesucht.de/wg-zimmer-in-Duesseldorf.30.0.1.0.html'
# raw = get_html(dusseldorf)
# ads = extract_data(raw)

