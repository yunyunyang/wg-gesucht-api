from flask import Flask, render_template
from apis.crawler import deserialize

app = Flask(__name__)

@app.route('/')
def index():

    file_name = './wg-gesucht-api/static/json/dusseldorf.json'
    zimmers = deserialize(file_name)

    return render_template('index.html', name='World', zimmers=zimmers)


if __name__ == '__main__':
    app.run(debug=True)