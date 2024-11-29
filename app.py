from flask import Flask, request, jsonify
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv('DB_PASSWORD'),  # Access the password from environment variable
    database="portfolio"
)

cursor = db.cursor()

# API endpoint to store visitor information
@app.route('/api/store-visitor', methods=['POST'])
def store_visitor():
    # Get visitor's IP address from the request headers
    ip = request.remote_addr  # Flask automatically extracts the visitor's IP address
    
    # Get user agent from the incoming data
    data = request.json
    user_agent = data.get('userAgent')
    visit_time = datetime.now()  # Capture the current time

    try:
        # Insert visitor data into the MySQL database
        cursor.execute(
            "INSERT INTO visitors (ip_address, user_agent, visit_time) VALUES (%s, %s, %s)",
            (ip, user_agent, visit_time)
        )
        db.commit()  # Commit the transaction
        return jsonify({"message": "Visitor info stored successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)


# from flask import Flask, request, jsonify
# import mysql.connector
# import os  # Import the os module to access environment variables
# from datetime import datetime

# app = Flask(__name__)

# # Database connection using environment variables
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",  # You can also store your username in a secret if needed
#     password=os.getenv('DB_PASSWORD'),  # Access the password from environment variable
#     database="portfolio"
# )

# cursor = db.cursor()

# # API endpoint to store visitor information
# @app.route('/api/store-visitor', methods=['POST'])
# def store_visitor():
#     data = request.json
#     ip = data.get('ip')
#     user_agent = data.get('userAgent')
#     visit_time = datetime.now()

#     try:
#         cursor.execute(
#             "INSERT INTO visitors (ip_address, user_agent, visit_time) VALUES (%s, %s, %s)",
#             (ip, user_agent, visit_time)
#         )
#         db.commit()
#         return jsonify({"message": "Visitor info stored successfully!"}), 201
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)
