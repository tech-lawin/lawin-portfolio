from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing for APIs

@app.route('/')
def home():
    return jsonify({"message": "Backend is running on port 6000!"})

@app.route('/api/test')
def test_endpoint():
    return jsonify({"message": "This is a test endpoint!"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6000)  # Specify port
