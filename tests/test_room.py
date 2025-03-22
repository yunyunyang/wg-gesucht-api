import os
import sys
import json
import unittest
import jsonschema
from jsonschema import validate

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.api.room import query_room
from src.api.models import Zimmer

class Test(unittest.TestCase):
  
    def test_query_room(self):
        
        city_name = "Aachen"
        city_id = "1"
        page_id = 1

        room_list = query_room(city_name, city_id, page_id)

        # Convert the list of Zimmer objects to a list of dictionaries
        room_dicts = [zimmer.to_dict() for zimmer in room_list]

        # Serialize it to JSON
        room_json = json.dumps(room_dicts, indent=4)

        # Deserialize JSON
        room_data = json.loads(room_json)
        
        schema = {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "rooms": {"type": "string"},
                    "district": {"type": "string"},
                    "street": {"type": "string"},
                    "rent": {"type": "string"},
                    "availability": {"type": "string"},
                    "size": {"type": "string"},
                    "author": {"type": "string"},
                    "online": {"type": "string"},
                    "link": {"type": "string"}
                },
                "required": ["title", "rooms", "district", "street", "rent", "availability", "size", "author", "online", "link"]
            }
        }

        try:
            validate(instance=room_data, schema=schema)
        except jsonschema.exceptions.ValidationError as e:
            print(f"JSON is invalid: {e.message}")
        except jsonschema.exceptions.SchemaError as e:
            print(f"Invalid schema: {e.message}")


if __name__ == "__main__":
    unittest.main()