class Zimmer:

    def __init__(self, title, rooms, district, street, rent, availability, size, author, online):
        self.title = title
        self.rooms = rooms
        self.district = district
        self.street = street
        self.rent = rent
        self.availability = availability
        self.size = size
        self.author = author
        self.online = online


    def display_info(self):
        print(f"Title: {self.title}, Rooms: {self.rooms}")