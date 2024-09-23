from flask import Flask, render_template
from apis.crawler import deserialize
from apis.crawler import get_html, extract_data, export_json

app = Flask(__name__)

@app.route('/')
def index():

    # Realtime data
    # export_json()

    # Read from json
    file_name = './wg-gesucht-api/static/json/dusseldorf.json'

    zimmers = deserialize(file_name)

    return render_template('index.html', name='World', zimmers=zimmers)


if __name__ == '__main__':
    app.run(debug=True)