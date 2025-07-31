import os
import sys

# Dynamically add the root project directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from source_code.api import app
from source_code.tester import run_test_case

import json
import os

def test_simple_case():
    with open("tests/test_cases/test_case_1.json") as f:
        data = json.load(f)
    result = run_test_case(data, app)
    assert result["status"] == "pass"
