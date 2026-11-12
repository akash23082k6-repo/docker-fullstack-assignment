import os
from flask import Flask, request, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# MongoDB configuration
mongo_uri = os.getenv("MONGO_URI")

client = None
collection = None

if mongo_uri:
    client = MongoClient(
        mongo_uri,
        serverSelectionTimeoutMS=5000
    )

    db = client["flask_assignment"]
    collection = db["form_submissions"]


# Home route
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Flask Backend is running successfully"
    })


# Health check
@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy"
    })


# Receive frontend form data
@app.route("/api/submit", methods=["POST"])
def submit():

    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "message": "No data received"
            }), 400

        name = data.get("name")
        email = data.get("email")

        if not name or not email:
            return jsonify({
                "message": "Name and email are required"
            }), 400

        if collection is None:
            return jsonify({
                "message": "Database configuration is missing"
            }), 500

        # Save data in MongoDB
        submission = {
            "name": name,
            "email": email
        }

        collection.insert_one(submission)

        return jsonify({
            "message": "Data submitted successfully"
        }), 201

    except Exception as error:
        print("Error:", error)

        return jsonify({
            "message": "Something went wrong"
        }), 500


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
