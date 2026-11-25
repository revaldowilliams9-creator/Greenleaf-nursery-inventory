# GreenLeaf Nursery Inventory Manager

A lightweight full-stack web application built with **Python**, **Flask**, and **SQLite** that allows nursery staff to view current plant inventory and dynamically update retail pricing through a browser interface.

## Features
- **Automated Database Seeding:** Initializes a local SQLite database (`nursery.db`) and populates starter inventory on launch.
- **Home Navigation Hub (`/`):** Provides quick browser navigation across inventory and pricing routes.
- **Live Inventory View (`/plants`):** Queries the database and renders a clean HTML table of plant IDs, names, and prices in ZAR (`R`).
- **Validated Price Updates (`/update`):** Supports both `GET` and `POST` requests with server-side validation to reject missing fields, negative prices, or non-existent plant IDs.

<img width="511" height="95" alt="image" src="https://github.com/user-attachments/assets/516fdddf-10ff-43f1-84c2-1d135c075ca6" />


## Application Routes

| Route | Methods | Description |
| :--- | :--- | :--- |
| `/` | `GET` | Welcome page with navigation links to inventory and price updates |
| `/plants` | `GET` | Displays the live plant catalog and current ZAR pricing |
| `/update` | `GET`, `POST` | Form and backend handler for validating and updating plant prices |

## Tech Stack
- **Backend:** Python 3, Flask
- **Database:** SQLite3
- **Frontend:** HTML5

## Getting Started
```bash
pip install flask
python app.py
```
Then open `http://127.0.0` in your browser.

I built this web application to practice connecting a Python backend to a relational SQLite database with full CRUD functionality. My goal was to replace static spreadsheets with a clean browser interface that enforces strict server-side input validation against negative prices or invalid product IDs.
