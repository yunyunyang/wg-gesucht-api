import sys
import os
import json

# Get the absolute path to the project root directory by going two levels up
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

def query_city(keyword: str):

    # Locate the file
    initial = keyword[0].lower()

    # Construct the full file path to the city JSON file inside the static folder
    file_path = os.path.join(project_root, 'static', 'json', 'cities', f"{initial}.json")
    
    # Check if the file exists and read it
    if os.path.exists(file_path):
        with open(file_path, 'r') as json_file:

            cities = json.load(json_file)

            # Filter cities where the city_name starts with city_name keyword
            filtered_cities = [
                {"city_id": city["city_id"], "city_name": city["city_name"]}
                for city in cities if city["city_name"].lower().startswith(keyword.lower())
            ]

        return filtered_cities
    
    else:
        return {"error": f"City {keyword} not found"}

