from flask import Flask, render_template, request, jsonify
import mysql.connector
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv('DB_PASSWORD'),  # Secure the password with an environment variable
    database="portfolio"
)

cursor = db.cursor()

# Route to serve index.html
@app.route('/')
def index():
    """
    Serves the homepage (index.html).
    """
    return render_template('index.html')

# API to store visitor info
@app.route('/api/store-visitor', methods=['POST'])
def store_visitor():
    try:
        data = request.get_json()  # Get JSON data from the request
        print(f"Received data: {data}")  # Log the incoming data
        ip = data.get('ip') if data else None  # Extract IP or set to None if no data
        user_agent = data.get('userAgent') if data else None
        visit_time = datetime.now()

        # Insert visitor info into the database
        cursor.execute(
            "INSERT INTO visitors (ip_address, user_agent, visit_time) VALUES (%s, %s, %s)",
            (ip, user_agent, visit_time)
        )
        db.commit()
        print("Data inserted successfully.")
        return jsonify({"message": "Visitor info stored successfully!"}), 201
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
