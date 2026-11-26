# 🌿 GreenLeaf Nursery Inventory Manager

A lightweight full-stack web application built with **Python**, **Flask**, and **SQLite** that allows nursery staff to view current plant inventory and dynamically update retail pricing through a browser interface.

## 💡 Why I Built This
I built this web application to practice connecting a Python backend to a relational SQLite database with full CRUD functionality. My goal was to replace static spreadsheets with a clean browser interface that enforces strict server-side input validation against negative prices or invalid product IDs.

## ✨ Key Features
* 🌱 **Automated Database Seeding:** Initializes a local SQLite database (`nursery.db`) and populates starter inventory on launch.
* 🧭 **Home Navigation Hub (`/`):** Provides quick browser navigation across inventory and pricing routes.
* 📋 **Live Inventory View (`/plants`):** Queries the database and renders a clean HTML table of plant IDs, names, and prices in ZAR (`R`).
* 🛡️ **Validated Price Updates (`/update`):** Supports both `GET` and `POST` requests with server-side validation to reject missing fields, negative prices, or non-existent plant IDs.

## 📸 Live Preview
<img width="700" height="130" alt="GreenLeaf Nursery Current Price List" src="https://github.com/user-attachments/assets/15590339-79d0-4208-b924-c6821bcc8026" />

## 🛣️ Application Routes

| Route | Methods | Description |
| :--- | :--- | :--- |
| `/` | `GET` | Welcome page with navigation links to inventory and price updates |
| `/plants` | `GET` | Displays the live plant catalog and current ZAR pricing |
| `/update` | `GET`, `POST` | Form and backend handler for validating and updating plant prices |

## 🛠️ Tech Stack
* **Backend:** Python 3, Flask
* **Database:** SQLite3
* **Frontend:** HTML5

## 🚀 Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd Greenleaf-nursery-inventory
   ```

2. **Install Flask and launch the server:**
   ```bash
   pip install flask
   python app.py
   ```

3. **Open the app in your browser:**
   Navigate to `http://127.0.0` to access the nursery dashboard.
