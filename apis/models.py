import json
class Zimmer:

    def __init__(self, title, rooms, district, street, rent, availability, size, author, online, link, image):
        self.title = title
        self.rooms = rooms
        self.district = district
        self.street = street
        self.rent = rent
        self.availability = availability
        self.size = size
        self.author = author
        self.online = online
        self.link = link
        self.image = image

    def display_info(self):
        print(f"Title: {self.title}, Rooms: {self.rooms}")

class City:

    def __init__(self, city_id, city_name, country_code, federated_state_id, city_and_state):
        self.city_id = city_id
        self.city_name = city_name
        self.country_code = country_code
        self.federated_state_id = federated_state_id
        self.city_and_state = city_and_state