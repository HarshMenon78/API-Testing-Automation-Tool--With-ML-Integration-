from flask import Flask, request, jsonify
from .tester import run_test_case
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load your ML model (mocked for now)
model = None  # Placeholder for ML model

# API test route
@app.route('/test', methods=['POST'])
def test_api():
	data = request.json
	result = run_test_case(data, model)
	return jsonify(result)