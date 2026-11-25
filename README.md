# GreenLeaf Nursery Inventory Manager

A lightweight web application built with Python, Flask, and SQLite that allows nursery staff to view current plant inventory and update retail pricing through a browser interface.

## Features
- **Automated Database Seeding:** Initializes a local SQLite database (`nursery.db`) and populates starter inventory on launch.
- **Live Inventory View (`/plants`):** Queries the database and renders a clean HTML table of plant IDs, names, and prices in ZAR (`R`).
- **Validated Price Updates (`/update`):** Supports both `GET` and `POST` requests with server-side validation to reject missing fields, negative prices, or non-existent plant IDs.

## Getting Started
```bash
pip install flask
python app.py
```
Then open `http://127.0.0` in your browser.
