from flask import Flask, render_template
from apis.crawler import get_html, extract_data

app = Flask(__name__)

@app.route('/')
def index():

    dusseldorf = 'https://www.wg-gesucht.de/wg-zimmer-in-Duesseldorf.30.0.1.0.html'
    raw = get_html(dusseldorf)
    zimmers = extract_data(raw)

    return render_template('index.html', name='World', zimmers=zimmers)


if __name__ == '__main__':
    app.run(debug=True)