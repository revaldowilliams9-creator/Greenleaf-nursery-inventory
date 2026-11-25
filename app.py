from flask import Flask, request
import sqlite3

app = Flask(__name__)

def initialize_database():
    connection = sqlite3.connect("nursery.db")
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS plants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL
    )
    """)
    # Seed the table with sample plants if it is empty
    cursor.execute("SELECT COUNT(*) FROM plants")
    if cursor.fetchone()[0] == 0:
        sample_plants = [("Fern", 45.00), ("Aloe Vera", 30.00), ("Basil", 15.00)]
        cursor.executemany("INSERT INTO plants (name, price) VALUES (?, ?)", sample_plants)
    connection.commit()
    connection.close()

# Initialise database when app starts
initialize_database()

@app.route("/")
def home():
    return """
    <h2>GreenLeaf Nursery App is running!</h2>
    <p><a href="/plants">View Plant Inventory</a> | <a href="/update">Update a Plant Price</a></p>
    """

# ADDED ROUTES & LOGIC FOR UPDATING PLANT PRICES


@app.route("/update", methods=["GET", "POST"])
def update_price():
    if request.method == "POST":
        # Retrieve form data
        plant_id = request.form.get("plant_id")
        new_price = request.form.get("new_price")
        
        # Validation block
        if not plant_id or not new_price:
            return "<h3>Error: Both Plant ID and New Price are required fields.</h3><a href='/update'>Try Again</a>"
        
        try:
            plant_id = int(plant_id)
            new_price = float(new_price)
            if new_price < 0:
                return "<h3>Error: Price cannot be negative.</h3><a href='/update'>Try Again</a>"
        except ValueError:
            return "<h3>Error: Invalid numerical values provided.</h3><a href='/update'>Try Again</a>"
            
        # Connect and execute UPDATE operation
        connection = sqlite3.connect("nursery.db")
        cursor = connection.cursor()
        
        # Verify if the plant exists in the database
        cursor.execute("SELECT * FROM plants WHERE id = ?", (plant_id,))
        if cursor.fetchone() is None:
            connection.close()
            return f"<h3>Error: Plant with ID {plant_id} does not exist.</h3><a href='/update'>Try Again</a>"
            
        # Run the update statement
        cursor.execute("UPDATE plants SET price = ? WHERE id = ?", (new_price, plant_id))
        connection.commit()
        connection.close()
        
        return f"<h3>Success: Price for Plant ID {plant_id} updated to R{new_price:.2f}!</h3><br><a href='/plants'>View Updated Plant List</a>"

    # GET Request: Return the HTML form to update plant prices
    html_form = """
    <html>
        <head><title>Update Plant Price</title></head>
        <body>
            <h2>GreenLeaf Nursery - Update Plant Price</h2>
            <form method="POST" action="/update">
                <label for="plant_id">Plant ID:</label><br>
                <input type="number" id="plant_id" name="plant_id" required><br><br>
                
                <label for="new_price">New Price (R):</label><br>
                <input type="number" step="0.01" id="new_price" name="new_price" required><br><br>
                
                <input type="submit" value="Update Price">
            </form>
            <br>
            <a href="/plants">View Current Price List</a>
        </body>
    </html>
    """
    return html_form


@app.route("/plants")
def view_plants():
    connection = sqlite3.connect("nursery.db")
    cursor = connection.cursor()
    
    # Query all plant entries
    cursor.execute("SELECT id, name, price FROM plants")
    all_plants = cursor.fetchall()
    connection.close()
    
    # Build a clean HTML page displaying results
    html_output = """
    <html>
        <head>
            <title>Plant Inventory</title>
        </head>
        <body>
            <h2>GreenLeaf Nursery - Current Price List</h2>
            <table border="1" cellpadding="8" cellspacing="0">
                <tr>
                    <th>ID</th>
                    <th>Plant Name</th>
                    <th>Price</th>
                </tr>
    """
    
    for plant in all_plants:
        html_output += f"""
                <tr>
                    <td>{plant[0]}</td>
                    <td>{plant[1]}</td>
                    <td>R{plant[2]:.2f}</td>
                </tr>
        """
        
    html_output += """
            </table>
            <br>
            <a href="/update">Update a Plant Price</a> | <a href="/">Home</a>
        </body>
    </html>
    """
    return html_output

# Run application with debug mode on
if __name__ == "__main__":
    app.run(debug=True)
