from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access

@app.route('/')
def home():
    return jsonify({"message": "Backend is running!"})

@app.route('/api/test')
def test():
    return jsonify({"message": "Test endpoint working!"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
