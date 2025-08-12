import os
import sys
import json
import requests

# Dynamically add the root project directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from source_code.api import app  # Only needed if testing local Flask/FastAPI routes
from source_code.tester import run_test_case

def test_simple_case():
    with open("tests/test_cases/test_case_1.json") as f:
        data = json.load(f)

    # Check if the test case includes a live API endpoint
    if "url" in data:
        response = requests.request(
            method=data.get("method", "GET"),
            url=data["url"],
            headers=data.get("headers", {}),
            json=data.get("body", {})
        )

        result = {
            "status_code": response.status_code,
            "response_body": response.json() if "application/json" in response.headers.get("Content-Type", "") else response.text
        }

        print("Live API Response:", result)
        assert result["status_code"] == data.get("expected_status", 200)

    else:
        # Local API testing (through tester.py logic)
        result = run_test_case(data, app)
        print("Local Test Result:", result)
        assert result["status"] == "Test Passed"