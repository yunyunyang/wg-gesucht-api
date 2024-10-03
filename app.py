from flask import Flask, render_template
from apis.crawler import load_json_as_objects
from apis.offline import query_city

from apis.models import Zimmer

app = Flask(__name__)

@app.route('/')
def index():

    cities = query_city()
    print(len(cities))

    # Read from json
    file_name = './wg-gesucht-api/static/json/dusseldorf.json'

    zimmers = load_json_as_objects(file_name, Zimmer)

    return render_template('index.html', cities=cities, zimmers=zimmers)


if __name__ == '__main__':
    app.run(debug=True)