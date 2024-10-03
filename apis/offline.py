import sys
import os
import requests
import json

from bs4 import BeautifulSoup

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from apis.crawler import get_html, extract_data, raw_to_ad, load_json_as_objects
from apis.models import City


# update ads json based on city.json
def batch_update():
    # umlaut = {'ä': 'a', 'ö': 'o', 'ü': 'u', 'Ä': 'A', 'Ö': 'O', 'Ü': 'U', 'ß': 'ss'}

    json_data = './wg-gesucht-api/static/json/city.json'
    cities = load_json_as_objects(json_data, City)

    for city in cities:
        city_name = city.city_name
        if 'ö' in city_name:
            city_name = city_name.replace('ö', 'o')
        if 'ü' in city_name:
            city_name = city_name.replace('ü', 'u')
            
        export_json(city_name, city.city_id)


def export_json(city_name, city_id):

    # dusseldorf = 'https://www.wg-gesucht.de/wg-zimmer-in-Duesseldorf.30.0.1.0.html'

    ad_path = f'https://www.wg-gesucht.de/wg-zimmer-in-{city_name}.{city_id}.0.1.0.html'
    
    raw = get_html(ad_path)
    ads = extract_data(raw)

    ads_obj = [raw_to_ad(ad) for ad in ads]

    file_name = f'./wg-gesucht-api/static/json/{city_name}.json'

    with open(file_name, 'w') as json_file:
        json.dump(ads_obj, json_file, indent=4)

    print(f"Data exported to {file_name}")



def query_city():
    # url = 'https://www.wg-gesucht.de/ajax/getCities.php?country_parameter=&query='
    file_name = './wg-gesucht-api/static/json/city.json'

    with open(file_name, 'r') as json_file:
        city_data = json.load(json_file)

    cities = [City(**data) for data in city_data]

    return cities


if __name__ == "__main__":
    batch_update()