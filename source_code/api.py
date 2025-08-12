from flask import Flask, request, jsonify
import joblib
from .tester import run_test_case
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the trained ML model
try:
    model = joblib.load('trained_model.pkl')
    print("✅ Model loaded successfully.")
except FileNotFoundError:
    model = None
    print("❌ trained_model.pkl not found. Please train the model first.")

# API test route
@app.route('/test', methods=['POST'])
def test_api():
    if model is None:
        return jsonify({"error": "Model not loaded. Please train it first."}), 500

    data = request.json
    result = run_test_case(data, model)
    return jsonify(result)