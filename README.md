# WG-Gesucht API

A Python-based project that scrapes and interacts with the [WG-Gesucht](https://www.wg-gesucht.de/) website, which helps users find shared apartments and accommodation in Germany.

## Features

- Scrapes listings from WG-Gesucht
- Filters partner ads and retrieves room data such as location, price, and availability
- Uses Flask for rendering and managing the web interface
- Added JSON serialization and deserialization to enable offline functionality

## Technologies

- **Backend** Python, Flask
- **Frontend** HTML, CSS, Javascript, Bootstrap
- **Tools** Git, Github, Visual Studio Code

## Troubleshooting

- **Access to 127.0.0.1 was denied**
  - Open a new tab in Chrome and type in the address: chrome://net-internals/#sockets
  - Click on “Flush socket pools”
