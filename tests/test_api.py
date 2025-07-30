from source_code.tester import run_test_case
from source_code.main import app
import json
import os

def test_simple_case():
    with open("tests/test_cases/test_case_1.json") as f:
        data = json.load(f)
    result = run_test_case(data, app)
    assert result["status"] == "pass"
