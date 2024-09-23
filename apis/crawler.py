import requests
from bs4 import BeautifulSoup
# from datetime import datetime
# import time

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

        title = div.h3.text.strip()
        rooms, district, street = div.find("div", {"class": "col-xs-11"}).span.text.strip().replace('\n', '').replace(' ', '').split('|')
        rent = div.b.text
        publish = div.find("div", {"class": "col-xs-5"}).text.strip()

        size = div.find("div", {"class": "col-xs-3 text-right"}).b
        if size:
            size = div.find("div", {"class": "col-xs-3 text-right"}).b.text.strip()

        author, online = div.find("div", {"class": "col-sm-12 flex_space_between", "style": "min-height: 18px;"}).text.strip().split('\n')

        zimmer = Zimmer(title, rooms, district, street, rent, publish, size, author, online)
        ads.append(zimmer)
    
    return ads



dusseldorf = 'https://www.wg-gesucht.de/wg-zimmer-in-Duesseldorf.30.0.1.0.html'
raw = get_html(dusseldorf)
html = extract_data(raw)

for ad in html:
    print(ad.title)