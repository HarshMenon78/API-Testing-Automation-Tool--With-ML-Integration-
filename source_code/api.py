from flask import Flask, request, jsonify
from .tester import run_test_case
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load your ML model (mocked for now)
model = None  # Placeholder for ML model

@app.route('/test', methods=['POST'])
def test_api():
    try:
        data = request.json
        result = run_test_case(data, model)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
